__author__ = 'Jager'
from equipmanager import EquipmentManager
from classes.warrior import Warrior
from classes.priest import Priest
from classes.mage import Mage
from classes.rouge import Rouge
from char import Character
from clothtype import ClothType
from hands import Hands
import random


class GameManager:
    def __init__(self):
        self.equipmanager = EquipmentManager()
        self.players = []

    def startgame(self):
        self.initplayers()
        self.game()

    def initplayers(self):
        p1 = Warrior('Meister', 'Human', 'Warrior')
        p2 = Priest('Jager', 'Undead', 'Priest')
        self.players.append(p1)
        self.players.append(p2)
        self.set_equipments()

    def set_equipments(self):
        print("Setting equipments...\n")
        while True:
            chosen = self.char_choose()
            if chosen is None: break
            while True:
                setanother = self.set_cloth(chosen)
                if not(setanother): break
            while True:
                setanother = self.set_weapons(chosen)
                if not(setanother): break

    def char_choose(self):
        self.show_players()
        chosen = input("\nChose a character: " )
        try:
            chosen = int(chosen)
        except ValueError:
            print("Nothing is chosen")
            return None
        if 0 <= chosen < len(self.players):
            print("\n-{}- is chosen\n".format(self.players[chosen].cname))
            return self.players[chosen]
        else:
            return None

    def set_cloth(self, character):
        self.show_clothes()
        chosen = input("\nChoose a cloth: ")
        try:
            chosen = int(chosen)
        except ValueError:
            print("Nothing is chosen")
            return False
        if 0 <= chosen < len(self.equipmanager.clothes):
            chosencloth = self.equipmanager.clothes[chosen]
            if character.setcloth(ClothType.fromstring(chosencloth.type), chosencloth):
                print("\n-{}- is set to {}\n".format(chosencloth.name, character.cname))
            return True
        else:
            return False

    def set_weapons(self, character):
        self.show_weapons()
        chosen = input("\nChoose a weapon: [weapon id] [hand - left(0), right(1)] ")
        try:
            values = chosen.split(' ')
            chosen = int(values[0])
            hand = int(values[0])
            if(hand == 0):
                hand = Hands.left
            else:
                hand = Hands.right
        except:
            print("Nothing is chosen")
            return False
        if 0 <= chosen < len(self.equipmanager.weapons):
            chosenweapon = self.equipmanager.weapons[chosen]
            if(character.setweapon(hand, chosenweapon)):
                 print("\n-{}- is set to {}\n".format(chosenweapon.name, character.cname))
            return True
        else:
            return False

    def show_players(self):
        i = 0
        for c in self.players:
            print("[{}] {}".format(i, c.cname))
            i += 1

    def show_clothes(self):
        i = 0
        for e in self.equipmanager.clothes:
            print("[{}] {}".format(i, e.__str__()))
            i += 1

    def show_weapons(self):
        i = 0
        for w in self.equipmanager.weapons:
            print("[{}] {}".format(i, w.__str__()))
            i += 1

    def show_equipment(self):
        self.show_clothes()
        print("\n")
        self.show_weapons()

    @staticmethod
    def hitdamage(attacker, dmg):
        print('{} attacked with {} damage'.format(attacker.cname, dmg))

    @staticmethod
    def specattack(attacker, attackname):
        print("{} attacked with {}".format(attacker.cname, attackname))

    @staticmethod
    def gameround(player1, player2):
        dmg = player1.hit(player2, GameManager.hitdamage)
        if(player1.health < player1.maxhp*0.2 and player1.canheal()): print("{} healed {} on himself".format(player1.cname, player1.heal(player1)))
        else:
            dmg += player1.special_attack1(player2, GameManager.hitdamage, GameManager.specattack)
        print('{} got {} damage from {}'.format(player2.cname,  str(dmg), player1.cname))

    def game(self):
        player0 = self.players[0]
        player1 = self.players[1]
        player0.full_resource()
        player1.full_resource()
        print(player0.__str__())
        print(player1.__str__())
        print('======= Let the fight begin! =======')
        while(player0.isalive() and player1.isalive()):
            if(random.randint(1,100) < 50):
                attacker = player0
                opponent = player1
            else:
                attacker = player1
                opponent = player0
            print('ATTACKER: ' + attacker.state())
            print('OPPONENT: ' + opponent.state())
            GameManager.gameround(attacker, opponent)
            if(not(opponent.isalive())): break
            GameManager.gameround(opponent, attacker)
            attacker.regen_resource()
            opponent.regen_resource()
            print()
            input("--------------------")

        print("\nFight result:\n")
        print(player0.state())
        print(player1.state())
        if(player1.isalive()): winner = player1
        else: winner = player0
        print("The winner is {}".format(winner.cname.upper()))



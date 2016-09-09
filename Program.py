__author__ = 'Jager'
from char import Character
from cloth import Cloth
from weapon import Weapon
import random
from time import sleep
from hands import Hands
from clothtype import ClothType
from classes.warrior import Warrior
from classes.priest import Priest
from classes.mage import Mage
from classes.rouge import Rouge

meister = Warrior('Meister', 'Human', 'Warrior')
jager = Priest('Jager', 'Undead', 'Priest')

w_sword1 = Weapon('Sword of Oblivion', 50)
w_sword2 = Weapon('Warglaive of Azzinoth', 30)
w_axe1 = Weapon('Axe of Destruction', 70)
w_dagger1 = Weapon('Dagger of Time', 20)
w_staff1 = Weapon('Staff of Gandalf', 80)


meister.setweapon(Hands.right, w_dagger1)
meister.setweapon(Hands.left, w_axe1)

meister.setcloth(ClothType.chest, Cloth('Leather chestpiece', 60))
meister.setcloth(ClothType.legs, Cloth('Leather leggins', 50))
meister.setcloth(ClothType.hands, Cloth('Leather gloves', 30))
meister.setcloth(ClothType.feet, Cloth('Leather boots', 35))


jager.setweapon(Hands.right, w_staff1)

jager.setcloth(ClothType.chest, Cloth('Cloak of Invincibility', 50, 60))
jager.setcloth(ClothType.legs, Cloth('Trausers of Medivh', 40, 25))
jager.setcloth(ClothType.head, Cloth('Hood of Valor', 20, 30))
jager.setcloth(ClothType.feet, Cloth('Boots of Magic', 10, 15))

def hitdamage(attacker, dmg):
    print('{} attacked with {} damage'.format(attacker.cname, dmg))


def specattack(attacker, attackname):
    print("{} attacked with {}".format(attacker.cname, attackname))

def round(player1, player2):
    dmg = player1.hit(player2, hitdamage)
    if(player1.health < player1.maxhp*0.2 and player1.canheal()): print("{} healed {} on himself".format(player1.cname, player1.heal(player1)))
    else:
        dmg += player1.special_attack1(player2, hitdamage, specattack)
    print('{} got {} damage from {}'.format(player2.cname,  str(dmg), player1.cname))

meister.full_resource()
jager.full_resource()
print(meister.__str__())
print(jager.__str__())
print('======= Let the fight begin! =======')
while(meister.isalive() and jager.isalive()):
    if(random.randint(1,100) < 50):
        attacker = meister
        opponent = jager
    else:
        attacker = jager
        opponent = meister
    print('ATTACKER: ' + attacker.state())
    print('OPPONENT: ' + opponent.state())
    round(attacker, opponent)
    if(not(opponent.isalive())): break
    round(opponent, attacker)
    attacker.regen_resource()
    opponent.regen_resource()
    print()
    input("--------------------")

print("\nFight result:\n")
print(meister.state())
print(jager.state())
if(jager.isalive()): winner = jager
else: winner = meister
print("The winner is {}".format(winner.cname.upper()))




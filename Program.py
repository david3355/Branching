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
from dbhandler.filedb import FileDatabase
from dbhandler.serializer import Serializer


sc = Serializer("db/clothes.db")
sw = Serializer("db/weapons.db")

c1 = Cloth(ClothType.chest, 'Leather chestpiece', 60)
c2 = Cloth(ClothType.legs, 'Leather leggins', 50)
c3 = Cloth(ClothType.hands, 'Leather gloves', 30)
c4 = Cloth(ClothType.feet, 'Leather boots', 35)
c5 = Cloth(ClothType.chest, 'Cloak of Invincibility', 50, 60)
c6 = Cloth(ClothType.legs, 'Trausers of Medivh', 40, 25)
c7 = Cloth(ClothType.head, 'Hood of Valor', 20, 30)
c8 = Cloth(ClothType.feet, 'Boots of Magic', 10, 15)

w_sword1 = Weapon('Sword of Oblivion', 50)
w_sword2 = Weapon('Warglaive of Azzinoth', 30)
w_axe1 = Weapon('Axe of Destruction', 70)
w_dagger1 = Weapon('Dagger of Time', 20)
w_staff1 = Weapon('Staff of Gandalf', 80)


# def saveobjects(serializer, objects):
#     for o in objects:
#         serializer.saveobject(o)
#
# saveobjects(sc, [c1, c2, c3, c4, c5, c6, c7, c8])
# saveobjects(sw, [w_sword1, w_sword2, w_axe1, w_dagger1, w_staff1])

meister = Warrior('Meister', 'Human', 'Warrior')
jager = Priest('Jager', 'Undead', 'Priest')

meister.setweapon(Hands.right, w_dagger1)
meister.setweapon(Hands.left, w_axe1)

meister.setcloth(ClothType.chest, c1)
meister.setcloth(ClothType.legs, c2)
meister.setcloth(ClothType.hands, c3)
meister.setcloth(ClothType.feet, c4)


jager.setweapon(Hands.right, w_staff1)

jager.setcloth(ClothType.chest, c5)
jager.setcloth(ClothType.legs, c6)
jager.setcloth(ClothType.head, c7)
jager.setcloth(ClothType.feet, c8)

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




__author__ = 'Jager'
from char import Character
from cloth import Cloth
from weapon import Weapon
import random
from time import sleep
from hands import Hands
from clothtype import ClothType

jager = Character('Jager', 'Human', 'Rouge')
meister = Character('Meister', 'Undead', 'Warrior')

w_sword1 = Weapon('Sword of Oblivion', 50)
w_sword2 = Weapon('Warglaive of Azzinoth', 30)
w_axe1 = Weapon('Axe of Destruction', 70)
w_dagger1 = Weapon('Dagger of Time', 20)


jager.setweapon(Hands.right, w_dagger1)
jager.setweapon(Hands.left, w_axe1)

jager.setcloth(ClothType.chest, Cloth('Leather chestpiece', 60))
jager.setcloth(ClothType.legs, Cloth('Leather leggins', 50))
jager.setcloth(ClothType.hands, Cloth('Leather gloves', 30))
jager.setcloth(ClothType.feet, Cloth('Leather boots', 35))


meister.setweapon(Hands.right, w_sword1)
meister.setweapon(Hands.left, w_sword2)

meister.setcloth(ClothType.chest, Cloth('Steel chestplate', 120))
meister.setcloth(ClothType.legs, Cloth('Steel leggins', 70))

def hitdamage(attacker, dmg):
    print('{} attacked with {} damage'.format(attacker.cname, dmg))


print(jager.__str__())
print(meister.__str__())
print('======= Let the fight begin! =======')
while(jager.isalive() and meister.isalive()):
    if(random.randint(1,100) < 50):
        attacker = jager
        opponent = meister
    else:
        attacker = meister
        opponent = jager
    print('ATTACKER: ' + attacker.state())
    print('OPPONENT: ' + opponent.state())
    dmg = attacker.hit(opponent, hitdamage)
    print('{} got {} damage from {}'.format(opponent.cname,  str(dmg), attacker.cname))
    dmg = opponent.hit(attacker, hitdamage)
    print('{} got {} damage from {}'.format(attacker.cname, str(dmg), opponent.cname ))
    print()
    sleep(1.2)


print(jager.state())
print(meister.state())




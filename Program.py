__author__ = 'Jager'
from char import Character
from cloth import Cloth
from weapon import Weapon

c1 = Character('Jager', 'Human', 'Rouge')

w_sword = Weapon('Sword', 30)
c1.setweapon('left', w_sword)
cloth_chest=Cloth('Chestplate', 80)
c1.setcloth('chest', cloth_chest)





print(c1.__str__())




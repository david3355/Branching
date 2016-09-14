__author__ = 'Jager'

from gamemanager import GameManager

# c1 = Cloth(ClothType.chest, 'Leather chestpiece', 60)
# c2 = Cloth(ClothType.legs, 'Leather leggins', 50)
# c3 = Cloth(ClothType.hands, 'Leather gloves', 30)
# c4 = Cloth(ClothType.feet, 'Leather boots', 35)
# c5 = Cloth(ClothType.chest, 'Cloak of Invincibility', 50, 60)
# c6 = Cloth(ClothType.legs, 'Trausers of Medivh', 40, 25)
# c7 = Cloth(ClothType.head, 'Hood of Valor', 20, 30)
# c8 = Cloth(ClothType.feet, 'Boots of Magic', 10, 15)
#
# w_sword1 = Weapon('Sword of Oblivion', 50)
# w_sword2 = Weapon('Warglaive of Azzinoth', 30)
# w_axe1 = Weapon('Axe of Destruction', 70)
# w_dagger1 = Weapon('Dagger of Time', 20)
# w_staff1 = Weapon('Staff of Gandalf', 80)


# def saveobjects(serializer, objects):
#     for o in objects:
#         serializer.saveobject(o)
#
# saveobjects(sc, [c1, c2, c3, c4, c5, c6, c7, c8])
# saveobjects(sw, [w_sword1, w_sword2, w_axe1, w_dagger1, w_staff1])



# meister.setweapon(Hands.right, w_dagger1)
# meister.setweapon(Hands.left, w_axe1)
#
# meister.setcloth(ClothType.chest, c1)
# meister.setcloth(ClothType.legs, c2)
# meister.setcloth(ClothType.hands, c3)
# meister.setcloth(ClothType.feet, c4)
#
#
# jager.setweapon(Hands.right, w_staff1)
#
# jager.setcloth(ClothType.chest, c5)
# jager.setcloth(ClothType.legs, c6)
# jager.setcloth(ClothType.head, c7)
# jager.setcloth(ClothType.feet, c8)


gamemanager = GameManager()
gamemanager.startgame()




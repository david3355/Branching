__author__ = 'Jager'
from equipment import Equipment
from clothtype import ClothType


class Cloth (Equipment):
    def __init__(self, clothtype, name, armor, mana=0):
        super(Cloth, self).__init__(name)
        self.armor = armor
        self.plusmana = mana
        if clothtype is ClothType:
            self.type = clothtype.name
        else:
            self.type = clothtype

    @staticmethod
    def fromJSON(jsonstr):
        obj = Equipment.fromJSON(jsonstr)
        return Cloth(obj["type"], obj["name"],  obj["armor"], obj["plusmana"])

    def __str__(self):
        return "{}({}): Armor({}), Mana({})".format(self.name, self.type, self.armor, self.plusmana)

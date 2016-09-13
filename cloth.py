__author__ = 'Jager'
from equipment import Equipment

class Cloth (Equipment):
    def __init__(self, clothtype, name, armor, mana=0):
        super(Cloth, self).__init__(name)
        self.armor = armor
        self.plusmana = mana
        self.type = clothtype.name

    @staticmethod
    def fromJSON(jsonstr):
        obj = Equipment.fromJSON(jsonstr)
        return Cloth(obj["name"], obj["armor"], obj["plusmana"], obj["type"])

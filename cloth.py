__author__ = 'Jager'
from equipment import Equipment

class Cloth (Equipment):
    def __init__(self, name, armor, mana = 0):
        super(Cloth, self).__init__(name)
        self.armor=armor
        self.plusmana = mana


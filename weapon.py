__author__ = 'Jager'
from equipment import Equipment

class Weapon (Equipment):
    def __init__(self, name, power):
        super(Weapon, self).__init__(name)
        self.power=power

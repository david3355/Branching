__author__ = 'Jager'
from equipment import Equipment


class Weapon (Equipment):
    def __init__(self, name, power):
        super(Weapon, self).__init__(name)
        self.power = power

    @staticmethod
    def fromJSON(jsonstr):
        obj = Equipment.fromJSON(jsonstr)
        return Weapon(obj["name"], obj["power"])

    def __str__(self):
        return "{}: Power({})".format(self.name, self.power)
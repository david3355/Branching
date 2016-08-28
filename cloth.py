__author__ = 'Jager'
from equipment import Equipment

class Cloth (Equipment):
    def __init__(self, name, armor):
        super(Cloth, self).__init__(name)
        self.armor=armor


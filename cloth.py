__author__ = 'Jager'

class Cloth:
    def __init__(self, name, armor):
        self.name=name
        self.armor=armor

    def __eq__(self, other):
        return self.name==other.name
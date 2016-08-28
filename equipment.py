__author__ = 'Jager'

class Equipment:
    def __init__(self, name):
        self.name=name


    def __eq__(self, other):
        return self.name==other.name

    def __str__(self):
        return self.name

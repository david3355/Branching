__author__ = 'Jager'
from char import Character
from hands import Hands
import random

class Warrior (Character):
    def __init__(self, cname, crace, cclass):
        super(Warrior, self).__init__(cname, crace, cclass)
        self.maxrage = 100
        self.rage = self.maxrage

    def special_attack1(self, opponent, hitdamage_callback, specatt_callback):
        self.hit(opponent, hitdamage_callback)
        ragecost = 30
        if(self.isalive() and self.rage >= ragecost):
            wr = self.getweapon(Hands.right)
            wl = self.getweapon(Hands.left)
            pow = wr.power + wl.power
            specatt_callback(self, '[Heroic Strike]')
            damage = random.randint(int(self.power/2), self.power) + pow
            hitdamage_callback(self, damage)
            self.rage -= ragecost
            return opponent.hurt(damage)
        return 0

    def special_attack2(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def heal(self, target):
        pass    # hook method

    def regen_resource(self):
        value = 5
        if(self.rage + value <= self.maxrage): self.rage += value
        else: self.rage = self.maxrage

    def full_resource(self):
        self.rage = self.maxrage

    def __str__(self):
        return super(Warrior, self).__str__() + " RAGE: {}/{}".format(self.maxrage, self.rage)

    def state(self):
        return super(Warrior, self).state() + " RAGE: {}/{}".format(self.maxrage, self.rage)

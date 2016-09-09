__author__ = 'Jager'
from char import Character
import random

class Priest (Character):
    def __init__(self, cname, crace, cclass):
        super(Priest, self).__init__(cname, crace, cclass)
        self.maxmana = 200
        self.mana = self.maxmana

    def special_attack1(self, opponent, hitdamage_callback, specatt_callback):
        manacost = 30
        if(self.isalive() and self.mana >= manacost):
            pow = random.randint(int(self.maxmana * 0.1), int(self.maxmana * 0.3)) + self.mana * 0.3
            specatt_callback(self, '[Mind Blast]')
            damage = random.randint(int(self.power/2), self.power) + pow
            hitdamage_callback(self, damage)
            self.mana -= manacost
            return opponent.hurt(damage)
        return 0

    def special_attack2(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def canheal(self):
        return True;

    def heal(self, target):
        maxmanacost = 30
        if (self.mana >= maxmanacost):
            manacost = maxmanacost
        else:
            manacost = self.mana

        lower_range = manacost-10
        if(lower_range < 0): lower_range = 0
        percent = random.randint(lower_range, manacost)
        plushp = target.maxhp * (percent/100)
        target.regen(plushp)
        self.mana -= manacost
        return plushp

    def regen_resource(self):
        value = 10
        if(self.mana + value <= self.maxmana): self.mana += value
        else: self.mana = self.maxmana

    def full_resource(self):
        self.mana = self.maxmana

    def hasmana(self):
        return True;

    def __str__(self):
        return super(Priest, self).__str__() + " MANA: {}/{}".format(self.maxmana, self.mana)

    def state(self):
        return super(Priest, self).state() + " MANA: {}/{}".format(self.maxmana, self.mana)
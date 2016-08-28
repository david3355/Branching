__author__ = 'Jager'
import random

class Character:
    def __init__(self, cname, crace, cclass):
        self.cname=cname
        self.crace=crace
        self.cclass=cclass
        self.health=100
        self.armor=0
        self.power=10
        self.clothes=[]


    def __str__(self):
        return 'Character > NAME: {}; RACE: {}; CLASS: {};'.format(self.cname, self.crace, self.cclass)


    def addcloth(self, cloth):
        self.clothes.__add__(cloth)
        self.armor += cloth.armor

    def removecloth(self, cloth):
        self.clothes.remove(cloth)
        self.armor -= cloth.armor

    def hit(self, opponent):
        damage = random.randint(self.power/2, self.power)
        opponent.hurt(damage)

    def hurt(self, damage):
        self.health -= damage

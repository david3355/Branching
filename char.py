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
        self.clothes = {'hands': None, 'head':None, 'chest':None, 'legs': None, 'feet': None, 'shoulders': None}
        self.weapons = {'left':None, 'right':None}


    def __str__(self):
        return 'Character > NAME: {}; RACE: {}; CLASS: {};\nHEALTH: {}; ARMOR: {}\nPOWER: {}'.format(self.cname, self.crace, self.cclass, self.health, self.armor, self.power)


    def setcloth(self, type, cloth):
        if(type in self.clothes.keys()):
            self.clothes[type]=cloth
            self.armor += cloth.armor

    def removecloth(self, type):
        if(type in self.clothes.keys()):
            cloth = self.clothes[type]
            self.armor -= cloth.armor
            self.clothes[type] = None

    def hit(self, opponent):
        damage = random.randint(self.power/2, self.power)
        opponent.hurt(damage)

    def hurt(self, damage):
        damage -= self.armor * 0.8
        if(damage < 0): damage = 0
        self.health -= damage

    def setweapon(self, hand, weapon):
        if(hand in self.weapons.keys()):
            self.weapons[hand] = weapon
            self.power += weapon.power

    def removeweapon(self, hand):
        if(hand in self.weapons.keys()):
            weapon = self.weapons[hand]
            self.power -= weapon.power
            self.weapons[hand] = None
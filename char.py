__author__ = 'Jager'
import random
from clothtype import ClothType
from hands import Hands

class Character:
    def __init__(self, cname, crace, cclass):
        self.cname=cname
        self.crace=crace
        self.cclass=cclass
        self.maxhp = 1000
        self.health=self.maxhp
        self.armor=0
        self.power=100
        self.clothes = {ClothType.chest: None, ClothType.head:None, ClothType.hands:None, ClothType.legs: None, ClothType.feet: None, ClothType.shoulders: None}
        self.weapons = {Hands.left: None, Hands.right: None}



    def __str__(self):
        return 'Character > NAME: {}; RACE: {}; CLASS: {}; HEALTH: {}; ARMOR: {}; POWER: {}'.format(self.cname, self.crace, self.cclass, self.health, self.armor, self.power)

    def state(self):
        return 'NAME: {}; HEALTH: {}'.format(self.cname, self.health)

    def isalive(self):
        return self.health > 0


    def setcloth(self, type, cloth):
        if(type in self.clothes.keys()):
            if(self.clothes[type] != None): self.removecloth(type)
            self.clothes[type]=cloth
            self.armor += cloth.armor
            if(self.hasmana()): self.maxmana += cloth.plusmana

    def removecloth(self, type):
        if(type in self.clothes.keys()):
            cloth = self.clothes[type]
            self.armor -= cloth.armor
            self.clothes[type] = None
            if(self.hasmana()): self.maxmana -= cloth.plusmana

    def setweapon(self, hand, weapon):
        if(hand in self.weapons.keys()):
            if(self.weapons[hand] != None): self.removeweapon(hand)
            self.weapons[hand] = weapon
            self.power += weapon.power

    def removeweapon(self, hand):
        if(hand in self.weapons.keys()):
            weapon = self.weapons[hand]
            self.power -= weapon.power
            self.weapons[hand] = None

    def getweapon(self, hand):
        if(hand in self.weapons.keys()):
            return self.weapons[hand];

    def getcloth(self, type):
        if(type in self.clothes.keys()):
            return self.clothes[type];

    def hit(self, opponent, hitdamage_callback):
        if(self.isalive()):
            damage = random.randint(int(self.power/2), self.power)
            hitdamage_callback(self, damage)
            return opponent.hurt(damage)
        return 0

    def hurt(self, damage):
        damage -= self.armor * 0.8
        if(damage < 0): damage = 0
        self.health -= damage
        if(self.health < 0): self.health = 0
        return damage

    def regen(self, health):
        if (self.health + health > self.maxhp): self.health = self.maxhp
        else: self.health += health

    def special_attack1(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def special_attack2(self, opponent, hitdamage_callback, specatt_callback):
        pass    # hook method

    def canheal(self):
        return False;

    def heal(self, target):
        pass    # hook method

    def regen_resource(self):
        pass    # hook method

    def full_resource(self):
        pass    # hook method

    def hasmana(self):
        return False;
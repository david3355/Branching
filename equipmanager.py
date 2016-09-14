__author__ = 'Jager'
from dbhandler.serializer import Serializer
from cloth import Cloth
from weapon import Weapon


class EquipmentManager:
    def __init__(self):
        self.clothes = []
        self.weapons = []
        self.cldbname = "db/clothes.db"
        self.wpdbname = "db/weapons.db"
        self.ser_clothes = Serializer(self.cldbname)
        self.ser_weapons = Serializer(self.wpdbname)
        self.load()

    def load(self):
        self.load_clothes()
        self.load_weapons()

    @staticmethod
    def get_instance():
        if EquipmentManager.instance is None:
            EquipmentManager.instance = EquipmentManager()
        return EquipmentManager.instance

    def load_clothes(self):
        self.clothes = self.ser_clothes.loadobjects(Cloth)

    def load_weapons(self):
        self.weapons = self.ser_weapons.loadobjects(Weapon)

    def get_cloth(self, index):
        if 0 <= index < len(self.clothes):
            return self.clothes[index]

    def get_weapon(self, index):
        if 0 <= index < len(self.weapons):
            return self.weapons[index]
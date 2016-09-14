__author__ = 'Jager'
from enum import Enum

class ClothType (Enum):
    head=1
    shoulders=2
    chest=3
    hands=4
    legs=5
    feet=6

    def fromstring(stringvalue):
        for e in ClothType:
            if e.name == stringvalue:
                return e
        return None



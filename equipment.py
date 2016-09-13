__author__ = 'Jager'
import json

class Equipment:
    def __init__(self, name):
        self.name=name


    def __eq__(self, other):
        return self.name==other.name

    def __str__(self):
        return self.name

    @staticmethod
    def fromJSON(jsonstr):
        'Returns a dict from json string'
        return json.loads(jsonstr)

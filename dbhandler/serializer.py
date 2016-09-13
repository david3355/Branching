__author__ = 'Jager'
from dbhandler.filedb import FileDatabase
import json

class Serializer:
    'Class for serializing and deserializing game objects'
    def __init__(self, dbname):
        self.dbname = dbname
        self.filehandler = FileDatabase(self.dbname)

    def saveobject(self, obj):
        newdata = json.dumps(obj.__dict__)
        self.filehandler.append(newdata)

    def loadobject(self, objectjson, objecttype):
        return objecttype.fromJSON(objectjson)

    def loadobjects(self, objecttype):
        savedobjects = self.filehandler.readall()
        objects = []
        for o in savedobjects:
            objects.append(self.loadobject(o, objecttype))
        return objects
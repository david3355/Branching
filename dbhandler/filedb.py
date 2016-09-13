__author__ = 'Jager'
import os.path as p


class FileDatabase:
    def __init__(self, filename):
        self.filename = filename
        FileDatabase.create_if_notexist(self.filename)

    @staticmethod
    def create_if_notexist(filename):
        if not(p.isfile(filename)):
            open(filename, 'a').close()

    def readall(self):
        file = open(self.filename, 'r', 1)
        lines = file.read().splitlines()
        file.close()
        return lines

    def writeall(self, data):
        file = open(self.filename, 'w', 1)
        file.write(data)
        file.close()

    def append(self, line):
        file = open(self.filename, 'a', 1)
        file.write(line + "\n")
        file.close()



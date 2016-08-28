__author__ = 'Jager'


class Character:
    def __init__(self, cname, crace, cclass):
        self.cname=cname
        self.crace=crace
        self.cclass=cclass


    def __str__(self):
        return 'Character > NAME: {}; RACE: {}; CLASS: {};'.format(self.cname, self.crace, self.cclass)
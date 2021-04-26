from random import randint
#import turtle

#Se cra una clase con las caracteristicas del corredor
class racer(object):
    def __init__(self, color, pos , lane , name):
        self.pos = pos
        self.color = color
        self.lane = lane
        self.name = name

    def move(self):
        r = (randint(1,6))*10
        self.pos = (self.pos[0] + r, self.pos[1])

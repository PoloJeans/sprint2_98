import pygame

class Entity():
    def __init__(self, x, y, prev, next):
        self.x = x
        self.y = y
        self.prev = prev
        self.next = next

    def setPrevNext(self, prev, next):
        self.prev = prev
        self.next = next
    
    def getPos(self):
        return (self.x, self.y)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setPos(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x
        self.y
        
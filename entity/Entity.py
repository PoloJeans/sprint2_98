import pygame

class Entity():
    def __init__(self, x, y, prev, next):
        self.health = 50
        self.x = x
        self.y = y
        self.prev = prev
        self.next = next

    def setPrevNext(self, prev, next):
        self.prev = prev
        self.next = next

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health
    
    def getPos(self):
        return (self.x, self.y)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setPos(self, x, y):
        self.x = x
        self.y = y

    # def draw(self, screen):
    #     pygame.draw.circle(screen, "red", (self.x, self.y), 20)

    # def move(self, board):
    #     pass

    def reset(self):
        self.x
        self.y
        
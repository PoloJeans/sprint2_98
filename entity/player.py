import pygame

class Player():
    def __init__(self, x, y):
        self.health = 50
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(0, 0)

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health
    
    def getPos(self):
        return (self.x, self.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.pos, 20)

    def move(self, board):
        pass

    def reset(self):
        self.health = 50
        self.x
        self.y

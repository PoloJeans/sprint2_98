import pygame
from entity.Entity import Entity

class Sparc(Entity):
    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), 20)

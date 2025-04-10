import pygame
import pygame.image

class HealthBar():
    def __init__(self):
        self.health = 3
        self.healthBar = pygame.Surface((52, 16))
        self.sprite1 = pygame.image.load("./status/assets/heart1.png")
        self.sprite2 = pygame.image.load("./status/assets/heart2.png")
        self.sprite3 = pygame.image.load("./status/assets/heart3.png")
    
    def decHealth(self):
        self.health -= self.health

    def getHealth(self):
        return self.health
    
    def reset(self):
        self.health = 3
    
    def draw(self):
        if self.health == 1:
            self.healthBar.blit(self.sprite1, (0,0))
        elif self.health == 2:
            self.healthBar.blit(self.sprite2, (0,0))
        elif self.health == 3:
            self.healthBar.blit(self.sprite3, (0,0))
        return self.healthBar

        
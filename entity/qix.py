import pygame
import random
from entity.Entity import Entity

class Qix(Entity):
    direction_x = 5
    direction_y = 5
    
    
    #board_w, board_h = top left of green board

    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)
        self.sprite = pygame.image.load("./entity/assets/qix.png")
        self.qixSurface = pygame.Surface((32, 32))
        
    def qix_movement(self, board_mask):
        
        #Qix Mask
        newQix = self.sprite.convert_alpha()
        qix_mask = pygame.mask.from_surface(newQix)
        
        if board_mask.get_at((self.x,self.y)) == 1:
            self.x += self.direction_x+(random.randint(1,2))
            self.y += self.direction_y+(random.randint(1,2))
            
        else:
            if (random.randint(1,2)) == 1:
                self.direction_y *= -1
                self.y += self.direction_y * 3
            else:            
                self.direction_x *= -1
                self.x += self.direction_x * 3
        

    def draw(self, screen):
        self.qixSurface.blit(self.sprite, (0, 0))
        qix_mask = pygame.mask.from_surface(self.qixSurface)
        screen.blit(self.qixSurface, (self.x-20,self.y-20))


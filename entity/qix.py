import pygame
import random
from entity.Entity import Entity

class Qix(Entity):
    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)
            
        
    def qix_movement(self, board_mask):
        movement_direction = 1
        
        #Qix Mask
        newQix = pygame.image.load("red-circle1.png").convert_alpha()
        qix_mask = pygame.mask.from_surface(newQix)
        qix_image = qix_mask.to_surface()
        self.x+=movement_direction
        self.y+=movement_direction
        
        qix_on_board = qix_mask.overlap(board_mask,(self.x-1130,self.y-570))
        if qix_on_board:
            print("On Board")
            
        else:
            print("Off Board")
            movement_direction = movement_direction*-1



    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), 20)
        #Qix Mask
        newQix = pygame.image.load("red-circle1.png").convert_alpha()
        qix_mask = pygame.mask.from_surface(newQix)
        qix_image = qix_mask.to_surface()
        screen.blit(qix_image, (self.x-20,self.y-20))

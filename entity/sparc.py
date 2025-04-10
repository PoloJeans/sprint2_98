import pygame
from entity.Entity import Entity

class Sparc(Entity):
    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (self.x, self.y), 20)

    def sparc_movement(self, board_mask):
        movement_direction = 1
        
        #Sparc Mask
        newSparc = pygame.image.load("red-circle1.png").convert_alpha()
        sparc_mask = pygame.mask.from_surface(newSparc)
        sparc_image = sparc_mask.to_surface()
        self.x+=movement_direction
        self.y+=movement_direction
        
        qix_on_board = sparc_mask.overlap(board_mask,(self.x-1130,self.y-570))
        if qix_on_board:
            print("On Board")
            
        else:
            print("Off Board")
            movement_direction = movement_direction*-1
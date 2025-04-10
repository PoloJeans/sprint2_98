import pygame
import random
from entity.Entity import Entity

class Qix(Entity):
    direction_x = 5
    direction_y = 5
    
    
    def __init__(self, x, y, prev, next):
        super().__init__(x, y, prev, next)
            
        
    def qix_movement(self, board_mask):
        
        #Qix Mask
        newQix = pygame.image.load("red-circle1.png").convert_alpha()
        qix_mask = pygame.mask.from_surface(newQix)
        qix_image = qix_mask.to_surface()
        offset = (int(self.x - 1150), (int(self.y - 600)))
        qix_on_board = qix_mask.overlap(board_mask,offset)
        

        
        if qix_on_board:
            print("On Board")
            self.x += self.direction_x+(random.randint(1,2))
            self.y += self.direction_y+(random.randint(1,2))
        elif (self.y > 620 or self.y < 100):
            print("Off Board")
            self.direction_y *= -1 # Move back further to prevent sticking
            self.y += self.direction_y * 2
        elif (self.x > 1150 or self.x < 100 ):
            print("Off Board")
            self.direction_x *= -1 # Move back further to prevent sticking
            self.x += self.direction_x * 2
            




    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.x, self.y), 20)
        #Qix Mask
        newQix = pygame.image.load("red-circle1.png").convert_alpha()
        qix_mask = pygame.mask.from_surface(newQix)
        qix_image = qix_mask.to_surface()
        
        print(pygame.mouse.get_pos()[0],",", pygame.mouse.get_pos()[1])
        
        screen.blit(qix_image, (self.x-20,self.y-20))


import pygame

class Board():
    #change this to use draw line or something bruh idk
    def __init__(self, width, height, screen):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = screen.get_rect().center
        self.coords = list() 
    
    def setDim(self, width, height, screen):
        self.rect.update(0, 0, width, height)
        self.rect.center = screen.get_rect().center
        
    def getWidth(self):
        return self.rect.width

    def getHeight(self):
        return self.rect.height
    
    def draw(self, screen):
        pygame.draw.Rect(screen, "green", self.rect, 2)

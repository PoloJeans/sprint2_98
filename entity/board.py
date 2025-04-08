import pygame

class Board():
    #change this to use draw line or something bruh idk
    def __init__(self, coords, screen):
        
        self.next = 1
        self.prev = 0
        self.coords = coords
    
    #def setDim(self, width, height, screen):
    #    self.rect.update(0, 0, width, height)
    #    self.rect.center = screen.get_rect().center
        
    #def getWidth(self):
    #    return self.rect.width

    #def getHeight(self):
    #    return self.rect.height
    
    def draw(self, screen):
        pygame.draw.lines(screen, "green", True, self.coords, 2)

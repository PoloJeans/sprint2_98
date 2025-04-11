import pygame

class Board():
    #change this to use draw line or something bruh idk
    def __init__(self, coords, screen):
        
        self.next = 1
        self.prev = 0
        self.coords = coords
        
    def reset(self, screen):
        self.coords = [(100, screen.get_height() - 100), (screen.get_width() - 100, screen.get_height() - 100), (screen.get_width() - 100, 100), (100, 100)]
    
    def draw(self, screen):
        pygame.draw.lines(screen, "green", True, self.coords, 2)

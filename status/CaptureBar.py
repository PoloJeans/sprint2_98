import pygame
import pygame.image

class CaptureBar():
    def __init__(self):
        self.captured = 0
        self.captureBar = pygame.Surface((64,16))
        self.empty = pygame.image.load("./status/assets/captureBarEmpty.png")
        self.quarter = pygame.image.load("./status/assets/captureBarQuarter.png")
        self.half = pygame.image.load("./status/assets/captureBarHalf.png")
        self.threeQuart = pygame.image.load("./status/assets/captureBar3Quarter.png")
        self.full = pygame.image.load("./status/assets/captureBarFull.png")

    def setCaptured(self, value):
        self.captured == value * 100
    
    def getCaptured(self):
        return self.captured
    
    def reset(self):
        self.captured = 0

    def draw(self):
        self.captureBar.fill("black")
        if self.captured == 0:
            self.captureBar.blit(self.empty, (0, 0))
        elif self.captured <= 25:
            self.captureBar.blit(self.quarter, (0, 0))
        elif self.captured <= 50:
            self.captureBar.blit(self.half, (0, 0))
        elif self.captured <= 75:
            self.captureBar.blit(self.threeQuart, (0, 0))
        else:
            self.captureBar.blit(self.full, (0, 0))
        return self.captureBar





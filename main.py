# Example file showing a basic pygame "game loop"
import pygame
from entity.player import *
from entity.board import *
from entity.qix import *
from entity.sparc import *

screen = pygame.display.set_mode((1280, 720))
board = Board(screen.get_height()-100, screen.get_height()-100, screen)
player = Player()

def placecholderentityfunction():
    board.draw(screen)
    player.draw(screen)
    # handles player, qix, and sparc movement on the board, probably branches into collision checking 
    # and incursion

def mqix():
    # pygame setup
    pygame.init()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
               
        #entity management function
        placecholderentityfunction()

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

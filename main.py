# Example file showing a basic pygame "game loop"
import pygame

from entity.Player import *
from entity.board import *
from entity.qix import *
from entity.sparc import *

import pygame.image


screen = pygame.display.set_mode((1280, 720))

#Initialise the board using a list of tuple coordinates (x,y)
board = Board([(100, screen.get_height() - 100), (150, screen.get_height() - 100), (150, screen.get_height() - 300), (300, screen.get_height() - 300), (300, screen.get_height() - 100), (screen.get_width() - 100, screen.get_height() - 100), (screen.get_width() - 100, 100), (100, 100)], screen)
player = Player(110, screen.get_height() - 100, 0, 1)


def placecholderentityfunction():
    board.draw(screen)
    player.draw(screen)
    sparc.draw(screen)
    # handles player, qix, and sparc movement on the board, probably branches into collision checking 
    # and incursion

def mqix():
    # pygame setup
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    push = False
    next = 1
    prev = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        board.draw(screen)
        player.draw(screen)
        length = len(board.coords)
        keys = pygame.key.get_pressed()
        length = len(board.coords)
        
        #Trigger for push
        if keys[pygame.K_SPACE]:
            first = player.getPos()
            push = True
        
        if not push:
          player.edgeMove(board, keys)

        else:
            sparc.draw(screen)
            
             

        
        #entity management function
        

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

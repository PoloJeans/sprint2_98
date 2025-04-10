# Example file showing a basic pygame "game loop"
import pygame

from entity.player import *
from entity.board import *
from entity.qix import *
from entity.sparc import *

import pygame.image


screen = pygame.display.set_mode((1280, 720))

#Initialise the board using a list of tuple coordinates (x,y)
dim = [(100, screen.get_height() - 100), (150, screen.get_height() - 100), (150, screen.get_height() - 300), (300, screen.get_height() - 300), (300, screen.get_height() - 100), (screen.get_width() - 100, screen.get_height() - 100), (screen.get_width() - 100, 100), (100, 100)]
board = Board(dim, screen)
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

    # Player character
    pChar = pygame.image.load("red-circle1.png").convert_alpha()
    #pChar_rect = pChar.get_rect()
    pChar_mask = pygame.mask.from_surface(pChar)
    pChar_maskimg = pChar_mask.to_surface()

    tempBoard = pygame.Surface((1084,524))
    tempBoard.fill("blue")
    board_mask = pygame.mask.from_surface(tempBoard)


    #Run game
    while running:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        #Check mask overlap
        pos = player.getPos()
        pos = (pos[0]-20, pos[1]-20)
        outOfBounds = False
        if pChar_mask.overlap(board_mask, (pos[0]-1130, pos[1]-570)):
            outOfBounds = False
            col = "aliceblue"
        else: 
            col = "blue"
            outOfBounds = True


        #Display Masks
        screen.blit(pChar_maskimg, pos)
        tempBoard.fill(col)
        screen.blit(tempBoard, (100,100))


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
            if not outOfBounds:
                if keys[pygame.K_w]:
                    player.y -= 10
                elif keys[pygame.K_s]:
                    player.y += 10
                elif keys[pygame.K_a]:
                    player.x -= 10
                elif keys[pygame.K_d]:
                    player.x += 10
            # else:
                
            
             

        
        #entity management function
        

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

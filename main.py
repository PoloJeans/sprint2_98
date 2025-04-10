# Example file showing a basic pygame "game loop"
import pygame

from entity.Player import *
from entity.Board import *
from entity.Qix import *
from entity.Sparc import *

import pygame.image


screen = pygame.display.set_mode((640, 720), pygame.SHOWN | pygame.RESIZABLE)

#Initialise the board using a list of tuple coordinates (x,y)
board = Board([(100, screen.get_height() - 100),
            (150, screen.get_height() - 100),
            (150, screen.get_height() - 300),
            (300, screen.get_height() - 300),
            (300, screen.get_height() - 100),
            (screen.get_width() - 100, screen.get_height() - 100),
            (screen.get_width() - 100, 100), (100, 100)], screen)
player = Player(100, (screen.get_height() - 100), 0, 1)


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
    
    left = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("prev:" + str(player.prev) + ", " + str(board.coords[player.prev][0]) + ", " + str(board.coords[player.prev][1]))
                print("next:" + str(player.next) + ", " + str(board.coords[player.next][0]) + ", " + str(board.coords[player.next][1]))
                print("Player Pos: " + str(player.getPos()[0]) + ", " + str(player.getPos()[1]))
        screen.fill("black")

        board.draw(screen)
        player.draw(screen)
        length = len(board.coords)
        keys = pygame.key.get_pressed()
        length = len(board.coords)
        
        #Trigger for push
        
        
        if push == False:
          
          player.edgeMove(board, keys)
          if keys[pygame.K_SPACE]:
            first = player.getPos()
            push = True
            left = False

        else:
            print(push)
            if board.coords[player.prev][0] == player.getPos()[0] == board.coords[player.next][0] and left:
                push = False 
                left = False
            elif board.coords[player.prev][1] == player.getPos()[1] == board.coords[player.next][1] and left:
                push = False
                left = False
            elif keys[pygame.K_w]:
                player.y -= 10
                left = True
            elif keys[pygame.K_s]:
                player.y += 10
                left = True
            elif keys[pygame.K_a]:
                player.x -= 10
                left = True
            elif keys[pygame.K_d]:
                player.x += 10
                left = True
            
            
             

        
        #entity management function
        

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

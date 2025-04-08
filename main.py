# Example file showing a basic pygame "game loop"
import pygame
from entity.player import *
from entity.board import *
from entity.qix import *
from entity.sparc import *

screen = pygame.display.set_mode((1280, 720))
board = Board([(100, screen.get_height() - 100), (screen.get_width() - 100, screen.get_height() - 100),(screen.get_width() - 100, 100),(100, 100)], screen)
player = Player(screen.get_width()/2, screen.get_height() -100)

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
    push = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")

        board.draw(screen)
        player.draw(screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            first = (player.x, player.y)
            push = True
        
        if not push:
            if player.getPos() == board.coords[board.prev]:
                #FINISH THIS PART
                if (player.getPos() == board.coords[board.prev]):
                    if board.coords[board.prev-1][1] < board.coords[board.prev][1]:
                        if keys[pygame.K_w]:
                            player.y -= 10
                            board.prev -= 1
                            board.next -= 1
                    elif board.coords[board.prev - 1][1] > board.coords[board.prev][1]:
                        if keys[pygame.K_s]:
                                player.y += 10
                                board.prev -= 1
                                board.next -= 1
                    elif board.coords[board.prev - 1][0] < board.coords[board.prev][0]:
                        if keys[pygame.K_a]:
                                player.x += 10
                                board.prev -= 1
                                board.next -= 1
                    elif board.coords[board.prev - 1][0] > board.coords[board.prev][0]:
                        if keys[pygame.K_d]:
                                player.x += 10
                                board.prev -= 1
                                board.next -= 1
            if board.coords[board.prev][0] == board.coords[board.next][0]:
                if keys[pygame.K_w]:
                    player.y -= 10
                elif keys[pygame.K_s]:
                    player.y += 10
                    
            elif board.coords[board.prev][1] == board.coords[board.next][1]:
                if keys[pygame.K_a]:
                    player.x -= 10
                elif keys[pygame.K_d]:
                    player.x += 10

                
        
        #entity management function
        

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

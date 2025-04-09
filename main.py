# Example file showing a basic pygame "game loop"
import pygame

from entity.player import *
from entity.board import *
from entity.qix import *
from entity.sparc import *

import pygame.image


screen = pygame.display.set_mode((1280, 720))

board = Board([(100, screen.get_height() - 100), (screen.get_width() - 100, screen.get_height() - 100),(screen.get_width() - 100, 100),(100, 100)], screen)
player = Player(screen.get_width()/2, screen.get_height() -100)
sparc = Sparc(screen.get_width()/2, 100)

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
        if keys[pygame.K_SPACE]:
            first = (player.x, player.y)
            push = True
        
        if not push:
            if player.getPos() == board.coords[prev]:            
                if board.coords[(prev - 1) % length][1] < board.coords[prev][1]:
                    if keys[pygame.K_w]:
                        player.y -= 10
                        prev = (prev - 1) % length
                        next = (next - 1) % length
                elif board.coords[(prev - 1) % length][1] > board.coords[prev][1]:
                    if keys[pygame.K_s]:
                            player.y += 10
                            prev = (prev - 1) % length
                            next = (next - 1) % length
                elif board.coords[(prev - 1) % length][0] < board.coords[prev][0]:
                    if keys[pygame.K_a]:
                            player.x -= 10
                            prev = (prev - 1) % length
                            next = (next - 1) % length
                elif board.coords[(prev - 1) % length][0] > board.coords[prev][0]:
                    if keys[pygame.K_d]:
                            player.x += 10
                            prev = (prev - 1) % length
                            next = (next - 1) % length

            elif player.getPos() == board.coords[next]:
                
                if board.coords[(next +1) % length][1] < board.coords[next][1]:
                    if keys[pygame.K_w]:
                        player.y -= 10
                        prev = (prev + 1) % length
                        next = (next + 1) % length
                elif board.coords[(next +1) % length][1] > board.coords[next][1]:
                    if keys[pygame.K_s]:
                            player.y += 10
                            prev = (prev + 1) % length
                            next = (next + 1) % 1
                elif board.coords[(next +1) % length][0] < board.coords[next][0]:
                    if keys[pygame.K_a]:
                            player.x -= 10
                            prev = (prev + 1) % length
                            next = (next + 1) % length
                elif board.coords[(next +1) % length][0] > board.coords[next][0]:
                    if keys[pygame.K_d]:
                            player.x += 10
                            prev = (prev + 1) % length
                            next = (next + 1) % length


            elif board.coords[prev][0] == board.coords[next][0] and ((player.y > board.coords[prev][1] and player.y < board.coords[next][1]) or (player.y < board.coords[prev][1] and player.y > board.coords[next][1])):
                if keys[pygame.K_w]:
                    player.y -= 10
                elif keys[pygame.K_s]:
                    player.y += 10
                    
            elif board.coords[prev][1] == board.coords[next][1] and ((player.x > board.coords[prev][0] and player.x < board.coords[next][0]) or (player.x < board.coords[prev][0] and player.x > board.coords[next][0])):
                if keys[pygame.K_a]:
                    player.x -= 10
                elif keys[pygame.K_d]:
                    player.x += 10

        else:
            sparc.draw(screen)
            
             

        
        #entity management function
        

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

mqix()

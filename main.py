# Example file showing a basic pygame "game loop"
import pygame


from entity.Entity import *
from entity.Player import *
from entity.Board import *
from entity.Qix import *
from entity.Sparc import *

from status.HealthBar import *
from status.CaptureBar import *

import pygame.image


screen = pygame.display.set_mode((1280, 720), pygame.SHOWN | pygame.RESIZABLE)

#Initialise the board using a list of tuple coordinates (x,y)
board = Board([(100, screen.get_height() - 100),
            (150, screen.get_height() - 100),
            (150, screen.get_height() - 300),
            (300, screen.get_height() - 300),
            (300, screen.get_height() - 100),
            (screen.get_width() - 100, screen.get_height() - 100),
            (screen.get_width() - 100, 100), (100, 100)], screen)
hBar = HealthBar()
cBar = CaptureBar()
player = Player(100, (screen.get_height() - 100), 0, 1)
qix = Qix(screen.get_width() / 2, screen.get_height() / 2, 0, 1)
sparc = Sparc(screen.get_width() / 2, screen.get_height() - 620, 0, 1)


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

    # Player character
    pChar = pygame.image.load("red-circle1.png").convert_alpha()
    #pChar_rect = pChar.get_rect()
    pChar_mask = pygame.mask.from_surface(pChar)
    pChar_maskimg = pChar_mask.to_surface()

    tempBoard = pygame.Surface((1084,524))
    tempBoard.fill("blue")
    board_mask = pygame.mask.from_surface(tempBoard)

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
                print("prev:" + str(player.prev) + ", " + str(board.coords[player.prev][0]) + ", " + str(board.coords[player.prev][1]))
                print("next:" + str(player.next) + ", " + str(board.coords[player.next][0]) + ", " + str(board.coords[player.next][1]))
                print("Player Pos: " + str(player.getPos()[0]) + ", " + str(player.getPos()[1]))
        screen.fill("black")

        screen.blit(pygame.transform.scale_by(hBar.draw(), 2), (10, 10))
        screen.blit(pygame.transform.scale_by(cBar.draw(), 2), (screen.get_width() - 142, 10))

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


        screen.blit(pygame.transform.scale_by(hBar.draw(), 2), (10, 10))
        screen.blit(pygame.transform.scale_by(cBar.draw(), 2), (screen.get_width() - 142, 10))

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


        # Draw out all entities
        board.draw(screen)
        player.draw(screen)
        qix.draw(screen)
        sparc.draw(screen)

        length = len(board.coords)
        keys = pygame.key.get_pressed()
        length = len(board.coords)
        
        # Collision checker
        if player.collision(sparc, qix):


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

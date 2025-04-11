# Example file showing a basic pygame "game loop"
import pygame
import copy
import sys

from entity.Entity import *
from entity.player import *
from entity.Board import *
from entity.qix import *
from entity.sparc import *

from status.HealthBar import *
from status.CaptureBar import *
from menu.Button import *
import pygame.image


screen = pygame.display.set_mode((1280, 720), pygame.SHOWN | pygame.RESIZABLE)
botleft = (100, screen.get_height() - 100)
botright = (screen.get_width() - 100, screen.get_height() - 100)
topright = (screen.get_width() - 100, 100)
topleft = (100, 100)
#Initialise the board using a list of tuple coordinates (x,y)
board = Board([(100, screen.get_height() - 100),
            (screen.get_width() - 100, screen.get_height() - 100),
            (screen.get_width() - 100, 100), 
            (100, 100)], screen)
hBar = HealthBar()
cBar = CaptureBar()
player = Player(100, (screen.get_height() - 100), 0, 1)
qix = Qix(screen.get_width() / 2, screen.get_height() / 2, 0, 1)

# next and prev value for sparc is currently hardcoded to the board with an incursion already present
sparc = Sparc(screen.get_width() / 2, screen.get_height() - 620, 2, 3)


def placecholderentityfunction():
    board.draw(screen)
    player.draw(screen)
    sparc.draw(screen)
    # handles player, qix, and sparc movement on the board, probably branches into collision checking 
    # and incursion
def updateBoundary(coords, mask):
    for i in range(coords[0][0] + 1, coords[3][0]):
        for j in range(coords[0][1]+1, coords[1][1]):
            mask.set_at((i,j), 0)

def getFont(size):
    return pygame.font.Font("./menu/assets/font.ttf", size)

def getCapturedArea(boardMask, area):
    #Given a board mask & its area, 
    #return the % of captured bits as a float from 0-1
    capturedArea = area - boardMask.count()
    return round((capturedArea/area),2)
    

def main_menu():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Menu")
    pygame.mixer.music.load("toby fox - UNDERTALE Soundtrack - 01 Once Upon a Time.mp3")
    pygame.mixer.music.play(100,0,0)

    bg = pygame.image.load("./menu/assets/menubg.png")
    while True:
        screen.blit(bg, (0,0))
        mousePos = pygame.mouse.get_pos()

        menuText = getFont(70).render("mQix", True, "white")
        menuRect = menuText.get_rect(center=(screen.get_width()/2, 150))

        playButton = Button(pygame.image.load("./menu/assets/button.png").convert_alpha(), (1000,400), "PLAY", getFont(45))
        quitButton = Button(pygame.image.load("./menu/assets/button.png").convert_alpha(), (1000,550), "QUIT", getFont(45))

        screen.blit(menuText, menuRect)

        for button in [playButton,quitButton]:
            button.changeColour(mousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkInput(mousePos):
                    mqix()
                if quitButton.checkInput(mousePos):
                    pygame.quit()
                    break

        pygame.display.update()
        
def game_over_screen():
    pygame.init()
    pygame.font.init()
    pygame.mixer.music.load("Undertale Game Over Theme.mp3")
    pygame.mixer.music.play(100,0,0)
    
    while True:
        screen.fill("black")
        mousePos = pygame.mouse.get_pos()
        
        menuText = getFont(70).render("Game Over", True, "red")
        menuRect = menuText.get_rect(center=(screen.get_width()/2, 150))
        
        playButton = Button(pygame.image.load("./menu/assets/button.png").convert_alpha(), (620,400), "PLAY AGAIN", getFont(28))
        quitButton = Button(pygame.image.load("./menu/assets/button.png").convert_alpha(), (620,550), "QUIT", getFont(45))
        
        screen.blit(menuText, menuRect)
    
        for button in [playButton,quitButton]:
            button.changeColour(mousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkInput(mousePos):
                    mqix()
                if quitButton.checkInput(mousePos):
                    pygame.quit()
                    break
                
        pygame.display.update()
                
def mqix():
    # pygame setup
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    push = False
    left = False
    pygame.mixer.music.load("246940-9197049f-e352-4a71-bdea-9303e664c54d.mp3")
    pygame.mixer.music.play(100,0,0)
    
    boardMask = pygame.mask.Mask((screen.get_width(), screen.get_height()))
    for i in range (topleft[0], topright[0] + 1):
        for j in range(topleft[1], botleft[1]+1):
            boardMask.set_at((i,j), 1)
            
    boardMaskArea = boardMask.count() # Number of 1 bits in mask (USE FOR getCapturedArea() )

    # Player character
    pChar = pygame.image.load("red-circle1.png").convert_alpha()
    #pChar_rect = pChar.get_rect()
    pChar_mask = pygame.mask.from_surface(pChar)
    pChar_maskimg = pChar_mask.to_surface()
    

    #Check mask overlap
    pos = player.getPos()
    pos = (pos[0]-20, pos[1]-20)


    #Display Masks
    screen.blit(pChar_maskimg, pos)


    # Player character
    pChar = pygame.image.load("red-circle1.png").convert_alpha()
    pChar_mask = pygame.mask.from_surface(pChar)
    pChar_maskimg = pChar_mask.to_surface()


    #Run game
    while running:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                running = False
                print("prev:" + str(player.prev) + ", " + str(board.coords[player.prev][0]) + ", " + str(board.coords[player.prev][1]))
                print("next:" + str(player.next) + ", " + str(board.coords[player.next][0]) + ", " + str(board.coords[player.next][1]))
                print("Player Pos: " + str(player.getPos()[0]) + ", " + str(player.getPos()[1]))
                print(board.coords)
                print(pushCoords)
        screen.fill("black")
        
        if (hBar.getHealth() <= 0):
            #Reset Game Variables
            running = False
            push = False
            left = False
            cBar.reset()
            hBar.reset()
            player.setPrevNext(0,1)
            sparc.setPrevNext(0,1)
            board.reset(screen)
            
            pygame.mixer.music.stop()
            game_over_screen()
        
            

        # screen.blit(hBar.draw(), (10, 10))
        screen.blit(pygame.transform.scale_by(hBar.draw(), 2), (10, 10))
        screen.blit(pygame.transform.scale_by(cBar.draw(), 2), (screen.get_width() - 142, 10))

        #Check mask overlap
        pos = player.getPos()
        pos = (pos[0]-20, pos[1]-20)

        #Display Masks
        screen.blit(pChar_maskimg, pos)

        #Check mask overlap
        pos = player.getPos()
        pos = (pos[0]-20, pos[1]-20)
        outOfBounds = False
        if pChar_mask.overlap(boardMask, (pos[0]-1130, pos[1]-570)):
            outOfBounds = False
            col = "aliceblue"
        else: 
            col = "blue"
            outOfBounds = True


        #Display Masks
        screen.blit(pChar_maskimg, pos)


        # Draw out all entities
        board.draw(screen)
        player.draw(screen)
        qix.draw(screen)
        qix.qix_movement(boardMask)
        sparc.draw(screen)
        sparc.sparc_movement(boardMask)
        
        keys = pygame.key.get_pressed()
        
        # Collision checker
        if player.collision(sparc, qix, push) :
            hBar.decHealth()
            pushCoords =[]
            push  = False
            if hBar.getHealth() == 0:
                # trigger game over
                pass
            player.setPos(100, (screen.get_height() - 100)) #Bottom left corner
            player.setPrevNext(0, 1)
            #sparc.setPrevNext(2,3)
            qix.setPos(screen.get_width() / 2, screen.get_height() / 2)
            #sparc.setPos(screen.get_width() - 100, screen.get_height() - 620)


        #getUpdatedArea(boardMask, boardMaskArea)

        sparc.edgeMove(board)
        #Trigger for push
        if push == False:
          
          player.edgeMove(board, keys)
          if keys[pygame.K_SPACE]:
            pushCoords = []
            lastkey = -1
            push = True
            left = False

        else:
            
            pos = player.getPos()
            current  = copy.deepcopy(pushCoords)
            current.append(pos)
            current.append(pos)

            
            pygame.draw.lines(screen, "green", False, current, 2)
            
            if board.coords[player.prev][0] == player.getPos()[0] == board.coords[player.next][0] and left:
                push = False 
                left = False
                pushCoords.append(player.getPos())
                if len(pushCoords) != 4 or pushCoords[3] == board.coords[player.next] or pushCoords[3] == board.coords[player.prev] or pushCoords[0] == board.coords[player.prev] or pushCoords[0] == board.coords[player.prev]:
                    player.setPos(pushCoords[0][0], pushCoords[0][1])
                    pushCoords = []
                else:
                
                    
                    if boardMask.get_at((player.getPos()[0]-1, player.getPos()[1])) == 1:
                        if (pushCoords[0][1] < pushCoords[3][1]):
                            pushCoords.reverse()
                            board.coords.insert(player.prev+1, pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[0])
                            player.next = (player.prev + 1 ) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                            
                        else:
                            board.coords.insert((player.prev + 1), pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])

                            
                            player.prev = board.coords.index(pushCoords[3])
                            player.next = (player.prev + 1) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                    else:
                        if (pushCoords[0][1] < pushCoords[3][1]):
                            board.coords.insert((player.prev + 1), pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[3])
                            player.next = (player.prev + 1) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                            
                        else:
                            pushCoords.reverse()
                            board.coords.insert(player.prev+1, pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[0])
                            player.next = (player.prev + 1 ) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                


            elif board.coords[player.prev][1] == player.getPos()[1] == board.coords[player.next][1] and left:
                push = False
                left = False
                pushCoords.append(player.getPos())
                if len(pushCoords) != 4 or pushCoords[3] == board.coords[player.next] or pushCoords[3] == board.coords[player.prev] or pushCoords[0] == board.coords[player.prev] or pushCoords[0] == board.coords[player.prev]:
                    player.setPos(pushCoords[0][0], pushCoords[0][1])
                    pushCoords = []
                else:
                    
                    if boardMask.get_at((player.getPos()[0], player.getPos()[1]-1)) == 1:
                        if (pushCoords[0][0] > pushCoords[3][0]):
                            pushCoords.reverse()
                            board.coords.insert(player.prev+1, pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[0])
                            player.next = (player.prev + 1 ) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                            
                        else:
                            board.coords.insert((player.prev + 1), pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[3])
                            player.next = (player.prev + 1) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                    else:
                        if (pushCoords[0][0] < pushCoords[3][0]):
                            pushCoords.reverse()
                            board.coords.insert(player.prev+1, pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[0])
                            player.next = (player.prev + 1 ) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                        else:
                            board.coords.insert((player.prev + 1), pushCoords[0])
                            board.coords.insert((player.prev + 2), pushCoords[1])
                            board.coords.insert((player.prev + 3) , pushCoords[2])
                            board.coords.insert((player.prev + 4), pushCoords[3])
                            player.prev = board.coords.index(pushCoords[3])
                            player.next = (player.prev + 1) % len(board.coords)
                            pushCoords.sort()
                            updateBoundary(pushCoords, boardMask)
                            sparc.setPos(board.coords[sparc.prev][0], board.coords[sparc.prev][1])
                        

            elif keys[pygame.K_w]:
                if boardMask.get_at((pos[0], pos[1] - 10 )) == 1:
                    if lastkey != 0:
                        
                        pushCoords.append(player.getPos())
                    lastkey = 0
                    player.y -= 10
                    left = True
            elif keys[pygame.K_s]:
                if boardMask.get_at((pos[0], pos[1] + 10 )) == 1:
                    if lastkey != 1:
                        
                        pushCoords.append(player.getPos())
                    lastkey = 1
                    player.y += 10
                    left = True
            elif keys[pygame.K_a]:
                if boardMask.get_at((pos[0] -10 , pos[1])) == 1:
                    if lastkey != 2:
                        
                        pushCoords.append(player.getPos())
                    lastkey = 2
                    player.x -= 10
                    left = True
            elif keys[pygame.K_d]:
                if boardMask.get_at((pos[0] + 10 , pos[1])) == 1:
                    if lastkey != 3:
                        
                        pushCoords.append(player.getPos())
                    lastkey = 3
                    
                    player.x += 10
                    left = True
            

             

        
        #entity management function
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(120) # limits FPS to 120

    pygame.quit()

main_menu()
# Example file showing a basic pygame "game loop"
import pygame
import pygame.image

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
#Visual Initialization
sWidth = screen.get_width()
sHeight = screen.get_height()
boardWidth = sWidth-100
boardHeight = sHeight-100
board = pygame.Rect(0, 0, boardWidth, boardHeight)
board.center = screen.get_rect().center
img = pygame.image.load("IMG_1343.WEBP")
pygame.mixer.music.load("246940-9197049f-e352-4a71-bdea-9303e664c54d.mp3")
pygame.mixer.music.play(100,0,0)


#Variable Setup
dt = 0.01
hp = 3
leftBound = board.centerx - boardWidth/2
rightBound = board.centerx + boardWidth/2
topBound = board.centery - boardHeight/2
botBound = board.centery + boardHeight/2
player_pos = pygame.Vector2(board.centerx, botBound )

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(pygame.transform.scale(img, (300,394)), (screen.get_rect().centerx - pygame.transform.scale(img, (300,394)).get_rect().centerx, screen.get_rect().centery/2 -  pygame.transform.scale(img, (300,394)).get_rect().centery/2))
    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "green", board, 2)
    pygame.draw.circle(screen, "red", player_pos, 20)
    

    keys = pygame.key.get_pressed()
    if (topBound < player_pos.y) and (player_pos.x==leftBound or player_pos.x== rightBound):
        if keys[pygame.K_w]:
            player_pos.y -= 10
    if (player_pos.y < botBound) and (player_pos.x==leftBound or player_pos.x== rightBound):
        if keys[pygame.K_s]:
            player_pos.y += 10
    if (leftBound < player_pos.x) and (player_pos.y==topBound or player_pos.y== botBound):
        if keys[pygame.K_a]:
            player_pos.x -= 10
    if (player_pos.x < rightBound and (player_pos.y==topBound or player_pos.y== botBound)):
        if keys[pygame.K_d]:
            player_pos.x += 10
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()
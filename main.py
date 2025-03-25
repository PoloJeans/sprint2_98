# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()
#Visual Initialization
sWidth = screen.get_width()
sHeight = screen.get_height()
boardWidth = sHeight-100
boardHeight = sHeight-100
board = pygame.Rect(0, 0, boardWidth, boardHeight)
board.center = screen.get_rect().center

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

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "green", board, 2)
    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()
    if (topBound < player_pos.y) and (player_pos.x==leftBound or player_pos.x== rightBound):
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
    if (player_pos.y < botBound) and (player_pos.x==leftBound or player_pos.x== rightBound):
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
    if (leftBound < player_pos.x) and (player_pos.y==topBound or player_pos.y== botBound):
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
    if (player_pos.x < rightBound and (player_pos.y==topBound or player_pos.y== botBound)):
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()

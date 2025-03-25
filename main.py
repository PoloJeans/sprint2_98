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
board = pygame.Rect(0, 0, sHeight-100, sHeight-100)
board.center = screen.get_rect().center
#Variable Setup
dt = 0.01
hp = 3

player_pos = pygame.Vector2(sWidth/2, sHeight/2)

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
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    elif keys[pygame.K_s]:
        player_pos.y += 300 * dt
    elif keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    elif keys[pygame.K_d]:
        player_pos.x += 300 * dt
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()

# Import libraries
import pygame
import sys


# Pygame initiate
pygame.init()

# It controlled speed of the game
CLOCK = pygame.time.Clock()

# Game screen size
SCREEN = pygame.display.set_mode((800,800))

# Game Caption
pygame.display.set_caption("Jumping mario")


# Jumping variable
jumping = False

# Mario's middle position
X_POSITION, Y_POSITION = 400, 660

# Velocity for Movement
X_VELOCITY, Y_VELOCITY = 5, 5

# Gravity && Jump_Height && Velocity
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT


# Images load and size defined
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("images/mario_standing.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("images/mario_jumping.png"), (48, 64))
BACKGROUND = pygame.image.load("images/background.png")


# Starting The game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # key pressed
    keys_pressed = pygame.key.get_pressed()

    # Movement logic
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        X_POSITION = min(X_POSITION + X_VELOCITY, SCREEN.get_width() - STANDING_SURFACE.get_width() / 2)
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        X_POSITION = max(X_POSITION - X_VELOCITY, STANDING_SURFACE.get_width() / 2)
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w] or keys_pressed[pygame.K_SPACE]:
        jumping = True
    
    # Boundary checking for Y_POSITION
    Y_POSITION = max(Y_POSITION, STANDING_SURFACE.get_height() / 2)
    Y_POSITION = min(Y_POSITION, SCREEN.get_height() - STANDING_SURFACE.get_height() / 2)
    

    # Background picture set
    SCREEN.blit(BACKGROUND, (0,0))

    # Jumping logic
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        # Rectangle around of Mario
        mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
    else:
        # Rectangle around of Mario
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)


    # pygame display updated
    pygame.display.update()

    # Clock tick setup
    CLOCK.tick(60)
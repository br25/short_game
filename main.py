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


    SCREEN.blit(BACKGROUND, (0,0))

    # pygame display updated
    pygame.display.update()
    
    # Clock tick setup
    CLOCK.tick(60)
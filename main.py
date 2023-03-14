


import pygame

pygame.init()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set up the drawing window
screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])

print(gameWindowWidth, gameWindowHeight)



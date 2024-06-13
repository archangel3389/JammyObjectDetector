import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Set up the colors
purple = (128, 0, 128)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the background with purple
    window.fill(purple)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
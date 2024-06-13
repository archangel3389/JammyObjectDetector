import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jammy Object Detector")



class Player():
    def __init__(self, name, health, x, y):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        
    def draw(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


player1 = Player("Thomas", 199, 100, 100)
# Set up the colors
purple = (128, 0, 128)

# Game loop
running = True
while running:
    # Handle events
    player1.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                player1.x -= 10
                
            if event.key == K_RIGHT:
                player1.x += 10
                
            if event.key == K_UP:
                player1.y -= 10
                
            if event.key == K_DOWN:
                player1.y += 10
                
            
    # Fill the background with purple
    window.fill(purple)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
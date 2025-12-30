import sys
import pygame
from star_func import *



# Initialize Pygame Elements
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("AD ASTRA PER ASPERA")
stars = pygame.sprite.Group()

many_stars(screen, stars)
# Run Game
while True:
    # Check for user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Update star positions
    update_stars(screen, stars)
            

    screen.fill((255,255,255)) # Set background color
    stars.draw(screen)

    pygame.display.flip() # Display drawn screen
            
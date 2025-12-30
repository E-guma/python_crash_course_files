import sys
import pygame
from star_func2 import *



# Initialize Pygame Elements
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("AD ASTRA PER ASPERA")
clock = pygame.time.Clock()
stars = pygame.sprite.Group()
star = Star(screen, stars)
stars.add(star)


# many_stars(screen, stars)
# Run Game
while True:
    # Check for user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Update star positions
    stars.update()
    screen.fill((255,255,255)) # Set background color
    stars.draw(screen)
    
    pygame.display.flip() # Display drawn screen
    clock.tick(144)  # Set frame rate to 60 fps
            
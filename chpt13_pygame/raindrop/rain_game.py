import pygame
import rain_drop as rd
from settings import Settings

# Initialize game elements
pygame.init()
settings = Settings()
screen = pygame.display.set_mode(settings.screen_size)
pygame.display.set_caption(settings.caption)
clock = pygame.time.Clock()

# Group of raindrops
drops = pygame.sprite.Group()
# Create a row of raindrops
rd.create_row_drops(settings, screen, drops)


while True:
    rd.check_events()
    rd.update_drops(settings, screen, drops)
    rd.update_screen(settings, screen, drops)            
    clock.tick(120)
    
    
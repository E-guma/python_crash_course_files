import pygame
import functions as f
from settings import Settings
from ball_basket import Basket

pygame.init()
settings = Settings()
screen = pygame.display.set_mode(settings.screen_size)
pygame.display.set_caption(settings.caption)
clock = pygame.time.Clock()
# Create Basket and Ball groups
baskets = pygame.sprite.Group()
balls = pygame.sprite.Group()

# Create basket and add it to group
basket = Basket(settings, screen)
baskets.add(basket)

# Game Loop
while True:
    f.check_events(basket)
    baskets.update()
    f.update_ball(settings, screen, baskets, balls)
    f.update_screen(settings, screen, baskets, balls)
    clock.tick(60)

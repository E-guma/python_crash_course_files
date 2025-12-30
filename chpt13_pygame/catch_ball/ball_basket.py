from random import randint
import pygame

class Ball(pygame.sprite.Sprite):
    """Create a ball game object"""
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/ball.png').convert_alpha()
        self.rect = self.image.get_frect()
        self.rect.bottom = self.screen_rect.top
        self.rect.right = randint(int(self.rect.width), self.screen_rect.width)

    def update(self):
        """Update ball's position"""
        self.rect.y += self.settings.ball_speed
        if self.rect.top > self.screen_rect.height:
            self.kill()


class Basket(pygame.sprite.Sprite):
    """Create a basket game object"""
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/basket.png').convert_alpha()
        self.rect = self.image.get_frect()
        self.rect.bottom = self.screen_rect.bottom - 5
        self.rect.centerx = self.screen_rect.centerx
        # Movement flags
        self.move_right = False
        self.move_left = False
        
    def update(self):
        """Update basket's position"""
        if self.move_right:
            # Move Right
            self.rect.centerx += self.settings.basket_speed
        if self.move_left:
            # Move Left
            self.rect.centerx -= self.settings.basket_speed
        self.rect.clamp_ip(self.screen_rect)

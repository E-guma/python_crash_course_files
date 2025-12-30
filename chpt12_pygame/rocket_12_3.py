import sys
import pygame
from show_image_12_1 import get_image

class Rocket(get_image):
    def __init__(self, screen, image_path):
        super().__init__(screen, image_path)
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.rocket_speed = 1
        
    def update(self, rect):
        if self.move_right:
            rect.centerx += self.rocket_speed
        if self.move_left:
            rect.centerx -= self.rocket_speed
        if self.move_up:
            rect.centery -= self.rocket_speed
        if self.move_down:
            rect.centery += self.rocket_speed
        rect.clamp_ip(self.screen.get_rect())
        

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('ROCKET')
rocket = Rocket(screen, 'images/rocket.png')
scaled_rkt = rocket.scale(0.1)
scaled_rkt_rect = scaled_rkt.get_rect()
scaled_rkt_rect.center = screen.get_rect().center

bg_color = 255, 255, 255
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.move_right = True
            elif event.key == pygame.K_LEFT:
                rocket.move_left = True
            elif event.key == pygame.K_UP:
                rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                rocket.move_down = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.move_right = False
            elif event.key == pygame.K_LEFT:
                rocket.move_left = False
            elif event.key == pygame.K_UP:
                rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                rocket.move_down = False
            
    screen.fill(bg_color)
    rocket.update(scaled_rkt_rect)
    rocket.blitme(scaled_rkt, scaled_rkt_rect)
    pygame.display.flip()

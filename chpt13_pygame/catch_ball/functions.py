import sys
import pygame
from ball_basket import Ball


def check_events(basket):
    """Respond to user triggered events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close game
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                    basket.move_right = True
            elif event.key == pygame.K_LEFT:
                    basket.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                    basket.move_right = False
            elif event.key == pygame.K_LEFT:
                    basket.move_left = False
            
            
def update_screen(settings, screen, baskets, balls):
    """Update game elements on screen"""
    screen.fill(settings.bgcolor)
    balls.draw(screen)
    baskets.draw(screen)
    # Draw new screen
    pygame.display.flip()
    
def create_ball(settings, screen, balls):
    """Create a single ball object and add it to group"""
    ball = Ball(settings, screen)
    balls.add(ball)    

def update_ball(settings, screen, baskets, balls):
    """Update Ball elements"""
    balls.update()
    # Check ball basket collision
    collisions = pygame.sprite.groupcollide(balls, baskets, True, False)
    
    if len(balls) == 0:
        # Create a new ball
        create_ball(settings, screen, balls)



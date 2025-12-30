import sys
from random import randint
import pygame

class Raindrop(pygame.sprite.Sprite):
    """Creating a raindrop game object"""
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/raindrop.png').convert_alpha()
        self.rect = self.image.get_frect()
        self.rect.x, self.rect.y = 0, -self.rect.height
        self.make_new_row = True
        self.offset_limit = int(0.1 * self.settings.drop_speed * 10)
        self.speed_offset = randint(-self.offset_limit, self.offset_limit)/10
        
    def update(self):
        """Update drop's position"""
        self.rect.y += self.settings.drop_speed + self.speed_offset
        if self.rect.top > self.screen.get_height():
            self.kill()    
        

def check_events():
    """Check for user triggered events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, drops):
    """Continuously update game elements on screen"""
    screen.fill(settings.bgcolor)
    # Draw drops
    drops.draw(screen)
    
    # Redraw screen
    pygame.display.flip()
    
def update_drops(settings, screen, drops):
    """Update raindrop elements"""
    for drop in drops.sprites():
        if drop.make_new_row and drop.rect.top > screen.get_height()/4:
            for drop in drops.sprites():
                drop.make_new_row = False
            create_row_drops(settings, screen, drops)
            break
        
    drops.update()
     
def create_drop(settings, screen, drops, x):
        """Create a raindrop, set its x position and add it to group"""
        rain_drop = Raindrop(settings, screen)
        rain_drop.rect.right = x
        drops.add(rain_drop)
    
        
def create_row_drops(settings, screen, drops):
    """Create a row of raindrops"""        
    drop = Raindrop(settings, screen)
    drop_right = 30 + drop.rect.width
    while drop_right <= screen.get_width() - 30:
        create_drop(settings, screen, drops, drop_right)
        # Set next drop position
        drop_right += 30 + drop.rect.width
    
    
    
    
    
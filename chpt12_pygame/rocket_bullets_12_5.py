import sys
import pygame

Image_Path = 'images/cartoon1.png'

class Rocket:
    """Load an image into memory and position it"""
    
    def __init__(self,screen, image_path):
        """initialize image atrributes"""
        self.image = pygame.image.load(image_path).convert_alpha()
        self.screen = screen
        self.rect = self.image.get_frect()
        self.screen_rect = screen.get_frect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Movement Flags
        self.move_up = False
        self.move_down = False
        self.speed = 0.5
        
    def blitme(self, img = None, rect = None):
        if img:
            self.screen.blit(img, rect)
        else:
            self.screen.blit(self.image,self.rect)
        
    def scale(self, factor):
        """Returns the scaled version of an image"""
        new_width = int(self.image.get_width()*factor)
        new_height = int(self.image.get_height()*factor)
        new_dim = (new_width,new_height)
        return pygame.transform.scale(self.image, new_dim)

    def update(self):
        if self.move_up:
            self.rect.centery -= self.speed
        if self.move_down:
            self.rect.centery += self.speed
        self.rect.clamp_ip(self.screen_rect)

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the rocket."""
    
    def __init__(self, screen, rocket):
        """Create a bullet object at the rocket's current position."""
        super().__init__()
        self.screen = screen
        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.FRect((0, 0), (15, 5))
        self.rect.centery = rocket.rect.centery + 15
        self.rect.right = rocket.rect.right
        self.color = (255,0,0)
        self.speed = 1
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the position of the bullet.
        self.rect.x += self.speed
        if self.rect.right > self.screen.get_rect().right:
            self.kill()

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('ROCKET WITH BULLETS')
rocket = Rocket(screen, Image_Path)
bullets = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                rocket.move_down = True
            elif event.key == pygame.K_SPACE:
                # Fire a bullet
                new_bullet = Bullet(screen, rocket)
                bullets.add(new_bullet)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                rocket.move_down = False        
                
    bg_color = (0, 55, 55)
    screen.fill(bg_color)
    rocket.update()
    bullets.update()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    pygame.display.flip()

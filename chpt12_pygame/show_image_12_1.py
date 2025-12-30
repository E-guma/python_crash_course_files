import sys
import pygame


class get_image:
    """Load an image into memory and position it"""
    
    def __init__(self,screen, image_path):
        """initialize image atrributes"""
        self.image = pygame.image.load(image_path).convert_alpha()
        self.screen = screen
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.image_rect.center = self.screen_rect.center
        
    def blitme(self, img = None, rect = None):
        if img:
            self.screen.blit(img, rect)
        else:
            self.screen.blit(self.image,self.image_rect)
        
    def scale(self,factor):
        """Returns the scaled version of an image"""
        new_width = int(self.image.get_width()*factor)
        new_height = int(self.image.get_height()*factor)
        new_dim = (new_width,new_height)
        return pygame.transform.scale(self.image, new_dim)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption('GAME DEV')
    image = get_image(screen, 'images/pix.png')
    scaled_img = image.scale(0.4)
    scaled_img_rect = scaled_img.get_rect()
    scaled_img_rect.center = screen.get_rect().center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        bg_color = (0, 0, 255)
        screen.fill(bg_color)
        image.blitme(scaled_img, scaled_img_rect)
        
        pygame.display.flip()

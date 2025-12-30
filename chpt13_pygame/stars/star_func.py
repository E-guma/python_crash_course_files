from random import randint
import pygame


class Star(pygame.sprite.Sprite):
    """Create a star game element"""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_frect()
        self.rect.topleft = (-self.rect.width,30)
        self.direction = 1

    def update(self):
        """Update star position"""
        self.rect.x += 1 * self.direction
        if self.rect.top > self.screen.get_height():
            self.kill()


def update_stars(screen, stars):
    for star in stars:
        if (star.direction == 1) and (star.rect.right > screen.get_width() - 40):
            for item in stars:
                item.rect.y += (30 )
                item.direction *= -1
        elif (star.direction == -1) and (star.rect.left < 40):
            for item in stars:
                item.rect.y += (30 )
                item.direction *= -1
    stars.update()
    
    
def stars_on_a_row(screen, star):
    """Returns the number of stars that fit on a row"""
    row_space = screen.get_width() - (2*30)
    row_stars = int(row_space / (star.rect.width + 30))
    return row_stars

def number_of_rows(screen, star):
    """Returns the number of star rows that fit on the screen"""
    space = screen.get_height() - (30)
    row_number = int(space / (star.rect.height + 30))
    return row_number

def create_star(screen, stars, star_number, row):
    """Create a single star and place it in the correct position"""
    star = Star(screen)
    star.rect.x = 105 + (star.rect.width + 30) * star_number
    star.rect.y = 30 + (star.rect.height + 30) * row
    # star.direction *= (-1) ** row
    stars.add(star)
    
def many_stars(screen, stars):
    """Create a full screen of stars"""
    star = Star(screen)
    row_stars = stars_on_a_row(screen, star)
    row_number = number_of_rows(screen, star)
    
    for row in range(row_number):
        for star_number in range(row_stars):
            create_star(screen, stars, star_number, row)


       
            
            
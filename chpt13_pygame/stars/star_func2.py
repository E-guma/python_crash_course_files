from random import randint
import pygame


class Star(pygame.sprite.Sprite):
    """Create a star game element"""
    def __init__(self, screen, stars):
        super().__init__()
        self.screen = screen
        self.stars = stars
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_frect()
        self.rect.topleft = (-2*self.rect.width,30)
        self.direction = 1
        self.row_number = 0
        self.create_new = True
        
    def update(self):
        """Update star position"""
        if self.create_new and self.rect.right >= 30:
            star = Star(self.screen, self.stars)
            self.stars.add(star)
            
        if self.row_number == 0 and self.rect.right > 30:    
            self.create_new = False

            
        self.rect.x += 1.9 * self.direction
        # if self.rect.left >= 0:
        if (self.direction == 1) and (self.rect.right > self.screen.get_width() - 40):
            self.rect.y += (30 + self.rect.height)
            self.row_number += 1
            self.direction *= -1
            
        elif (self.direction == -1) and (self.rect.left < 40):
            self.rect.y += (30 + self.rect.height)
            self.row_number += 1
            self.direction *= -1
        if self.rect.top > self.screen.get_height():
            self.kill()

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
    star = Star(screen, stars)
    star.rect.x = 105 + (star.rect.width + 30) * star_number
    star.rect.y = 30 + (star.rect.height + 30) * row
    star.direction *= (-1) ** row
    stars.add(star)
    
def many_stars(screen, stars):
    """Create a full screen of stars"""
    star = Star()
    row_stars = stars_on_a_row(screen, star)
    row_number = number_of_rows(screen, star)
    
    for row in range(row_number):
        for star_number in range(row_stars):
            create_star(screen, stars, star_number, row)


       
            
            
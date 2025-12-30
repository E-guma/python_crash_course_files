import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.ACTIVEEVENT:
            
            print(event)
            
        pygame.display.flip()
        
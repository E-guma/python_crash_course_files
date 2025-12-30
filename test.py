import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# A red square
rect = pygame.Rect(250, 150, 50, 50)
dragging = False
screen_rect = screen.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If we click inside the square, start dragging
            if rect.collidepoint(event.pos):
                dragging = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            
        elif event.type == pygame.MOUSEMOTION:
            # HERE IS THE REL ATTRIBUTE IN ACTION
            if dragging:
                # event.rel contains (dx, dy)
                # We add that change to the rectangle's position
                dx, dy = event.rel
                rect.x += dx
                # rect.y += dy
                rect.clamp_ip(screen_rect)  # Keep the rect within screen bounds

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 50, 50), rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Elements to Screen")
font = pygame.font.Font(None, 40)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (200, 150, 200, 100))
    text = font.render("Hello Pygame!", True, (0, 0, 0))
    screen.blit(text, (220, 180))                    
    pygame.display.update()

pygame.quit()

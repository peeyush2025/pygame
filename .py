import pygame
pygame.init()
s=pygame.display.set_mode((600,400))
p=pygame.Rect(50,50,60,60)
e=pygame.Rect(300,200,60,60)
r=1
while r:
    for e2 in pygame.event.get():
        if e2.type==pygame.QUIT:r=0
    k=pygame.key.get_pressed()
    p.x+=(k[pygame.K_RIGHT]-k[pygame.K_LEFT])*5
    p.y+=(k[pygame.K_DOWN]-k[pygame.K_UP])*5
    s.fill((255,255,255))
    pygame.draw.rect(s,(0,0,255),p)
    pygame.draw.rect(s,(255,0,0),e)
    pygame.display.update()
pygame.quit()

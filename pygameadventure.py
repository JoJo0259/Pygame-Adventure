import pygame

pygame.init()

width = 500
height = 500

px = 50
py = 50
pwidth = 50
phight = 50
vel = 5

display  = pygame.display.set_mode((width, height))

pygame.display.set_caption("Adventure Game")

run = True
while run:
    pygame.time.delay(100)
    #not key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and px > vel:
        px -= vel
    if keys[pygame.K_RIGHT] and px < width - pwidth:
        px += vel
    if keys[pygame.K_UP] and py > vel:
        py -= vel
    if keys[pygame.K_DOWN] and py < height - phight:
        py += vel
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        vel = 15
    else:
        vel = 5
    #draw
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 0), (px, py, pwidth, phight))
    pygame.display.update()
pygame.quit()
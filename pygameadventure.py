import pygame
import os
import random

pygame.init()

width = 500
height = 500

grass1 = pygame.image.load('Assets\Map\Grass1.jpg')
grass2 = pygame.image.load('Assets\Map\Grass2.jpg')
water1 = pygame.image.load('Assets\Map\Water1.jpg')
water2 = pygame.image.load('Assets\Map\Water2.jpg')

def mapgen(grass1, grass2, water1, water2):
    map = {}
    i = 0
    for i in range(0, 20):
        map[i] = {}
        j = 0
        for j in range(0, 20):
            ran = random.randint(0, 3)
            if ran == 0:
                map[i][j] = grass1
            elif ran == 1:
                map[i][j] = grass2
            elif ran == 2 or ran == 3:
                if i == 0 or j == 0:
                    if ran == 2:
                        map[i][j] = water1
                    elif ran == 3:
                        map[i][j] = water2
                elif map[i-1][j] != water1 and map[i-1][j] != water2 and map[i][j-1] != water1 and map[i][j-1] != water2:
                    ran = random.randint(0, 1)
                    if ran == 0:
                        map[i][j] = grass1
                    elif ran == 1:
                        map[i][j] = grass2
                elif ran == 2:
                    map[i][j] = water1
                elif ran == 3:
                    map[i][j] = water2
            j += 1
        i += 1
    return map


def mapdraw(map, display):
    i = 0
    for i in range(0, 20):
        j = 0
        for j in range(0, 20):
            display.blit(map[i][j], (i*25, j*25))
            j += 1
        i += 1

px = 0
py = 0
pwidth = 25
phight = 25
pimg = pygame.image.load('Assets\Charachter\charachter.png')
vel = 5

display  = pygame.display.set_mode((width, height))

maptile = mapgen(grass1, grass2, water1, water2)
mapdraw(maptile, display)

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
    if keys[pygame.K_RIGHT] and px + vel < width - pwidth:
        px += vel
    if keys[pygame.K_UP] and py > vel:
        py -= vel
    if keys[pygame.K_DOWN] and py + vel < height - phight:
        py += vel
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        vel = 15
    else:
        vel = 5
    #draw
    #display.fill((0, 0, 0))
    #pygame.draw.rect(display, (0, 255, 0), (px, py, pwidth, phight))
    mapdraw(maptile, display)
    display.blit(pimg, (px, py))
    pygame.display.update()
pygame.quit()
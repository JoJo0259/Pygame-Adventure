import pygame
import os
import random
import json

#INITIALIZE#
pygame.init()

#IMAGE LOAD#
grass1 = pygame.image.load('Assets\Map\Grass1.jpg')
grass2 = pygame.image.load('Assets\Map\Grass2.jpg')
water1 = pygame.image.load('Assets\Map\Water1.jpg')
water2 = pygame.image.load('Assets\Map\Water2.jpg')

#MAP FUNCTIONS#
def mapgen():
    map = {}
    i = 0
    for i in range(0, 20):
        map[str(i)] = {}
        j = 0
        for j in range(0, 20):
            ran = random.randint(0, 1)
            if ran == 0:
                map[str(i)][str(j)] = "grass1"
            elif ran == 1:
                map[str(i)][str(j)] = "grass2"
            #elif ran == 2 or ran == 3:
                #if i == 0 or j == 0:
                    #if ran == 2:
                        #map[i][j] = "water1"
                    #elif ran == 3:
                        #map[i][j] = "water2"
                #elif map[i-1][j] != "water1" and map[i-1][j] != "water2" and map[i][j-1] != "water1" and map[i][j-1] != "water2":
                    #ran = random.randint(0, 1)
                    #if ran == 0:
                        #map[i][j] = "grass1"
                    #elif ran == 1:
                        #map[i][j] = "grass2"
                #elif ran == 2:
                    #map[i][j] = "water1"
                #elif ran == 3:
                    #map[i][j] = "water2"
            j += 1
        i += 1
    return map

def mapdraw(grass1, grass2, water1, water2, map, display):
    i = 0
    for i in range(0, 20):
        j = 0
        for j in range(0, 20):
            if map[str(i)][str(j)] == "grass1":
                display.blit(grass1, (i*25, j*25))
            elif map[str(i)][str(j)] == "grass2":
                display.blit(grass2, (i*25, j*25))
            j += 1
        i += 1

def storemaptile(psavenum, ptilex, ptiley, maptile):
    maptilepath = "Save\Save" + str(psavenum) + "\Map\Tile(" + str(ptilex) + ", " + str(ptiley) + ").json"
    with open(maptilepath, 'w') as f:
        json.dump(maptile, f, indent=4)

def loadmaptile(psavenum, ptilex, ptiley, maptile):
    maptilepath = "Save\Save" + str(psavenum) + "\Map\Tile(" + str(ptilex) + ", " + str(ptiley) + ").json"
    with open(maptilepath, 'r') as f:
        return json.load(f)

def mapfileexist(psavenum, ptilex, ptiley):
    maptilepath = "Save\Save" + str(psavenum) + "\Map\Tile(" + str(ptilex) + ", " + str(ptiley) + ").json"
    return os.path.exists(maptilepath)

#START#

#PLAYER#
px = 0 
py = 0
pimg = pygame.image.load('Assets\Charachter\charachter.png')
ptilex = 0
ptiley = 0
pwidth = 25
phight = 25
vel = 5
psavenum = 1

#DISPLAY#
width = 500
height = 500
display  = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adventure Game")

#MAP TILE LOAD?GEN#
maptile = {}
if mapfileexist(psavenum, ptilex, ptiley):
    maptile = loadmaptile(psavenum, ptilex, ptiley, maptile)
    mapdraw(grass1, grass2, water1, water2, maptile, display)
else:
    maptile = mapgen()
    mapdraw(grass1, grass2, water1, water2, maptile, display)
    storemaptile(psavenum, ptilex, ptiley, maptile)

#GAME#
run = True
while run:
    pygame.time.delay(100)
    
    #NOT KEY EVENTS#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #MOVEMENT#
    keys = pygame.key.get_pressed()

    #KEY LEFT MOVE#
    if keys[pygame.K_LEFT] and px > vel:
        px -= vel
    elif keys[pygame.K_LEFT] and px <= vel and mapfileexist(psavenum, ptilex - 1, ptiley):
        maptile = loadmaptile(psavenum, ptilex - 1, ptiley, maptile)
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptilex -= 1
        px = 500 - pwidth
    elif keys[pygame.K_LEFT] and px <= vel:
        storemaptile(psavenum, ptilex, ptiley, maptile)
        maptile = mapgen()
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptilex -= 1
        px = 500 - pwidth
        storemaptile(psavenum, ptilex, ptiley, maptile)
    
    #KEY RIGHT MOVE#
    if keys[pygame.K_RIGHT] and px + vel < width - pwidth:
        px += vel
    elif keys[pygame.K_RIGHT] and px + vel >= width - pwidth and mapfileexist(psavenum, ptilex + 1, ptiley):
        maptile = loadmaptile(psavenum, ptilex + 1, ptiley, maptile)
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptilex += 1
        px = 0
    elif keys[pygame.K_RIGHT] and px + vel >= width - pwidth:
        storemaptile(psavenum, ptilex, ptiley, maptile)
        maptile = mapgen()
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptilex += 1
        px = 0
        storemaptile(psavenum, ptilex, ptiley, maptile)
    
    #KEY UP MOVE#
    if keys[pygame.K_UP] and py > vel:
        py -= vel
    elif keys[pygame.K_UP] and py <= vel and mapfileexist(psavenum, ptilex, ptiley + 1):
        maptile = loadmaptile(psavenum, ptilex, ptiley + 1, maptile)
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptiley += 1
        py = 500 - phight
    elif keys[pygame.K_UP] and py <= vel:
        storemaptile(psavenum, ptilex, ptiley, maptile)
        maptile = mapgen()
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptiley += 1
        py = 500 - phight
        storemaptile(psavenum, ptilex, ptiley, maptile)
    
    #KEY DOWN MOVE
    if keys[pygame.K_DOWN] and py + vel < height - phight:
        py += vel
    elif keys[pygame.K_DOWN] and py + vel >= height - phight and mapfileexist(psavenum, ptilex, ptiley - 1):
        maptile = loadmaptile(psavenum, ptilex, ptiley - 1, maptile)
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptiley -= 1
        py = 0
    elif keys[pygame.K_DOWN] and py + vel >= height - phight:
        storemaptile(psavenum, ptilex, ptiley, maptile)
        maptile = mapgen()
        mapdraw(grass1, grass2, water1, water2, maptile, display)
        ptiley -= 1
        py = 0
        storemaptile(psavenum, ptilex, ptiley, maptile)
    
    #ACCELERATION#
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        vel = 15
    else:
        vel = 5
    
    #DRAW#
    mapdraw(grass1, grass2, water1, water2, maptile, display)
    display.blit(pimg, (px, py))
    pygame.display.update()
pygame.quit()
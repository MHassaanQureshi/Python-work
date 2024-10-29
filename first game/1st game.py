import sys
import pygame
import random
import math
pygame.init()
score = 0
screen = pygame.display.set_mode((800 , 600))
#change title
pygame.display.set_caption("first game")
#LOGO
icon = pygame.image.load("icon game.png")
pygame.display.set_icon(icon)
#adding background
background = pygame.image.load("background.png")
#adding ship
enemyimg = pygame.image.load("enemy.png")
enemyX =  random.randint(0,800)
enemyY =random.randint(50,150)
enemyX_change = 2
enemyY_change = 40

#Enemy
plyimage = pygame.image.load("ship.png")
plyimageX = 370
plyimageY = 480
#bullet
bullet = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(plyimage ,(x,y))

def enemy(x,y):
    screen.blit(enemyimg ,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet ,(x+16 , y+10))
def collision(enemyX,enemyY , bulletX,bulletY ):
    distance = math.sqrt((math.pow(enemyX - bulletX ,2))+ (math.pow(enemyY - bulletY ,2)))
    if distance < 20:
        return True
    else:
        return False
#screening Loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            running = False
            sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            plyimageX+=4
        if event.key == pygame.K_LEFT:
            plyimageX-=4
        if event.key == pygame.K_SPACE:
            bulletX = plyimageX
            fire_bullet(bulletX ,bulletY)
        
    if plyimageX<=0:
        plyimageX=0
    if plyimageX>=736:
        plyimageX=736
    
    
    enemyX += enemyX_change
    if enemyX<=0:
        enemyX_change = 2
        enemyY += enemyY_change
    if enemyX>=736:
        enemyX_change = -2
        enemyY += enemyY_change
    if bulletY<=20:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is"fire":
        fire_bullet(bulletX ,bulletY)
        bulletY -= bulletY_change
    #collision
    iscollision = collision(enemyX,enemyY , bulletX,bulletY )
    if collision:
        bulletY = 480
        bullet_state = "ready"  

    # change backgrond colour
    enemy(enemyX,enemyY)
    player(plyimageX,plyimageY)
    #always update when working on screen
    pygame.display.update()
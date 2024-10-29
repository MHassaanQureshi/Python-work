import pygame
import os

WINDOW = pygame.display.set_mode((800,450))
RED = (255,0,0)
YELLOW = (255,255,0)
BALL_COLOR = (255,255,255)
RED_BOX = pygame.Rect((0,225,10,80))
YELLOW_BOX = pygame.Rect((790,225,10,80))
BALL = pygame.Rect((400,225,10,10))
decrement = 5
FPS = 60

def DRAW_WINDOW():
     WINDOW.fill((0,0,0))
     pygame.draw.rect(WINDOW,RED,RED_BOX)
     pygame.draw.rect(WINDOW,YELLOW,YELLOW_BOX)
     pygame.draw.rect(WINDOW,BALL_COLOR,BALL)
     pygame.display.update()

def handle_ball(BALL):
    for movment in BALL:
        BALL.x += decrement

    for movment in BALL:
        BALL.y -= decrement


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
        
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_w]:
            RED_BOX.y -= decrement
        
        if keys_pressed[pygame.K_s]:
            RED_BOX.y += decrement

        eys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_UP]:
            YELLOW_BOX.y -= decrement
        
        if keys_pressed[pygame.K_DOWN]:
           YELLOW_BOX.y += decrement

        if YELLOW_BOX.y <= 0:
            YELLOW_BOX.y  = 0
        if YELLOW_BOX.y >= 370:
            YELLOW_BOX.y  = 370

        if RED_BOX.y <= 0:
            RED_BOX.y   = 0
        if RED_BOX.y  >= 370:
            RED_BOX.y   = 370

        DRAW_WINDOW()   
        handle_ball(BALL)     
    pygame.quit()


if __name__ == "__main__":
    main()

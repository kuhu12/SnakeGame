import pygame, sys
from pygame.locals import *
pygame.init()

window_width=600
window_height=600
canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Mini Project")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
speed=10
fps=25


font = pygame.font.SysFont(None, 40, True, True)
mainClock = pygame.time.Clock()

ballimg=pygame.image.load("ball.jpg")
ballrect=ballimg.get_rect()

while True:
    moveup=movedown=moveright=moveleft=False
    ballrect.centerx=ballrect.centery=300
    
    while True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:

                if event.key==K_UP:
                    moveup=True
                if event.key==K_DOWN:
                    movedown=True
                if event.key==K_LEFT:
                    moveleft=True
                if event.key==K_RIGHT:
                    moveright=True
                    
            if event.type==KEYUP:

                if event.key==K_UP:
                    moveup=False
                if event.key==K_DOWN:
                    movedown=False
                if event.key==K_LEFT:
                    moveleft=False
                if event.key==K_RIGHT:
                    moveright=False
                    
        if(moveup and (ballrect.top>0)):
            ballrect.top-=speed
        if(movedown and (ballrect.bottom<600)):
            ballrect.bottom+=speed
        if(moveleft and (ballrect.left>0)):
           ballrect.left-=speed
        if(moveright and (ballrect.right<600)):
           ballrect.right+=speed


        x=str(ballrect.centerx)
        y=str(ballrect.centery)

        posx=font.render(x,1,blue)
        posy=font.render(y,1,red)

        posxrect=posx.get_rect()
        posyrect=posy.get_rect()

        posxrect.topleft=(10,10)
        posyrect.topleft=(70,10)

        canvas.fill(green)
        canvas.blit(posx,posxrect)
        canvas.blit(posy,posyrect)

        canvas.blit(ballimg,ballrect)

        pygame.display.update()
        mainClock.tick(fps)
        
pygame.display.update()

        
        
            
    
    

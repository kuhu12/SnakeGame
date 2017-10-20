import pygame, random, sys
from pygame.locals import *
pygame.init()

#intialising variables

window_height=500 
window_width=500

black = (0,0,0)
blue = (0, 0, 225)
fps = 25
speed = 5
font = pygame.font.SysFont(None, 28)
mainClock = pygame.time.Clock()

Canvas = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('MINI PROJECT')

pygame.display.update()

ballimage = pygame.image.load('ball.jpg')
ballrect = ballimage.get_rect()


while True:

    moveup = movedown = moveright = moveleft = False
    ballrect.centerx = ballrect.centery = 250
    
    while True:     #the main game loop
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_UP:
                    moveup = True
                    
                if event.key == K_DOWN:
                    movedown = True
                if event.key == K_LEFT:
                    moveleft = True
                if event.key == K_RIGHT:
                    moveright = True
                    

            if event.type == KEYUP:

                if event.key == K_UP:
                    moveup = False
                if event.key == K_DOWN:
                    movedown = False

                if event.key == K_LEFT:
                    moveleft = False
                if event.key == K_RIGHT:
                    moveright = False

        if (moveup and (ballrect.top > 0)):
            ballrect.top-= speed
        if (movedown and (ballrect.bottom < 500)):
            ballrect.bottom += speed
        if (moveleft and (ballrect.left > 0)):
            ballrect.left -= speed
        if (moveright and (ballrect.right < 500)):
                ballrect.right += speed

        #getting the position of the ball

        x = str(ballrect.centerx)
        y = str(ballrect.centery)

        pos_x = font.render(x, 1, blue)
        pos_y = font.render(y, 1, blue)

        pos_xrect = pos_x.get_rect()
        pos_yrect = pos_y.get_rect()

        pos_xrect.topleft = (10, 10)
        pos_yrect.topleft = (50, 10)
        
                
        Canvas.fill(black)
        Canvas.blit(pos_x, pos_xrect)
        Canvas.blit(pos_y, pos_yrect)
    
        
        Canvas.blit(ballimage, ballrect)
        pygame.display.update()

        mainClock.tick(fps)
    
    pygame.mixer.music.stop()
pygame.display.update()

import pygame,sys
from pygame.locals import *
pygame.init()

canvas=pygame.display.set_mode((600,600))
pygame.display.set_caption("Mouse Input")
green=(0,255,0)
red=(255,0,0)

while True:
    for event in pygame.event.get():
        canvas.fill(red)
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            x= event.pos[0]
            y= event.pos[1]               
            pygame.draw.circle(canvas,green,(x,y),20,0)

    pygame.display.update()                       
                           
                           

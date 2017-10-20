import pygame, sys
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw the shapes")

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0,255, 0)
canvas.fill(black)
pygame.draw.rect(canvas, green, (10 , 10, 220, 220))
pygame.draw.circle(canvas, white, (150, 150), 100,3 )
pygame.draw.line(canvas, green,(20,20),(400,20) , 5) 
pygame.draw.polygon(canvas,red,((50,150),(150,50),(250,50),(350,150),(250,250),(150,250)),3)
pygame.display.update()


import pygame, sys
from pygame.locals import *
pygame.init()

font=pygame.font.SysFont(None,80,True,True)
text="Python is Fun!"
green=(0,255,0)
blue=(0,0,255)

textobj=font.render(text,1,blue)
textrect=textobj.get_rect()

canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Text Input')

textrect.left=250
textrect.right=250

canvas.blit(textobj,textrect)
pygame.display.update()

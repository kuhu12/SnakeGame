import pygame, sys
from pygame.locals import *
pygame.init()

canvas=pygame.display.set_mode((500,500))
pygame.display.set_caption("Keyboard Input")
black=(0,0,0)
canvas.fill(black)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()

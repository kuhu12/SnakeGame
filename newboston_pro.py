import pygame,sys
from pygame.locals import *
import time
import random

pygame.init()


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

window_width=800
window_height=600

canvas=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Slither")
clock=pygame.time.Clock()

block_width=10
fps=15
font=pygame.font.SysFont(None,40,True,True)


def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    canvas.blit(screen_text,[window_width/2,window_height/2])

def gameloop():
    gameExit=False
    gameOver=False
    
    lead_x=window_width/2
    lead_y=window_height/2
    
    lead_x_change=0
    lead_y_change=0

    randAppleX=random.randrange(0,window_width-block_width)
    randAppleY=random.randrange(0,window_height-block_width)
    
    
    while not gameExit:
        while gameOver==True:
            canvas.fill(white)
            message_to_screen("Game Over,press C to play again or Q to quit",blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_q:
                        gameExit=True
                        gameOver=False
                    if event.key==K_c:
                        gameloop()


                        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==KEYDOWN:
                if event.key==K_LEFT:
                    lead_x_change= -block_width
                    lead_y_change=0
                elif event.key==K_RIGHT:
                    lead_x_change= block_width
                    lead_y_change=0
                elif event.key==K_UP:
                    lead_y_change= -block_width
                    lead_x_change=0
                elif event.key==K_DOWN:
                    lead_y_change= block_width
                    lead_x_change=0
        if lead_x>=window_width or lead_x<0 or lead_y>=window_height or lead_y<0:
           gameOver=True

        
        lead_x += lead_x_change
        lead_y += lead_y_change
        canvas.fill(green)

        pygame.draw.rect(canvas,red,[randAppleX,randAppleY,block_width,block_width])
        pygame.draw.rect(canvas,black,[lead_x,lead_y,block_width,block_width])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
    

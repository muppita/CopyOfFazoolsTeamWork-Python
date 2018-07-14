import pygame

from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([1200,900])
background = pygame.image.load("board.png")

white = (255,255,255)


while True: 
    
    for event in pygame.event.get():
       if event.type == QUIT:
          pygame.quit()
    screen.blit(background,(0,0))
    pygame.draw.rect(background,(255,255,255),Rect((800,40),(90,80)))
    pygame.display.update()





  
    
    


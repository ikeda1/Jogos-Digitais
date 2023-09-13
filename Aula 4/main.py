'''
Pedro Henrique Ikeda
32016344
'''

import pygame as pg
from pygame.locals import *
from sys import exit

bg_img = 'mar.jpeg'
sprite_img = 'peixe.png'

pg.init()
screen = pg.display.set_mode((640, 480), 0, 32)
background = pg.image.load(bg_img).convert()
sprite = pg.image.load(sprite_img)


x = 0

while True:
    

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(sprite, (x,100))

    x += 1

    if x > 640:
        x -= 640
    
    pg.display.update()

'''
Pedro Henrique Ikeda
32016344
'''

import pygame as pg
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2

bg_img = 'mar.jpeg'
sprite_img = 'peixe.png'
sprite_img2 = 'peixe2.png'

pg.init()
screen = pg.display.set_mode((640, 480), 0, 32)

background = pg.image.load(bg_img).convert()
sprite = pg.image.load(sprite_img)
sprite2 = pg.image.load(sprite_img2)
sprite2 = pg.transform.scale(sprite2, (128, 128))

clock = pg.time.Clock()

position = Vector2(100.0, 100.0)
position2 = Vector2(600.0, 400.0)
speed = 250
heading = Vector2()
heading2 = Vector2()

while True:
    
    

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            destination = Vector2(*event.pos) - (Vector2(*sprite.get_size())/2)
            destination2 = Vector2(*event.pos) - (Vector2(*sprite2.get_size())/2)
            heading = Vector2.from_points(position, destination)
            heading2 = Vector2.from_points(position2, destination2)
            heading.normalize()
            heading2.normalize()

    screen.blit(background, (0,0))
    screen.blit(sprite, (position.x,position.y))
    screen.blit(sprite2, (position2.x, position2.y))

    fps = clock.tick()
    fps_seconds = fps/1000.0

    distance_moved = fps_seconds * speed

    position += heading * distance_moved
    position2 += heading2 * distance_moved
    pg.display.update()

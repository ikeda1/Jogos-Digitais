'''
Pedro Henrique Ikeda
32016344
'''

import pygame as pg
from pygame.locals import *
from sys import exit
from gameobjects.Vector2 import Vector2
import random
import time

bg_img = 'mar.jpeg'
sprite_img = 'peixe.png'
sprite_img2 = 'peixe2.png'
height = 480
width = 640
time_step = 1

pg.init()
screen = pg.display.set_mode((width, height), 0, 32)

background = pg.image.load(bg_img).convert()
sprite = pg.image.load(sprite_img)
sprite2 = pg.image.load(sprite_img2)
sprite2 = pg.transform.scale(sprite2, (128, 128))

clock = pg.time.Clock()

position = Vector2(100.0, 100.0)
position2 = Vector2(500.0, 350.0)
speed = 250
heading1 = Vector2()
heading2 = Vector2()
prev_time = time.time()

def random_move(sprite, position):
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    
    destination = Vector2(x,y) - (Vector2(*sprite.get_size())/2)
    heading = Vector2.from_points(position, destination)
    heading.normalize()
    print(heading)
    return heading

while True:
    
    

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

        # if event.type == MOUSEBUTTONDOWN:
        #     destination = Vector2(*event.pos) - (Vector2(*sprite.get_size())/2)
        #     destination2 = Vector2(*event.pos) - (Vector2(*sprite2.get_size())/2)
        #     print(event.pos)
        #     heading1 = Vector2.from_points(position, destination)
        #     heading2 = Vector2.from_points(position2, destination2)
        #     heading1.normalize()
        #     heading2.normalize()


    now = time.time()
    # print(now, prev_time)
    if now-prev_time >= time_step:
        heading1 = random_move(sprite, position)
        heading2 = random_move(sprite2, position)
        prev_time = now
        now = time.time()



    screen.blit(background, (0,0))
    screen.blit(sprite, (position.x,position.y))
    screen.blit(sprite2, (position2.x, position2.y))

    fps = clock.tick()
    fps_seconds = fps/1000.0

    distance_moved = fps_seconds * speed

    position += heading1 * distance_moved
    position2 += heading2 * distance_moved
    pg.display.update()

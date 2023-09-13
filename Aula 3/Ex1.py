'''
Pedro Henrique Ikeda
32016344
'''

import pygame
from pygame.locals import *
from sys import exit 
from random import *


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

def gera_cor():
    red = randrange(0,255)
    green = randrange(0,255)
    blue = randrange(0,255)
    colorRect = (red, green, blue)
    return colorRect

def retangulo():
    altura = randrange(0,70)
    largura = randrange(0,70)
    pos_x = randrange(0,600)
    pos_y = randrange(0,600)

    return pygame.draw.rect(screen, gera_cor(), (pos_x, pos_y, altura, largura))

def circulo():
    raio = randrange(0,100)
    pos_x = randrange(0,600)
    pos_y = randrange(0,600)

    return pygame.draw.circle(screen, gera_cor(), (pos_x,pos_y), raio)



# cria imagens com gradiantes suaves
def create_scales(height):
    red_scale_surface   = pygame.surface.Surface((640, height)) 
    green_scale_surface = pygame.surface.Surface((640, height)) 
    blue_scale_surface  = pygame.surface.Surface((640, height)) 
    for x in range(640):
        c = int((x/639.)*255.)
        red   = (c, 0, 0) 
        green = (0, c, 0) 
        blue  = (0, 0, c)
        line_rect = Rect(x, 0, 1, height) 
        pygame.draw.rect(red_scale_surface, red, line_rect) 
        pygame.draw.rect(green_scale_surface, green, line_rect) 
        pygame.draw.rect(blue_scale_surface, blue, line_rect)
    return red_scale_surface, green_scale_surface, blue_scale_surface 

red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    retangulo()
    circulo()

    pygame.display.update()

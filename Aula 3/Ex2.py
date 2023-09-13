'''
Pedro Henrique Ikeda
32016344
'''

import pygame
from pygame.locals import *
from sys import exit 
from random import *

RETANGULO = 1

def lerp(val1, val2, factor):
    return val1+(val2 - val1) * factor

def blend(color1,color2,blend_factor = 0.1):
    red1,green1,blue1 = color1
    red2,green2,blue2 = color2
    red = lerp(red1, red2, blend_factor)
    green = lerp(green1, green2, blend_factor)
    blue = lerp(blue1, blue2, blend_factor)
    return int(red), int(green), int(blue)

def desenha_formas(params):
    if params['forma'] == RETANGULO:
        pygame.draw.rect(params['surface'], params['cor'],(params['x'],params['y'],params['height'],params['width']))

def desafio2():
    pygame.init()
    surface = pygame.display.set_mode((640,480),0,32)

    cor = (221,99,20)
    lerp_cor = (96,130,51)
    width = 640//3
    height = 480//2
    x1,y1 = 0, 0
    x2,y2 = x1 + width, 0
    x3,y3 = x2 + width, 0
    x4,y4 = 0, y1 + height
    x5,y5 = x4 + width, y1 + height
    x6,y6 = x5 + width, y1 + height
    fator1 = 0.1
    fator2 = 0.1
    fator3 = 0.1
    fator4 = 0.1
    fator5 = 0.1
    fator6 = 0.1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if y_mouse < height:
            if x_mouse < width:
                fator1 = x_mouse/480
            elif x_mouse < width*2:
                fator2 = x_mouse/480
            else:
                fator3 = x_mouse/480
        else:
            if x_mouse < width:
                fator4 = x_mouse/480
            elif x_mouse < width*2:
                fator5 = x_mouse/480
            else:
                fator6 = x_mouse/480
        cor_atual1 = blend(cor, lerp_cor, fator1)
        cor_atual2 = blend(cor, lerp_cor, fator2)
        cor_atual3 = blend(cor, lerp_cor, fator3)
        cor_atual4 = blend(cor, lerp_cor, fator4)
        cor_atual5 = blend(cor, lerp_cor, fator5)
        cor_atual6 = blend(cor, lerp_cor, fator6)
        def_1 = {'cor': cor_atual1, 'surface': surface, 'forma': RETANGULO,'x':x1, 'y':y1,'width': width,'height':height}
        def_2 = {'cor': cor_atual2, 'surface': surface, 'forma': RETANGULO,'x':x2, 'y':y2,'width': width,'height':height}
        def_3 = {'cor': cor_atual3, 'surface': surface, 'forma': RETANGULO,'x':x3, 'y':y3,'width': width,'height':height}
        def_4 = {'cor': cor_atual4, 'surface': surface, 'forma': RETANGULO,'x':x4, 'y':y4,'width': width,'height':height}
        def_5 = {'cor': cor_atual5, 'surface': surface, 'forma': RETANGULO,'x':x5, 'y':y5,'width': width,'height':height}
        def_6 = {'cor': cor_atual6, 'surface': surface, 'forma': RETANGULO,'x':x6, 'y':y6,'width': width,'height':height}

        desenha_formas(def_1)
        desenha_formas(def_2)
        desenha_formas(def_3)
        desenha_formas(def_4)
        desenha_formas(def_5)
        desenha_formas(def_6)
        pygame.display.update()

if __name__== '__main__':
    desafio2()

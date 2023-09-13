import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tanque.jpg').convert()

x,y=0,0
move_x, move_y = 0,0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        

    mx,my=pygame.mouse.get_pos()

    screen.fill((255,255,255))
    screen.blit(tank,(mx-(tank.get_width()//2),my-(tank.get_height()//2)))

    pygame.display.update()

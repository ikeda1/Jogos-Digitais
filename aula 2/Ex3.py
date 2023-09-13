import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE =(800,600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0 ,32)

tank = pygame.image.load('tanque.jpg').convert()

x,y=0,0
move_x, move_y = 0,0
dir = 0
# 0 = Left | 1 = Right | 2 = Up | 3 = Down

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            print(dir)
            if event.key==K_LEFT:
                move_x=-10
                move_y= 0
                dir = 0

                print(x)
            if event.key==K_RIGHT:
                move_x= 10
                move_y= 0
                dir = 1
                print(x)
            if event.key==K_UP:
                move_y=-10
                move_x= 0
                dir = 2
                print(x)
            if event.key==K_DOWN:
                move_y= 10
                move_x= 0
                dir = 3
                print(x)

                
        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x=0
                move_y=0
            if event.key == K_RIGHT:
                move_x=0
                move_y=0
            if event.key == K_UP:
                move_x=0
                move_y=0
            if event.key == K_DOWN:
                move_x=0
                move_y=0




        x += move_x
        y += move_y

        screen.fill((255,255,255))
        if dir == 0:
            img = tank

        elif dir == 1:
            img = pygame.transform.flip(tank, True, False)
        elif dir == 2:
            img = pygame.transform.flip(tank, True, False)
        elif dir == 3:
            img = pygame.transform.flip(tank, False, True)

        screen.blit(img,(x,y))

        pygame.display.update()

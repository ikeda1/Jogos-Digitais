import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Animation')
WHITE = (255,255,255)
catImg = pygame.image.load('gato.png')
w, h = catImg.get_size()
catx = (w*2)
caty = (h+2)+h//2 + 1
angle = 0
speed = 5
direction = 'right'


def blitRotate(surface, image, pos, originPos, angle):
    #calculate the axis aligned bounding box of the rotated image
    w, h        = image.get_size()
    box         = [pygame.math.Vector2(p) for p in [(0, 0),(w, 0), (w, -h), (0, -h)]]
    box_rotate  = [p.rotate(angle) for p in box]
    min_box     = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1]) 
    max_box     = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1]) 

    #calculate the translation of the pivot
    pivot       = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate= pivot.rotate(angle)
    pivot_move  = pivot_rotate - pivot

    #calculate the upper left origin of the rotate image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] + min_box[1] - pivot_move[1])

    #get a rotate image
    rotated_image = pygame.transform.rotate(image, angle)

    #rotate and blit the image
    surface.blit(rotated_image, origin)

    #draw rectangle around the image
    # pygame.draw.rect(surface, (255,0,0), (*origin, *rotated_image.get_size()),2)

while True:
    DISPLAYSURF.fill(WHITE)       


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        
        if pygame.key.get_pressed()[pygame.K_d]:
            angle -= 5


        if pygame.key.get_pressed()[pygame.K_e]:
            angle += 5


    if direction == 'right':
        catx += speed
        if catx == (400-(w/2)):
            direction = 'down'
    elif direction == 'down':
        caty += speed
        if caty == (300+(h/2 + 1)):
            direction = 'left'
    elif direction == 'left':
        catx -= speed
        if catx == (w/2):
            direction = 'up'
    elif direction == 'up':
        caty -= speed
        if caty == (h+2)+h//2 + 1:
            direction = 'right'

   
    # DISPLAYSURF.blit(catImg, (catx, caty))
    blitRotate(DISPLAYSURF, catImg, (catx,caty), (w/2, h/2), angle)

    
    pygame.display.update()
    fpsClock.tick(FPS)


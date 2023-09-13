import pygame

pygame.init() #inicia diversas funcionalidades do pygame

#retorna uma tela pronta com a dimensão passada por parametro
screen = pygame.display.set_mode((600,400)) 

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill((255,255,255)) #preenche a tela com uma determinada cor
    colorPolygon = (255,0,0)
    pointList = [[300, 300], [100, 400],[100, 300]] #coordenadas x,y dos lados
    pygame.draw.polygon(screen, colorPolygon, pointList)
    pygame.display.flip() #atualiza o display
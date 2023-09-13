import pygame

pygame.init() #inicia diversas funcionalidades do pygame

#retorna uma tela pronta com a dimensão passada por parametro
screen = pygame.display.set_mode((900,600)) 

loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill((255,255,255)) #preenche a tela com uma determinada cor
    colorCircle = (255,0,0)
    pos = [300,300]
    radius = 170
    width = 0
    pygame.draw.circle(screen, colorCircle, pos, radius, )
    pygame.display.flip() #atualiza o display
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
    colorRect = (255,0,0)
    pygame.draw.rect(screen, colorRect, (40,40,90,30),3)
    pygame.display.flip() #atualiza o display


    
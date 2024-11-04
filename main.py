# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Variaveis
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

# Game-Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
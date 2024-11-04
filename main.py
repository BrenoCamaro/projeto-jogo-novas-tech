# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
from sys import exit
import Jogador

pygame.init()

# Variaveis
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
jogador = Jogador.Jogador()
relogio = pygame.time.Clock()

# Game-Loop
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    jogador.draw(tela)
    jogador.update()
    pygame.display.flip()

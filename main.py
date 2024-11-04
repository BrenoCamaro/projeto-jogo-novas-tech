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
imagem_personagem_parado = pygame.sprite.Group()
imagem_personagem_parado.add(jogador)

# Game-Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    imagem_personagem_parado.draw(tela)
    pygame.display.flip()
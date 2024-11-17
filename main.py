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
todas_as_sprites = pygame.sprite.Group()
jogador = Jogador.Jogador()
todas_as_sprites.add(jogador)
relogio = pygame.time.Clock()

# Game-Loop
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_d]:
            jogador.andar()
            
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()

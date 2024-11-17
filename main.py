# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
from sys import exit
import Jogador

pygame.init()

# Variaveis
largura = 1236
altura = 640
tela = pygame.display.set_mode((largura, altura))
todas_as_sprites = pygame.sprite.Group()
jogador = Jogador.Jogador()
todas_as_sprites.add(jogador)
imagem_fundo = pygame.image.load('imagem_fundo\masmorra.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
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
    tela.blit(imagem_fundo, (0, 0))        
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()

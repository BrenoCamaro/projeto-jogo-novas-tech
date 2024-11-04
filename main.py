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
x = int(largura / 2)
y = int(altura / 2)
relogio = pygame.time.Clock()

# Game-Loop
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]: 
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20
                
    rect_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    pygame.display.flip()

import pygame
import  sys
from pygame.locals import *

pygame.init()

LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/PlanoDeFundo.jpg").convert_alpha()
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA, ALTURA))

ALIEN_IMG = pygame.image.load("imagens/aircraft.png").convert_alpha()
ALIEN_IMG = pygame.transform.scale(ALIEN_IMG, (50, 50))
POSICAO_X_ALIEN = 500
POSICAO_Y_ALIEN = 300

JOGADOR_IMG = pygame.image.load("imagens/spaceship (1).png").convert_alpha()
JOGADOR_IMG = pygame.transform.scale(JOGADOR_IMG, (50, 50))
JOGADOR_IMG = pygame.transform.rotate(JOGADOR_IMG, -90)
POSICAO_X_JOGADOR = 200
POSICAO_Y_JOGADOR = 300

pygame.display.set_caption("Space Journey")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    TELA.blit(IMAGEM_FUNDO, (0, 0))

    #Criando movimento da tela de fundo
    rel_x = LARGURA % IMAGEM_FUNDO.get_rect().width
    TELA.blit(IMAGEM_FUNDO, (rel_x - IMAGEM_FUNDO.get_rect().width, 0))
    if rel_x < LARGURA:
        TELA.blit(IMAGEM_FUNDO, (rel_x, 0))
    LARGURA -= 2

    TELA.blit(ALIEN_IMG, (POSICAO_X_ALIEN, POSICAO_Y_ALIEN))
    TELA.blit(JOGADOR_IMG, (POSICAO_X_JOGADOR, POSICAO_Y_JOGADOR))
    pygame.display.update()
            
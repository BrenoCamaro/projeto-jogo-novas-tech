import pygame
import  sys
import random
from pygame.locals import *

pygame.init()

LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/1.jpg").convert_alpha()
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


MUNICAO = pygame.image.load("imagens/bullet.png").convert_alpha()
MUNICAO = pygame.transform.scale(MUNICAO, (25, 25))
MUNICAO = pygame.transform.rotate(MUNICAO, -45)

VELOCIDADE_X_MUNICAO = 0
POSICAO_X_MUNICAO = 200
POSICAO_Y_MUNICAO = 300

GATILHO = False

pygame.display.set_caption("Space Journey")

#Função que defini o respawn dos aliens
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

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

    #Controles
    TECLA = pygame.key.get_pressed()
    if TECLA[K_w] and POSICAO_Y_JOGADOR > 1:
        POSICAO_Y_JOGADOR -= 5

        if not GATILHO:
            POSICAO_Y_MUNICAO -= 5

    if TECLA[K_s] and POSICAO_Y_JOGADOR < ALTURA:
        POSICAO_Y_JOGADOR += 5

        if not GATILHO:
            POSICAO_Y_MUNICAO += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        VELOCIDADE_X_MUNICAO = 1

    #Respawn do Alien
    if POSICAO_X_ALIEN == 50:
        POSICAO_X_ALIEN = respawn()[0]
        POSICAO_Y_ALIEN = respawn()[1]
        
    #Movimento do Alien
    LARGURA -= 2
    POSICAO_X_ALIEN -= 1

    #Movimento da Bala
    POSICAO_X_MUNICAO += VELOCIDADE_X_MUNICAO

    TELA.blit(ALIEN_IMG, (POSICAO_X_ALIEN, POSICAO_Y_ALIEN))
    TELA.blit(MUNICAO, (POSICAO_X_MUNICAO, POSICAO_Y_MUNICAO))
    TELA.blit(JOGADOR_IMG, (POSICAO_X_JOGADOR, POSICAO_Y_JOGADOR))
    pygame.display.update()
            
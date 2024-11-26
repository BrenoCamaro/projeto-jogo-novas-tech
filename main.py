import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador

pygame.init()

RODANDO = True

#Configurações de Tela
pygame.font.init()
LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/1.jpg").convert_alpha()
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA, ALTURA))
PONTOS = 2
pygame.display.set_caption("Space Journey")

alien = Alien()
jogador = Jogador()

#Classe Jogador
'''
JOGADOR_IMG = pygame.image.load("imagens/spaceship (1).png").convert_alpha()
JOGADOR_IMG = pygame.transform.scale(JOGADOR_IMG, (50, 50))
JOGADOR_IMG = pygame.transform.rotate(JOGADOR_IMG, -90)
POSICAO_X_JOGADOR = 200
POSICAO_Y_JOGADOR = 300
JOGADOR_IMG_RECT = JOGADOR_IMG.get_rect()
'''

#Classe Munição
MUNICAO = pygame.image.load("imagens/bullet.png").convert_alpha()
MUNICAO = pygame.transform.scale(MUNICAO, (25, 25))
VELOCIDADE_X_MUNICAO = 0
POSICAO_X_MUNICAO = 200
POSICAO_Y_MUNICAO = 300
GATILHO = False
MUNICAO_RECT = MUNICAO.get_rect()

#Função de respawn da Municao
def respawn_municao():
    gatilho = False
    respawn_municao_x = jogador.coordenadaX
    respawn_municao_y = jogador.coordenadaY
    velocidade_x_municao = 0
    return [respawn_municao_x, respawn_municao_y, gatilho, velocidade_x_municao]

#Função de colisão
def colisao():
    global PONTOS

    if jogador.retanguloDaImagem.colliderect(alien.retanguloDaImagem) or alien.retanguloDaImagem.x == 60:
        PONTOS -= 1
        return True
    elif MUNICAO_RECT.colliderect(alien.retanguloDaImagem):
        PONTOS += 1
        return True
    else:
        return False


while RODANDO:
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
    if TECLA[K_w] and jogador.coordenadaY > 1:
        jogador.coordenadaY -= 5

        if not GATILHO:
            POSICAO_Y_MUNICAO -= 5

    if TECLA[K_s] and jogador.coordenadaY < ALTURA:
        jogador.coordenadaY += 5

        if not GATILHO:
            POSICAO_Y_MUNICAO += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        VELOCIDADE_X_MUNICAO = 8

    if PONTOS == -1:
        RODANDO = False
    #Respawn do Alien
    if alien.coordenadaX == 50:
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Respawn da Municao
    if POSICAO_X_MUNICAO == 1000:
        POSICAO_X_MUNICAO, POSICAO_Y_MUNICAO, GATILHO, VELOCIDADE_X_MUNICAO = respawn_municao()

    if alien.coordenadaX == 50 or colisao():
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Posicao dos retangulos das imagens (Jogador, Alien, Municao)
    jogador.retanguloDaImagem.y = jogador.coordenadaY
    jogador.retanguloDaImagem.x = jogador.coordenadaX

    alien.retanguloDaImagem.y = alien.coordenadaY
    alien.retanguloDaImagem.x = alien.coordenadaX

    MUNICAO_RECT.y = POSICAO_Y_MUNICAO
    MUNICAO_RECT.x = POSICAO_X_MUNICAO
        
    #Movimento do Alien
    LARGURA -= 2
    alien.coordenadaX -= 1

    #Movimento da Bala
    POSICAO_X_MUNICAO += VELOCIDADE_X_MUNICAO

    pygame.draw.rect(TELA, (255,0, 0), jogador.retanguloDaImagem, 4)
    pygame.draw.rect(TELA, (255,0, 0), MUNICAO_RECT, 4)
    pygame.draw.rect(TELA, (255,0, 0), alien.retanguloDaImagem, 4)

    TELA.blit(alien.imagem, (alien.coordenadaX, alien.coordenadaY))
    TELA.blit(MUNICAO, (POSICAO_X_MUNICAO, POSICAO_Y_MUNICAO))
    TELA.blit(jogador.imagem, (jogador.coordenadaX, jogador.coordenadaY))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {PONTOS}", True, (255, 255, 255))

    TELA.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
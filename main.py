import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador
from municaoDaNave import MunicaoDaNave

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
municao = MunicaoDaNave()

#Classe Munição
'''
MUNICAO = pygame.image.load("imagens/bullet.png").convert_alpha()
MUNICAO = pygame.transform.scale(MUNICAO, (25, 25))
VELOCIDADE_X_MUNICAO = 0
POSICAO_X_MUNICAO = 200
POSICAO_Y_MUNICAO = 300
MUNICAO_RECT = MUNICAO.get_rect()
'''
GATILHO = False

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
    elif municao.retanguloDaImagem.colliderect(alien.retanguloDaImagem):
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
            municao.coordenadaY -= 5

    if TECLA[K_s] and jogador.coordenadaY < ALTURA:
        jogador.coordenadaY += 5

        if not GATILHO:
            municao.coordenadaY += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        municao.velocidade = 8

    if PONTOS == -1:
        RODANDO = False
    #Respawn do Alien
    if alien.coordenadaX == 50:
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Respawn da Municao
    if municao.coordenadaX == 1000:
        municao.coordenadaX, municao.coordenadaY, GATILHO, municao.velocidade = respawn_municao()

    if alien.coordenadaX == 50 or colisao():
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Posicao dos retangulos das imagens (Jogador, Alien, Municao)
    jogador.retanguloDaImagem.y = jogador.coordenadaY
    jogador.retanguloDaImagem.x = jogador.coordenadaX

    alien.retanguloDaImagem.y = alien.coordenadaY
    alien.retanguloDaImagem.x = alien.coordenadaX

    municao.retanguloDaImagem.y = municao.coordenadaY
    municao.retanguloDaImagem.x = municao.coordenadaX
        
    #Movimento do Alien
    LARGURA -= 2
    alien.coordenadaX -= 1

    #Movimento da Bala
    municao.coordenadaX += municao.velocidade

    pygame.draw.rect(TELA, (255,0, 0), jogador.retanguloDaImagem, 4)
    pygame.draw.rect(TELA, (255,0, 0), municao.retanguloDaImagem, 4)
    pygame.draw.rect(TELA, (255,0, 0), alien.retanguloDaImagem, 4)

    TELA.blit(alien.imagem, (alien.coordenadaX, alien.coordenadaY))
    TELA.blit(municao.imagem, (municao.coordenadaX, municao.coordenadaY))
    TELA.blit(jogador.imagem, (jogador.coordenadaX, jogador.coordenadaY))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {PONTOS}", True, (255, 255, 255))

    TELA.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador
from municaoDaNave import MunicaoDaNave
from colisao import Colisao

pygame.init()

RODANDO = True

#Configurações de Tela
pygame.font.init()
LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/1.jpg").convert_alpha()
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA, ALTURA))
pygame.display.set_caption("Space Journey")

alien = Alien()
jogador = Jogador()
municao = MunicaoDaNave()
colisao = Colisao()

GATILHO = False

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

    if colisao.pontuacao == -1:
        RODANDO = False
    #Respawn do Alien
    if alien.coordenadaX == 50:
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Respawn da Municao
    if municao.coordenadaX == 1000:
        municao.coordenadaX, municao.coordenadaY, GATILHO, municao.velocidade = municao.municaoRespawn(jogador)

    if alien.coordenadaX == 50 or colisao.colisao(jogador, alien, municao):
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
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {colisao.pontuacao}", True, (255, 255, 255))

    TELA.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador
from municaoDaNave import MunicaoDaNave
from colisao import Colisao
from configuracoes import Configuraoces as Config

pygame.init()
pygame.font.init()
pygame.display.set_caption("Space Journey")

RODANDO = True

config = Config()
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
    config.tela.blit(config.imagemDeFundo, (0, 0))

    #Criando movimento da tela de fundo
    config.animacaoTelaDeFundo()

    #Controles
    TECLA = pygame.key.get_pressed()
    if TECLA[K_w] and jogador.coordenadaY > 1:
        jogador.coordenadaY -= 5

        if not GATILHO:
            municao.coordenadaY -= 5

    if TECLA[K_s] and jogador.coordenadaY < config.altura:
        jogador.coordenadaY += 5

        if not GATILHO:
            municao.coordenadaY += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        municao.velocidade = 8

    if colisao.pontuacao == -1:
        RODANDO = False

    alien.alienRespawn(colisao, jogador, municao)

    #Respawn da Municao
    if municao.coordenadaX == 1000:
        municao.coordenadaX, municao.coordenadaY, GATILHO, municao.velocidade = municao.municaoRespawn(jogador)

    #Posicao dos retangulos das imagens (Jogador, Alien, Municao)
    jogador.retanguloDaImagem.y = jogador.coordenadaY
    jogador.retanguloDaImagem.x = jogador.coordenadaX

    alien.retanguloDaImagem.y = alien.coordenadaY
    alien.retanguloDaImagem.x = alien.coordenadaX

    municao.retanguloDaImagem.y = municao.coordenadaY
    municao.retanguloDaImagem.x = municao.coordenadaX
        
    alien.movimentacao(config, colisao)

    #Movimento da Bala
    municao.coordenadaX += municao.velocidade

    config.tela.blit(alien.imagem, (alien.coordenadaX, alien.coordenadaY))
    config.tela.blit(municao.imagem, (municao.coordenadaX, municao.coordenadaY))
    config.tela.blit(jogador.imagem, (jogador.coordenadaX, jogador.coordenadaY))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {colisao.pontuacao}", True, (255, 255, 255))

    config.tela.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
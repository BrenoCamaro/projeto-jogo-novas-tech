import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador
from municaoDaNave import MunicaoDaNave
from colisao import Colisao
from configuracoes import Configuraoces as Config
from controles import Controles
from imprimindoTela import imprimindo

pygame.init()
pygame.display.set_caption("Space Journey")

RODANDO = True

config = Config()
alien = Alien()
jogador = Jogador()
municao = MunicaoDaNave()
colisao = Colisao()
controle = Controles()

while RODANDO:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    config.tela.blit(config.imagemDeFundo, (0, 0))

    #Criando movimento da tela de fundo
    config.animacaoTelaDeFundo()

    #Controles
    tecla = pygame.key.get_pressed()

    if colisao.pontuacao == -1:
        RODANDO = False

    controle.controlesDoJogo(jogador, municao, config, tecla)

    alien.alienRespawn(colisao, jogador, municao)

    #Respawn da Municao
    if municao.coordenadaX == 1000:
        municao.coordenadaX, municao.coordenadaY, jogador.atirar, municao.velocidade = municao.municaoRespawn(jogador)

    jogador.retanguloDaImagem.y = jogador.coordenadaY
    jogador.retanguloDaImagem.x = jogador.coordenadaX

    alien.retanguloDaImagem.y = alien.coordenadaY
    alien.retanguloDaImagem.x = alien.coordenadaX

    municao.retanguloDaImagem.y = municao.coordenadaY
    municao.retanguloDaImagem.x = municao.coordenadaX

    alien.movimentacao(config, colisao)

    #Movimento da Bala
    municao.coordenadaX += municao.velocidade

    imprimindo(jogador, alien, municao, config, colisao)

    pygame.display.update()
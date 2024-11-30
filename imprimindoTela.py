import pygame
import  sys
from pygame.locals import *

pygame.font.init()

def imprimindo(jogador, alien, municao, config, colisao):

    config.tela.blit(alien.imagem, (alien.coordenadaX, alien.coordenadaY))
    config.tela.blit(municao.imagem, (municao.coordenadaX, municao.coordenadaY))
    config.tela.blit(jogador.imagem, (jogador.coordenadaX, jogador.coordenadaY))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {colisao.pontuacao}", True, (255, 255, 255))

    config.tela.blit(PONTUACAO_TEXTO, (10, 10))

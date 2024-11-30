import pygame
import  sys
from pygame.locals import *

class Controles():

    def controlesDoJogo(self, jogador, municao, config, tecla):
        
        if tecla[K_w] and jogador.coordenadaY > 1:
            jogador.coordenadaY -= 5

            if not jogador.atirar:
                municao.coordenadaY -= 5

        if tecla[K_s] and jogador.coordenadaY < config.altura:
            jogador.coordenadaY += 5

            if not jogador.atirar:
                municao.coordenadaY += 5

        if tecla[K_SPACE]:
            jogador.atirar = True
            municao.velocidade = 8

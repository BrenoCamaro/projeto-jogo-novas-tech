import pygame
import  sys
import random
from pygame.locals import *

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem = pygame.image.load("imagens/spaceship.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.coordenadaX = 500
        self.coordenadaY = 300
        self.retanguloDaImagem = self.imagem.get_rect()

    def alienRespawn(self, colisao, jogador, municao):
        coordenadaX = 1000
        coordenadaY = random.randint(1, 640)

        if self.coordenadaX == 50:
            self.coordenadaX = coordenadaX
            self.coordenadaY = coordenadaY

        if self.coordenadaX == 50 or colisao.colisao(jogador, self, municao):
            self.coordenadaX = coordenadaX
            self.coordenadaY = coordenadaY

    def movimentacao(self, config, colisao):
        config.largura -= 2
        self.coordenadaX -= 0.7

        if colisao.pontuacao <= 5:
            self.coordenadaX -= 0.3
        elif 10 <= colisao.pontuacao <= 13:
            self.coordenadaX -= 1
        elif 14 <=colisao.pontuacao <= 16:
            self.coordenadaX -= 2
        elif 17 <=colisao.pontuacao <= 18:
            self.coordenadaX -= 2.5
        elif colisao.pontuacao >= 19:
            self.coordenadaX -= 3
    

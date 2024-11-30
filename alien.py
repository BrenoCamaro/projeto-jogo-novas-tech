import pygame
import  sys
import random
from pygame.locals import *

class Alien():
    def __init__(self):
        self.imagem = pygame.image.load("imagens/spaceship.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.coordenadaX = 500
        self.coordenadaY = 300
        self.retanguloDaImagem = self.imagem.get_rect()

    def AlienRespawn(self, colisao, jogador, municao):
        coordenadaX = 1000
        coordenadaY = random.randint(1, 640)

        if self.coordenadaX == 50:
            self.coordenadaX = coordenadaX
            self.coordenadaY = coordenadaY

        if self.coordenadaX == 50 or colisao.colisao(jogador, self, municao):
            self.coordenadaX = coordenadaX
            self.coordenadaY = coordenadaY
    

import pygame
import  sys
import random
from pygame.locals import *

class MunicaoDaNave():
    def __init__(self):
        self.imagem = pygame.image.load("imagens/bullet.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (25, 25))
        self.velocidade = 0
        self.coordenadaX = 200
        self.coordenadaY = 300
        self.retanguloDaImagem = self.imagem.get_rect()

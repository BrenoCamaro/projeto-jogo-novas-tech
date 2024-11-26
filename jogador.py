import pygame
import  sys
import random
from pygame.locals import *

class Jogador():
    def __init__(self):
        self.imagem = pygame.image.load("imagens/spaceship (1).png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.imagem = pygame.transform.rotate(self.imagem, -90)
        self.coordenadaX = 200
        self.coordenadaY = 300
        self.retanguloDaImagem = self.imagem.get_rect()
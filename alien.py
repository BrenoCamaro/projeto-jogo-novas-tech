import pygame
import  sys
import random
from pygame.locals import *

class Alien():
    def __init__(self):
        self.imagem = pygame.image.load("imagens/aircraft.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (50, 50))
        self.coordenadaX = 500
        self.coordenadaY = 300
        self.retanguloDaImagem = self.imagem.get_rect()

    def AlienRespawn(self):
        coordenadaX = 1000
        coordenadaY = random.randint(1, 640)
        return [coordenadaX, coordenadaY]
    

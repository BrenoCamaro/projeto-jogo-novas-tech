import pygame
import  sys
import random
from pygame.locals import *

class Configuraoces():
    def __init__(self):
        self.largura = 1280
        self.altura = 667
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.imagemDeFundo = pygame.image.load("imagens/1.jpg").convert_alpha()
        self.imagemDeFundo = pygame.transform.scale(self.imagemDeFundo, (self.largura, self.altura))

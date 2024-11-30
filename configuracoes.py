import pygame
import  sys
import random
from pygame.locals import *

class Configuraoces():
    def __init__(self):
        self.largura = 1000
        self.altura = 667
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.imagemDeFundo = pygame.image.load("imagens/estrelas.png").convert_alpha()
        self.imagemDeFundo = pygame.transform.scale(self.imagemDeFundo, (self.largura, self.altura))

    def animacaoTelaDeFundo(self):
        rel_x = self.largura % self.imagemDeFundo.get_rect().width
        self.tela.blit(self.imagemDeFundo, (rel_x - self.imagemDeFundo.get_rect().width, 0))
        if rel_x < 1280:
            self.tela.blit(self.imagemDeFundo, (rel_x, 0))
        self.largura -= 0.1

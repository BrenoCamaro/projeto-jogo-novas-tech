# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
import os

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pasta_imagens_jogador = "imagens_jogador"
        nome_imagens_jogador_parado = ["personagem_parado1.png", "personagem_parado2.png", "personagem_parado3.png", "personagem_parado4.png", "personagem_parado5.png"]
        self.sprite_parado = [pygame.image.load(os.path.join(pasta_imagens_jogador, nome)) for nome in nome_imagens_jogador_parado]
        
        self.image = self.sprite_parado[0]
        self.rect = self.image.get_rect() # Pegando o retangulo da imagem
        self.rect.topleft = 100, 100 # Posição da imagem na tela



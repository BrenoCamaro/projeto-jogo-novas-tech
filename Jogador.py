# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
import os

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagens_jogador/personagem_parado1.png")
        self.rect = self.image.get_rect()
        
    def update(self):

        if pygame.key.get_pressed()[K_a]: 
            self.rect.move_ip(-20, 0)
        if pygame.key.get_pressed()[K_d]:
            self.rect.move_ip(20, 0)
        if pygame.key.get_pressed()[K_w]:
            self.rect.move_ip(0, -20)
        if pygame.key.get_pressed()[K_s]:
            self.rect.move_ip(0, 20)


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    




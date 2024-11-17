# Bibliotecas utilizadas 
import pygame
from pygame.locals import *
import os

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("imagens_jogador/personagem_correndo1.png"))
        self.sprites.append(pygame.image.load("imagens_jogador/personagem_correndo2.png"))
        self.sprites.append(pygame.image.load("imagens_jogador/personagem_correndo3.png"))
        self.sprites.append(pygame.image.load("imagens_jogador/personagem_correndo4.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        #self.image = pygame.image.load("imagens_jogador/personagem_parado1.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 100)
        
        self.animar = False

    def andar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            #self.rect.move_ip(-20, 0)
        '''
        if pygame.key.get_pressed()[K_d]:
            self.rect.move_ip(2, 0)
        if pygame.key.get_pressed()[K_w]:
            self.rect.move_ip(0, -20)
        if pygame.key.get_pressed()[K_s]:
            self.rect.move_ip(0, 20)
        '''

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    




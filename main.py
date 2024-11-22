import pygame
import  sys
from pygame.locals import *

pygame.init()

LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Journey")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
            
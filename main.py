import pygame
import  sys
import random
from pygame.locals import *
from alien import Alien
from jogador import Jogador
from municaoDaNave import MunicaoDaNave
from colisao import Colisao
from configuracoes import Configuraoces as Config

pygame.init()

RODANDO = True

config = Config()
alien = Alien()
jogador = Jogador()
municao = MunicaoDaNave()
colisao = Colisao()


#Configurações de Tela
pygame.font.init()
#LARGURA = 1000
ALTURA = 720
TELA = pygame.display.set_mode((config.largura, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/estrelas.png").convert_alpha()
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (config.largura, ALTURA))
pygame.display.set_caption("Space Journey")



GATILHO = False

while RODANDO:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    TELA.blit(IMAGEM_FUNDO, (0, 0))

    #Criando movimento da tela de fundo
    rel_x = config.largura % IMAGEM_FUNDO.get_rect().width
    TELA.blit(IMAGEM_FUNDO, (rel_x - IMAGEM_FUNDO.get_rect().width, 0))
    if rel_x < 1280:
        TELA.blit(IMAGEM_FUNDO, (rel_x, 0))
    config.largura -= 0.1

    #Controles
    TECLA = pygame.key.get_pressed()
    if TECLA[K_w] and jogador.coordenadaY > 1:
        jogador.coordenadaY -= 5

        if not GATILHO:
            municao.coordenadaY -= 5

    if TECLA[K_s] and jogador.coordenadaY < ALTURA:
        jogador.coordenadaY += 5

        if not GATILHO:
            municao.coordenadaY += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        municao.velocidade = 8

    if colisao.pontuacao == -1:
        RODANDO = False
    #Respawn do Alien
    if alien.coordenadaX == 50:
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Respawn da Municao
    if municao.coordenadaX == 1000:
        municao.coordenadaX, municao.coordenadaY, GATILHO, municao.velocidade = municao.municaoRespawn(jogador)

    if alien.coordenadaX == 50 or colisao.colisao(jogador, alien, municao):
        alien.coordenadaX = alien.AlienRespawn()[0]
        alien.coordenadaY = alien.AlienRespawn()[1]

    #Posicao dos retangulos das imagens (Jogador, Alien, Municao)
    jogador.retanguloDaImagem.y = jogador.coordenadaY
    jogador.retanguloDaImagem.x = jogador.coordenadaX

    alien.retanguloDaImagem.y = alien.coordenadaY
    alien.retanguloDaImagem.x = alien.coordenadaX

    municao.retanguloDaImagem.y = municao.coordenadaY
    municao.retanguloDaImagem.x = municao.coordenadaX
        
    #Movimento do Alien
    config.largura -= 2
    alien.coordenadaX -= 0.7

    if colisao.pontuacao <= 5:
        alien.coordenadaX -= 0.3
    elif 10 <= colisao.pontuacao <= 13:
        alien.coordenadaX -= 1
    elif 14 <=colisao.pontuacao <= 16:
        alien.coordenadaX -= 2
    elif 17 <=colisao.pontuacao <= 18:
        alien.coordenadaX -= 2.5
    elif colisao.pontuacao >= 19:
        alien.coordenadaX -= 3
        

    #Movimento da Bala
    municao.coordenadaX += municao.velocidade

    TELA.blit(alien.imagem, (alien.coordenadaX, alien.coordenadaY))
    TELA.blit(municao.imagem, (municao.coordenadaX, municao.coordenadaY))
    TELA.blit(jogador.imagem, (jogador.coordenadaX, jogador.coordenadaY))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {colisao.pontuacao}", True, (255, 255, 255))

    TELA.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
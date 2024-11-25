import pygame
import  sys
import random
from pygame.locals import *

pygame.init()
pygame.font.init()

RODANDO = True

LARGURA = 1000
ALTURA = 667
TELA = pygame.display.set_mode((LARGURA, ALTURA))
IMAGEM_FUNDO = pygame.image.load("imagens/1.jpg").convert_alpha()
IMAGEM_FUNDO = pygame.transform.scale(IMAGEM_FUNDO, (LARGURA, ALTURA))

ALIEN_IMG = pygame.image.load("imagens/aircraft.png").convert_alpha()
ALIEN_IMG = pygame.transform.scale(ALIEN_IMG, (50, 50))
POSICAO_X_ALIEN = 500
POSICAO_Y_ALIEN = 300

JOGADOR_IMG = pygame.image.load("imagens/spaceship (1).png").convert_alpha()
JOGADOR_IMG = pygame.transform.scale(JOGADOR_IMG, (50, 50))
JOGADOR_IMG = pygame.transform.rotate(JOGADOR_IMG, -90)
POSICAO_X_JOGADOR = 200
POSICAO_Y_JOGADOR = 300


MUNICAO = pygame.image.load("imagens/bullet.png").convert_alpha()
MUNICAO = pygame.transform.scale(MUNICAO, (25, 25))


VELOCIDADE_X_MUNICAO = 0
POSICAO_X_MUNICAO = 200
POSICAO_Y_MUNICAO = 300

GATILHO = False

PONTOS = 2



#Definindo retângulo nas imagens para colisões
JOGADOR_IMG_RECT = JOGADOR_IMG.get_rect()
ALIEN_IMG_RECT = ALIEN_IMG.get_rect()
MUNICAO_RECT = MUNICAO.get_rect()

pygame.display.set_caption("Space Journey")

#Função que defini o respawn dos aliens
def respawn():
    x = 1350
    y = random.randint(1, 640)
    return [x, y]

#Função de respawn da Municao
def respawn_municao():
    GATILHO = False
    respawn_municao_x = POSICAO_X_JOGADOR
    respawn_municao_y = POSICAO_Y_JOGADOR
    velocidade_x_municao = 0
    return [respawn_municao_x, respawn_municao_y, GATILHO, velocidade_x_municao]

#Função de colisão
def colisao():
    global PONTOS

    if JOGADOR_IMG_RECT.colliderect(ALIEN_IMG_RECT) or ALIEN_IMG_RECT.x == 60:
        PONTOS -= 1
        return True
    elif MUNICAO_RECT.colliderect(ALIEN_IMG_RECT):
        PONTOS += 1
        return True
    else:
        return False


while RODANDO:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    TELA.blit(IMAGEM_FUNDO, (0, 0))

    #Criando movimento da tela de fundo
    rel_x = LARGURA % IMAGEM_FUNDO.get_rect().width
    TELA.blit(IMAGEM_FUNDO, (rel_x - IMAGEM_FUNDO.get_rect().width, 0))
    if rel_x < LARGURA:
        TELA.blit(IMAGEM_FUNDO, (rel_x, 0))
    LARGURA -= 2

    #Controles
    TECLA = pygame.key.get_pressed()
    if TECLA[K_w] and POSICAO_Y_JOGADOR > 1:
        POSICAO_Y_JOGADOR -= 5

        if not GATILHO:
            POSICAO_Y_MUNICAO -= 5

    if TECLA[K_s] and POSICAO_Y_JOGADOR < ALTURA:
        POSICAO_Y_JOGADOR += 5

        if not GATILHO:
            POSICAO_Y_MUNICAO += 5

    if TECLA[K_SPACE]:
        GATILHO = True
        VELOCIDADE_X_MUNICAO = 8

    if PONTOS == -1:
        RODANDO = False
    #Respawn do Alien
    if POSICAO_X_ALIEN == 50:
        POSICAO_X_ALIEN = respawn()[0]
        POSICAO_Y_ALIEN = respawn()[1]

    #Respawn da Municao
    if POSICAO_X_MUNICAO == 1000:
        POSICAO_X_MUNICAO, POSICAO_Y_MUNICAO, GATILHO, VELOCIDADE_X_MUNICAO = respawn_municao()

    if POSICAO_X_ALIEN == 50 or colisao():
        POSICAO_X_ALIEN = respawn()[0]
        POSICAO_Y_ALIEN = respawn()[1]

    #Posicao dos retangulos das imagens (Jogador, Alien, Municao)
    JOGADOR_IMG_RECT.y = POSICAO_Y_JOGADOR
    JOGADOR_IMG_RECT.x = POSICAO_X_JOGADOR

    ALIEN_IMG_RECT.y = POSICAO_Y_ALIEN
    ALIEN_IMG_RECT.x = POSICAO_X_ALIEN

    MUNICAO_RECT.y = POSICAO_Y_MUNICAO
    MUNICAO_RECT.x = POSICAO_X_MUNICAO
        
    #Movimento do Alien
    LARGURA -= 2
    POSICAO_X_ALIEN -= 1

    #Movimento da Bala
    POSICAO_X_MUNICAO += VELOCIDADE_X_MUNICAO

    pygame.draw.rect(TELA, (255,0, 0), JOGADOR_IMG_RECT, 4)
    pygame.draw.rect(TELA, (255,0, 0), MUNICAO_RECT, 4)
    pygame.draw.rect(TELA, (255,0, 0), ALIEN_IMG_RECT, 4)

    TELA.blit(ALIEN_IMG, (POSICAO_X_ALIEN, POSICAO_Y_ALIEN))
    TELA.blit(MUNICAO, (POSICAO_X_MUNICAO, POSICAO_Y_MUNICAO))
    TELA.blit(JOGADOR_IMG, (POSICAO_X_JOGADOR, POSICAO_Y_JOGADOR))

    FONTE = pygame.font.Font(None, 36) 
    PONTUACAO_TEXTO = FONTE.render(f"Pontos: {PONTOS}", True, (255, 255, 255))

    TELA.blit(PONTUACAO_TEXTO, (10, 10))

    pygame.display.update()
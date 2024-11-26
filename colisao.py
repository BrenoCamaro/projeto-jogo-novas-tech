class Colisao():
    def __init__(self):
        self.pontuacao = 1

    def colisao(self, jogador, alien, municao,):
        if jogador.retanguloDaImagem.colliderect(alien.retanguloDaImagem) or alien.retanguloDaImagem.x == 60:
            self.pontuacao -= 1
            return True
        elif municao.retanguloDaImagem.colliderect(alien.retanguloDaImagem):
            self.pontuacao += 1
            return True
        else:
            return False


from pygame.locals import *
import pygame
import sys
import os
import time
import random
import pygame.mixer

largura = 900
altura = 400
# Folders
folderImg = "img"
folderCenario = "img\Cenarios"
folderPersonagem = "img\Personagens"
folderPoderes = "img\Poderes"


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, name, life, energy,  posy, posx):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemInimigo = pygame.image.load(os.path.join(
        folderPersonagem+"\CapangaBIT", "bitParado.png"))

        self.rect.top = posy
        self.rect.left = posx
        self.velocidade = 20
    
    def colocar(self, screen):
        screen.blit(self.ImagemInimigo,self.rect)

class Rasengan(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite._init_(self)
        self.ImagemRasengan = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa", "superR1.png"))

        self.circle = self.ImagemRasengan.get_circle()
        self.velocidadeRasengan = 20
        self.circle.top = posy
        self.circle.left = posx

    def trajetoria(self):
        self.circle.top = self.circle.top - self.velocidadeRasengan

    def colocar(self,screen):
        screen.blit(self.ImagemRasengan,self.circle)
    
class Rafa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemRafa = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))

        self.rect = self.ImagemRafa.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura - 60

        self.listaRasengan = []
        self.vida = True
        self.velocidade = 10

    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__movimento()

    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__movimento()

    def __movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 900:
                self.rect.right = 900
    
    def disparar(self,x,y):
        meuRasengan = Rasengan(x,y)
        self.listaRasengan.append(meuRasengan)
    
    def colocar(self, screen):
        screen.blit(self.imagemRafa, self.rect)

def jogo():
    pygame.init()
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("As aventuras no mundo BIT")

    jogador = Rafa()
    Cenario = pygame.image.load(os.path.join(folderCenario, "floresta2.jpg"))
    jogando = True

    rasengan = Rasengan(largura/2, altura - 60)

    relogio = pygame.time.clock()

    while True:
        relogio.tick(50)
        rasengan.trajetoria()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == K_LEFT:
                    jogador.movimentoEsquerda()
                
                elif evento.key == K_RIGHT:
                    jogador.movimentoDireita()
                
                elif evento.key == K_SPACE:
                    x,y = jogador.rect.center
                    jogador.disparar(x,y)
        
        screen.blit(Cenario, (0,0))

        rasengan.colocar(screen)
        jogador.colocar(screen)

        if len(jogador.listaRasengan) > 0:
            for x in jogador.listaRasengan:
                x.colocar(screen)
                x.trajetoria()
                if x.rect.top < -10:
                    jogador.listaRasengan.remove(x)
        pygame.display.update()

jogo()
                



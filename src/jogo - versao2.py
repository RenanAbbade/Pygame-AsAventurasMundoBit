import pygame
import sys
import os
import time
import random
import pygame.mixer


from pygame.locals import*

# Classe criadora de personagens


class Personagem(object):
    def __init__(self, name, life, energy,  y, x):
        self.alive = True
        self.name = name
        self.life = life
        self.energy = energy
        self.x = x
        self.y = y
        self.velocidade = 40
        self.poderx = x+25
        self.podery = y


        

    def movimentacao(self, evento, cenario, lstMovimentos, enemyx):
        if evento == "carregar":
            screen.blit(lstMovimentos, (self.x, self.y))
            self.energy += 1
            print(self.energy)
               
            
        if evento == "pular":
            for i in range(len(lstMovimentos)):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos[i], (self.x, self.y))
                if i >= 2 and i < 4:
                    self.y += 170
                    self.x += 10
                    

                if i < 2:
                    self.y -= 170
                    self.x += 10
                  

              
                time.sleep(0.140)
       
        if evento == "direita":
             for i in range(len(lstMovimentos)):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos[i], (self.x, self.y))
                self.x += self.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if evento == "esquerda":
            for i in range(len(lstMovimentos)):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos[i], (self.x, self.y))
                self.x -= self.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if evento == "ataque":
            if self.energy > 50:
                for i in range(len(lstMovimentos)):       
                        if i <=2:
                            screen.blit(cenario, (0, 0))
                            screen.blit(lstMovimentos[i], (self.x, self.y))
                            time.sleep(0.1)
                            pygame.display.update()
                            pygame.display.flip()
                        if i >2: #display_width = 1199
                            while self.poderx < 1199:
                                screen.blit(cenario, (0, 0))
                                screen.blit(lstMovimentos[2],(self.x, self.y))
                                screen.blit(lstMovimentos[i], (self.poderx, self.podery))
                                self.poderx +=30
                                time.sleep(0.025)
                                pygame.display.update()
                                pygame.display.flip()
                self.energy -= 50
                self.poderx = self.x+25
            else: 
                print("Sem energia")
            print(self.energy)

        if evento == "superAtaque":
            if self.energy > 150:
                self.podery = 0
                self.poderx = enemyx
                for i in range(len(lstMovimentos)):       
                        if i <=2:
                            screen.blit(cenario, (0, 0))
                            screen.blit(lstMovimentos[i], (self.x, self.y))
                            time.sleep(0.1)
                            pygame.display.update()
                            pygame.display.flip()
                        if i >2: #display_height = 656
                            while self.podery < 656:
                                screen.blit(cenario, (0, 0))
                                screen.blit(lstMovimentos[2],(self.x, self.y))
                                screen.blit(lstMovimentos[i], (self.poderx, self.podery))
                                self.podery +=10
                                pygame.display.update()
                                pygame.display.flip()
                self.energy -= 150
                self.poderx = self.x+25
                self.podery = self.y
            else: 
                print(self.name," Sem energia")
            print(self.name, " has", self.energy)


    def hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

    def entraTela(self):
        if self.life == True:
            if self.x <= 0:
                self.x = 0
            if self.x >= 1199:
                self.x = 1199



class Inimigo(object):
    def __init__(self, name, life, energy, v, y, x):
        self.alive = True
        self.name = name
        self.life = life
        self.energy = energy
        self.x = x
        self.y = y
        self.velocidade = v
        self.poderx = x-25
        self.podery = y
    
    def escolheMov(self,Movimentos):
        mov = random.randint(0,len(Movimentos))
        return mov

    def movimentacao(self, evento, cenario, lstMovimentos, enemyx):
        if evento == "carregar":
            screen.blit(lstMovimentos, (self.x, self.y))
            self.energy += 1
            print(self.energy)
            pygame.display.update()
            pygame.display.flip()      
            
        if evento == "pular":
            for i in range(4):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos, (self.x, self.y))
                if i >= 2 and i < 4:
                    self.y += 170
                 
                    pygame.display.update()
                    pygame.display.flip()
                if i < 2:
                    self.y -= 170
                    pygame.display.update()
                    pygame.display.flip()

                pygame.display.update()
                pygame.display.flip()
                time.sleep(0.140)
       
        if evento == "direita":
             for i in range(len(lstMovimentos)):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos[i], (self.x, self.y))
                self.x += self.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if evento == "esquerda":
            for i in range(len(lstMovimentos)):
                screen.blit(cenario, (0, 0))
                screen.blit(lstMovimentos[i], (self.x, self.y))
                self.x -= self.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if evento == "ataque":
            if self.energy > 50:
                for i in range(1,len(lstMovimentos)):       
                        while self.poderx > 0:
                            screen.blit(cenario, (0, 0))
                            screen.blit(lstMovimentos[0],(self.x, self.y))
                            screen.blit(lstMovimentos[i], (self.poderx, self.podery))
                            self.poderx -=30
                            time.sleep(0.025)
                            pygame.display.update()
                            pygame.display.flip()
                self.energy -= 50
                self.poderx = self.x-25
            else: 
                print(self.name," Sem energia")
            print(self.name, " has", self.energy)

        if evento == "superAtaque":
            if self.energy > 150:
                self.podery = 0
                self.poderx = enemyx
                for i in range(len(lstMovimentos)):       
                        if i <=2:
                            screen.blit(cenario, (0, 0))
                            screen.blit(lstMovimentos[i], (self.x, self.y))
                            time.sleep(0.1)
                            pygame.display.update()
                            pygame.display.flip()
                        if i >2: #display_height = 656
                            while self.podery < 656:
                                screen.blit(cenario, (0, 0))
                                screen.blit(lstMovimentos[2],(self.x, self.y))
                                screen.blit(lstMovimentos[i], (self.poderx, self.podery))
                                self.podery +=10
                                pygame.display.update()
                                pygame.display.flip()
                self.energy -= 150
                self.poderx = self.x+25
                self.podery = self.y
            else: 
                print("Sem energia")
            print(self.energy)


    def hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

    def entraTela(self):
        if self.life == True:
            if self.x <= 0:
                self.x = 0
            if self.x >= 1199:
                self.x = 1199


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("mistral", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

# Sair do jogo


def quitgame():
    pygame.quit()
    quit()

# creditos


def creditos():

    creditos = pygame.image.load(os.path.join(folderImg, "CREDITOS.png"))
    screen.blit(creditos, (0, 0))

# instruções


def inst():

    ins = pygame.image.load(os.path.join(folderImg, "instr.png"))
    screen.blit(ins, (0, 0))


'''
def gameover(scorefinal):
    largura = 847
    altura = 596

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption(" - Naruto: Final Shuriken -")
    relogio = pygame.time.Clock()
    screen.fill((255, 255, 255))
    # Musicas e img
    folderImg = "img"
    # Naruto
    gameOver = pygame.image.load(os.path.join(folderImg,"gameover.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render(
        "-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(white))
    aviso = smallText.render(
        "*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(white))
    perdedor = True
    pygame.mixer.pre_init()
    pygame.mixer.music.load('gameOver.ogg')
    pygame.mixer.music.play(-1)
    while perdedor != False:
        time.sleep(1)
        screen.blit(gameOver,(0,0))
        screen.blit(ranque,(150,500))
        screen.blit(aviso,(100,530))
        for event in pygame.event.get():
                pygame.display.update()
                pygame.display.flip()
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ranking(scorefinal)
                        perdedor = True


def venceu(scorefinal):

    largura = 847
    altura = 596

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption(" - Naruto: Final Shuriken -")
    relogio = pygame.time.Clock()
    screen.fill((255, 255, 255))
    # Musicas e img
    folderImg = "img"
    # Naruto
    youwin = pygame.image.load(os.path.join(folderImg,"youwin.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render(
        "-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(black))
    aviso = smallText.render(
        "*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(black))
    vencedor = True
    pygame.mixer.pre_init()
    pygame.mixer.music.load('gameWin.ogg')
    pygame.mixer.music.play(-1)
    while vencedor != False:
        time.sleep(1)
        screen.blit(youwin,(0,0))
        screen.blit(ranque,(150,500))
        screen.blit(aviso,(100,530))
        for event in pygame.event.get():
                pygame.display.update()
                pygame.display.flip()
                if event.type ==  pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ranking(scorefinal)
                        vencedor = False
'''
# menu


def tocarMusica(nomeMusica):
    pygame.mixer.pre_init()
    pygame.mixer.music.load(nomeMusica)
    pygame.mixer.music.play(-1)


def game_intro():

    intro = True
    folderImg = "img"
    menu = pygame.image.load(os.path.join(folderImg, "CAPA.PNG"))
    # Rodar música do menu
    tocarMusica('op.ogg')
    while intro == True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # colocar imagem do menu
        screen.blit(menu, (0, 0))
        button("JOGO", 600, 540, 50, 50, white, bright_rasen, jogo)
        button("CRÉDITOS", 0, 560, 100, 50, Aqua, white, creditos)
        button("INSTRUÇÕES", 0, 510, 100, 50, LightSkyBlue, white, inst)
        button("SAIR", 0, 610, 100, 50, DeepSkyBlue, bright_red, quitgame)
        pygame.display.update()
        clock.tick(15)


def jogo():
    #variaveis de controle
    jogando = True
    fase1 = True
    # Inicializando a musica da fase
    tocarMusica('combate1.ogg')
    #Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "PARADO.png"))

    capangaParado = pygame.image.load(os.path.join(folderPersonagem+"\CapangaBIT", "bitParado.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20)
    soldadoBIT = Inimigo("soldado1",100,1000,5,400,900)

    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta2.jpg"))
    
    cont = 0

    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(capangaParado, (soldadoBIT.x,soldadoBIT.y))

        for event in pygame.event.get():
            pygame.display.update()
            pygame.display.flip()

            # Animação andar para frente
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
    

                if event.key == K_UP:
                    pulando1 = pygame.image.load(os.path.join(
                    folderPersonagem+"\RAFA", "pulo1.png"))
                    # settando imgs
                    pulando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    pulando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    pulando4 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo4.png"))
                    pulando5 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo5.png"))
                    pulando = [pulando1, pulando2,
                        pulando3, pulando4, pulando5]
                    # chamando function
                    Rafa.movimentacao("pular", cenario1, pulando,0)
                #ataque
                if event.key == K_SPACE:
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3, rasengan1, rasengan2, rasengan3]
                    # chamando function
                    Rafa.movimentacao("ataque", cenario1, atacando,0)

                #superAtaque 
                
                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    Rafa.movimentacao("superAtaque", cenario1, atacando, soldadoBIT.x )
                
                    
        if tecla[K_DOWN]:
            carregando = pygame.image.load(os.path.join(
            folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.movimentacao("carregar",cenario1,carregando,0)
                # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            Rafa.movimentacao("direita",cenario1,correndo,0)
           
        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            correndoEsquerda1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            Rafa.movimentacao("esquerda",cenario1,correndo,0)
        MovSoldadoBit = ["ataque","pular"]
        escolhaMov = soldadoBIT.escolheMov(MovSoldadoBit)
        if escolhaMov == 0:
            capangaAtaque = pygame.image.load(os.path.join(folderPersonagem+"\CapangaBIT", "bitAtacando.png"))
            capangaRas1 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras1.png"))
            capangaRas2 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras2.png"))
            capangaRas3 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras3.png"))
            capagangaOf = [capangaAtaque, capangaRas1,capangaRas2,capangaRas3 ]      
            soldadoBIT.movimentacao("ataque", cenario1,capagangaOf, Rafa.x)
        if escolhaMov == 1:
            capangaParado = pygame.image.load(os.path.join(folderPersonagem+"\CapangaBIT", "bitParado.png"))
            soldadoBIT.movimentacao("pular", cenario1, capangaParado, Rafa.x)

            

        
        #Soldado BIT ATAQUES
        MovSoldadoBit = ["ataque","pular"]
        escolhaMov = soldadoBIT.escolheMov(MovSoldadoBit)
        if escolhaMov == 0:
            capangaAtaque = pygame.image.load(os.path.join(folderPersonagem+"\CapangaBIT", "bitAtacando.png"))
            capangaRas1 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras1.png"))
            capangaRas2 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras2.png"))
            capangaRas3 = pygame.image.load(os.path.join(folderPoderes+"\RasenganPoder", "ras3.png"))
            capagangaOf = [capangaAtaque, capangaRas1,capangaRas2,capangaRas3 ]      
            soldadoBIT.movimentacao("ataque", cenario1,capagangaOf, Rafa.x)
        if escolhaMov == 1:
            capangaParado = pygame.image.load(os.path.join(folderPersonagem+"\CapangaBIT", "bitParado.png"))
            soldadoBIT.movimentacao("pular", cenario1, capangaParado, Rafa.x)
            
    
  
        pygame.display.flip()
        pygame.display.update()



pygame.init()

display_width = 1199
display_height = 656

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
rasen = (240, 255, 255)
bright_red = (255, 255, 255)
bright_rasen = (224, 255, 255)
DeepSkyBlue = (0, 191, 255)
LightSkyBlue = (135, 206, 250)
SkyBlue = (135, 206, 235)
block_color = (53, 115, 255)
Aqua = (0, 255, 255)

#Folders
folderImg = "img"
folderCenario = "img\Cenarios"
folderPersonagem = "img\Personagens"
folderPoderes = "img\Poderes"

#Screen
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(' As Aventuras do Mundo Bit ')
clock = pygame.time.Clock()

game_intro()

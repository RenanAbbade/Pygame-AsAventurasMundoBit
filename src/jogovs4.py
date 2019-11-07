import pygame
import sys
import os
import time
import random
import pygame.mixer


from pygame.locals import*

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



# Folders
folderImg = "img"
folderLicoes = "img\Licoes"
folderCenario = "img\Cenarios"
folderPersonagem = "img\Personagens"
folderPoderes = "img\Poderes"

# Screen
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption(' As Aventuras do Mundo Bit ')
clock = pygame.time.Clock()

score = 0



# Classe criadora de personagens


class Personagem(object):
    def __init__(self, name, life, energy,  y, x, score):
        self.alive = True
        self.name = name
        self.life = life
        self.energy = energy
        self.x = x
        self.y = y
        self.velocidade = 40
        self.poderx = x+25
        self.podery = y
        self.score = score
   

    def carregar(self):
        self.energy += 1
        if self.energy >= 300:
            self.energy = 300


    def aumentaScore(self, aumento):
        self.score += aumento
    
    def pontuacao(self):
        font = pygame.font.SysFont(None, 20)
        pygame.font.init()
        font_padrao = pygame.font.get_default_font()
        tempo = pygame.time.get_ticks()/1000

        text = font.render(str(self.score), True, (255,255,255))
        screen.blit(text, [150, 580])
        temp = font.render(str("{0:.0f}".format(tempo)), True, (255,255,255))
        screen.blit(temp, [10, 580])
        pont = font.render("Pontuação:", True, (255,255,255))
        screen.blit(pont, [50, 580])


    def hit(self, damage):
        self.life -= damage
        self.score -= 50
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

    def  energiaLogo(self):
        energialogo = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","energia.png"))
        if self.energy == 300:
            screen.blit(energialogo,(0,10))
            screen.blit(energialogo,(65,10))
            screen.blit(energialogo,(135,10))
        elif self.energy >= 200 and self.energy < 300:
            screen.blit(energialogo,(0,10))
            screen.blit(energialogo,(65,10))
        elif self.energy >= 100 and self.energy < 200:
            screen.blit(energialogo,(0,10))
        
            
        
        



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

    def escolheMov(self, Movimentos):
        mov = random.randint(0, len(Movimentos))
        return mov


    def entraTela(self):
        if self.life == True:
            if self.x <= 0:
                self.x = 0
            if self.x >= 1199:
                self.x = 1199

    def hit(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.explode()
            #Se verdadeiro, oponente foi derrotado
            return True
        return False
        

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")



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
lista = []


def ranking(scorefinal):
    global lista
    pygame.init()
    pygame.font.init()
    posição = 1
    screen = pygame.display.set_mode((1199,656))
    smallText = pygame.font.SysFont("mistral",30)
    folder = 'img'
    fundo = pygame.image.load(os.path.join(folder,"RANKING.PNG"))
    screen.blit(fundo,(0,0))
    lista.append(scorefinal)
    lista.sort(reverse=True)

    novamente = smallText.render("-APERTE A TECLA DE ESPAÇO PARA TENTAR MAIS UMA VEZ!-",1,(white))
    sair = smallText.render("-PARA SAIR APERTE A TECLA X-",1,(white))
    y = 300
    x = 0
    i = 0
    print(" - Pontuação - ")
   
    print("pontuação FOI",scorefinal)
    
    for i in lista:
        if posição == 11:
            break
        posicao = str(posição) + "-   "  + str(i) + "  PONTOS"
        rank = smallText.render(posicao,1,(black))
        screen.blit(rank,(320,y))
        y += 20
        posição += 1
        opcao = True
    while opcao == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()
                    
                if event.key == pygame.K_x:
                    pygame.quit()
                    quit()
        
       
                pygame.quit()
                sys.exit() 
    
        screen.blit(novamente,(150,480))
        screen.blit(sair,(180,520))
        pygame.display.update()
    

def quitgame():
    pygame.quit()
    quit()

# creditos


def creditos():

    creditos = pygame.image.load(os.path.join(folderImg, "CREDITOS.png"))
    screen.blit(creditos, (0, 0))

# instruções
def licoes(fase):
    if fase == "Fase1":
        licao1 = pygame.image.load(os.path.join(folderLicoes, "licao1.png"))
        screen.blit(licao1, (display_width/2, 10))
    if fase == "Fase2":
        licao2 = pygame.image.load(os.path.join(folderLicoes, "licao2.png"))
        screen.blit(licao2, (display_width/2, 10))
    if fase == "Fase3":
        licao2 = pygame.image.load(os.path.join(folderLicoes, "licao3.png"))
        screen.blit(licao2, (display_width/2, 10))
    if fase == "Fase4":
        licao2 = pygame.image.load(os.path.join(folderLicoes, "licao4-5.png"))
        screen.blit(licao2, (display_width/2, 10))
    if fase == "Fase5":
        licao2 = pygame.image.load(os.path.join(folderLicoes, "licao4-5.png"))
        screen.blit(licao2, (display_width/2, 10))

    

def inst():

    ins = pygame.image.load(os.path.join(folderImg, "instr.png"))
    screen.blit(ins, (0, 0))

def vitoria(score):
    trocaFase = pygame.image.load(os.path.join(folderImg, "youWin.png"))
    screen.blit(trocaFase, (0, 0))
    time.sleep(10)

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
    tocarMusica('combate1.ogg')
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
    fase1()

def fase1():
    fase = "Fase1"
    
    # variaveis de controle
    jogando = True
    # Inicializando a musica da fase
    
    # Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))

    RasenColision1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision10.png"))

    inimigoParado = pygame.image.load(os.path.join(
        folderPersonagem+"\CapangaBIT", "bitParado.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20, 200)
    inimigo = Inimigo("soldado1", 200, 1000, 5, 400, 900)


    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta2.jpg"))

    cont = 0

    while jogando:
        relogio.tick(100)
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        Rafa.energiaLogo()
        licoes(fase)
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
        Rafa.pontuacao()
    

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
                    for i in range(len(pulando)):
                        screen.blit(cenario1,(0, 0))
                        Rafa.pontuacao()
                        Rafa.energiaLogo()
                        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                        screen.blit(pulando[i], (Rafa.x, Rafa.y))
                        if i >= 2 and i < 4:
                            Rafa.y += 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        if i < 2:
                            Rafa.y -= 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
                        # ataque
                if event.key == K_SPACE:
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3,
                                rasengan1, rasengan2, rasengan3]
                    # chamando function
                    colidiu = False
                    Rafa.aumentaScore(100)
                    if Rafa.energy > 100:
                        Rafa.energy -= 100
                        for i in range(len(atacando)):
                            screen.blit(cenario1, (0, 0))
                            Rafa.pontuacao()
                            Rafa.energiaLogo()
                            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.pontuacao()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_width = 1199
                                while Rafa.poderx < display_width:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.pontuacao()
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (Rafa.poderx, Rafa.podery))
                                    Rafa.poderx += 30
                                    #COLISION
                                    if (Rafa.poderx - inimigo.x) > -50 and (Rafa.poderx - inimigo.x)<90 and (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.pontuacao()
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        time.sleep(0.1)
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(100) == True:
                                            
                                            fase2(Rafa.score)
                                            break
                                        
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()

                    else:
                        print("Sem energia")
                    print(Rafa.energy)


                # superAtaque

                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    colidiu = False
                    Rafa.aumentaScore(120)
                    if  Rafa.energy > 200:
                        Rafa.energy -= 200
                        Rafa.podery = 0
                        Rafa.poderx = enemyx
                        for i in range(len(atacando)):
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.energiaLogo()
                                Rafa.pontuacao()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_height = 656
                                while Rafa.podery < display_height:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (inimigo.x, Rafa.podery))
                                    Rafa.podery += 20
                                    pygame.display.update()
                                    pygame.display.flip()
                                    #COLISION
                                    if (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            Rafa.pontuacao()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        time.sleep(0.1)
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(150) == True:
                                            trocaFase()
                                            fase2(Rafa.score)
                                            break
                                        
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                        
                        Rafa.poderx = Rafa.x+25
                        Rafa.podery = Rafa.y
                    else:
                        print(Rafa.name, " Sem energia")
                    print(Rafa.name, " has", Rafa.energy)

        if tecla[K_DOWN]:
            carregando = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.energiaLogo()
            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
            screen.blit(carregando, (Rafa.x, Rafa.y))
            Rafa.carregar()
            print(Rafa.energy)
            pygame.display.update()
            pygame.display.flip()
            # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x += Rafa.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            correndoEsquerda1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x -= Rafa.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        # Soldado BIT ATAQUES
   

        pygame.display.flip()
        pygame.display.update()






def fase2(score):

    fase = "Fase2"
       # variaveis de controle
    jogando = True
    # Inicializando a musica da fase
    
    # Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))

    RasenColision1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision10.png"))

    inimigoParado = pygame.image.load(os.path.join(
        folderPersonagem+"\CapangaBIT", "bitAtacando.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20, score)
    inimigo = Inimigo("soldado1", 200, 1000, 5, 100, 700)

    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta2.jpg"))

    cont = 0

    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        licoes(fase)
        Rafa.energiaLogo()
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
        Rafa.pontuacao()
       
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
                    for i in range(len(pulando)):
                        screen.blit(cenario1,(0, 0))
                        Rafa.energiaLogo()
                        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                        screen.blit(pulando[i], (Rafa.x, Rafa.y))
                        Rafa.pontuacao()
                        if i >= 2 and i < 4:
                            Rafa.y += 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        if i < 2:
                            Rafa.y -= 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
                        # ataque
                if event.key == K_SPACE:
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3,
                                rasengan1, rasengan2, rasengan3]
                    Rafa.aumentaScore(-100)
                    # chamando function
                    colidiu = False
                    if Rafa.energy > 100:
                        Rafa.energy -= 100
                        for i in range(len(atacando)):
                            screen.blit(cenario1, (0, 0))
                            Rafa.energiaLogo()
                            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                            Rafa.pontuacao()
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_width = 1199
                                while Rafa.poderx < display_width:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (Rafa.poderx, Rafa.podery))
                                    Rafa.pontuacao()
                                    Rafa.poderx += 30
                                    #COLISION
                                    if (Rafa.poderx - inimigo.x) > -50 and (Rafa.poderx - inimigo.x)<90 and (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            inimigo.hit(100, inimigo)
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        Rafa.poderx = Rafa.x+25
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                                   
                        
                  
                    else:
                        print("Sem energia")
                    print(Rafa.energy)


                # superAtaque

                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    Rafa.aumentaScore(200)
                    colidiu = False
                    if  Rafa.energy > 200:
                        Rafa.energy -= 200
                        Rafa.podery = 0
                        Rafa.poderx = enemyx
                        for i in range(len(atacando)):
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.energiaLogo()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                Rafa.pontuacao()
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_height = 656
                                while Rafa.podery < display_height:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (inimigo.x, Rafa.podery))
                                    Rafa.podery += 20
                                    Rafa.pontuacao()
                                    pygame.display.update()
                                    pygame.display.flip()
                                    #COLISION
                                    if (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        time.sleep(0.1)
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(150) == True:
                                            fase3(Rafa.score)
                                            break
                                        
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                        
                        Rafa.poderx = Rafa.x+25
                        Rafa.podery = Rafa.y
                    else:
                        print(Rafa.name, " Sem energia")
                    print(Rafa.name, " has", Rafa.energy)



        if tecla[K_DOWN]:
            carregando = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.energiaLogo()
            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
            screen.blit(carregando, (Rafa.x, Rafa.y))
            Rafa.carregar()
            print(Rafa.energy)
            pygame.display.update()
            pygame.display.flip()
            # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.pontuacao()
                Rafa.x += Rafa.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            correndoEsquerda1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.pontuacao()
                Rafa.x -= Rafa.velocidade
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        # Soldado BIT ATAQUES 
   

        pygame.display.flip()
        pygame.display.update()

def fase4(score):
    fase = "Fase4"
    jogando = True
    # Inicializando a musica da fase
    
    # Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))

    RasenColision1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision10.png"))

    inimigoParado = pygame.image.load(os.path.join(
        folderPersonagem+"\Joaquino", "JoaquinoParado.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20, score)
    inimigo = Inimigo("inimigo", 400, 500,5,300,800)
    portalJoaquino = pygame.image.load(os.path.join(folderPoderes+"\PoderJoaquino","portal.png"))#x600 y350
    xj = 400
    yj = 200
    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta3.jpg"))

    cont = 0

    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        licoes(fase)
        Rafa.energiaLogo()
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
        screen.blit(portalJoaquino, (xj, yj))
        Rafa.pontuacao()
       
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
                    for i in range(len(pulando)):
                        screen.blit(cenario1,(0, 0))
                        Rafa.energiaLogo()
                        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                        screen.blit(pulando[i], (Rafa.x, Rafa.y))
                        Rafa.pontuacao()
                        if i >= 2 and i < 4:
                            Rafa.y += 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        if i < 2:
                            Rafa.y -= 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
                        # ataque
                if event.key == K_SPACE:
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3,
                                rasengan1, rasengan2, rasengan3]
                    
                    # chamando function
                    colidiu = False
                    Rafa.aumentaScore(-350)
                    if Rafa.energy > 100:
                        Rafa.energy -= 100
                        for i in range(len(atacando)):
                            screen.blit(cenario1, (0, 0))
                            Rafa.energiaLogo()
                            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                            screen.blit(portalJoaquino, (xj, yj))
                            Rafa.pontuacao()
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                screen.blit(portalJoaquino, (xj, yj))
                                Rafa.pontuacao()
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_width = 1199
                                while Rafa.poderx < display_width:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(portalJoaquino, (xj, yj))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (Rafa.poderx, Rafa.podery))
                                    Rafa.pontuacao()
                                    Rafa.poderx += 30
                                    #COLISION
                                    print(Rafa.poderx, xj)
                                    if Rafa.poderx  >= 600 :
                                        while Rafa.poderx > 0:
                                            screen.blit(rasengan3, (Rafa.poderx, Rafa.podery))
                                            Rafa.poderx -= 50
                                            time.sleep(0.1)
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            pygame.display.flip()
                                            if Rafa.poderx < (Rafa.x - 20):
                                                print("Colidiu")
                                                
                                                colidiu = True
                                                RafaAtacado = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "atacado.png"))
                                                Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                                for c in range(12):
                                                    screen.blit(cenario1, (0, 0))
                                                    screen.blit(RafaAtacado, (Rafa.x, Rafa.y))
                                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                                    screen.blit(Rasencol[c], (Rafa.x, Rafa.y))
                                                    Rafa.hit(50)
                                                    Rafa.pontuacao()
                                                    pygame.display.update()
                                                    time.sleep(0.1)
                                                break
                                    
                                        
                                    if (Rafa.poderx - inimigo.x) > -50 and (Rafa.poderx - inimigo.x)<90 and (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(100) == True:
                                            fase2(Rafa.score)
                                            break
                                        break
                                   
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                                   
                        
                  
                    else:
                        print("Sem energia")
                    print(Rafa.energy)


                # superAtaque

                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    colidiu = False
                    Rafa.aumentaScore(450)
                    if  Rafa.energy > 200:
                        Rafa.energy -= 200
                        Rafa.podery = 0
                        Rafa.poderx = enemyx
                        for i in range(len(atacando)):
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.energiaLogo()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                Rafa.pontuacao()
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_height = 656
                                while Rafa.podery < display_height:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (inimigo.x, Rafa.podery))
                                    Rafa.podery += 20
                                    Rafa.pontuacao()
                                    pygame.display.update()
                                    pygame.display.flip()
                                    #COLISION
                                    if (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        colidiu = True
                                        
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        time.sleep(0.1)
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(150) == True:
                                            fase5(Rafa.score)
                                            break
                                        
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                        
                        Rafa.poderx = Rafa.x+25
                        Rafa.podery = Rafa.y
                    else:
                        print(Rafa.name, " Sem energia")
                    print(Rafa.name, " has", Rafa.energy)



        if tecla[K_DOWN]:
            carregando = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.energiaLogo()
            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
            screen.blit(carregando, (Rafa.x, Rafa.y))
            Rafa.carregar()
            print(Rafa.energy)
            pygame.display.update()
            pygame.display.flip()
            # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x += Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            correndoEsquerda1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x -= Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        # Soldado BIT ATAQUES

        pygame.display.flip()
        pygame.display.update()




def fase5(score):
    fase = "Fase5"
    jogando = True
    # Inicializando a musica da fase
    
    # Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))

    

    RasenColision1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision10.png"))

    inimigoParado = pygame.image.load(os.path.join(
        folderPersonagem+"\Joaquino", "JoaquinoParado.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20, score)
    inimigo = Inimigo("inimigo", 400, 500,5,300,800)
    portalJoaquino = pygame.image.load(os.path.join(folderPoderes+"\PoderJoaquino","portal.png"))#x600 y350
    xj = 550
    yj = 50
    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta3.jpg"))

    cont = 0

    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        licoes(fase)
        Rafa.energiaLogo()
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
        screen.blit(portalJoaquino, (xj, yj))
        Rafa.pontuacao()
     
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
                    for i in range(len(pulando)):
                        screen.blit(cenario1,(0, 0))
                        Rafa.energiaLogo()
                        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                        screen.blit(pulando[i], (Rafa.x, Rafa.y))
                        Rafa.pontuacao()
                        if i >= 2 and i < 4:
                            Rafa.y += 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        if i < 2:
                            Rafa.y -= 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
                        # ataque
                if event.key == K_SPACE:
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3,
                                rasengan1, rasengan2, rasengan3]
                    # chamando function
                    colidiu = False
                    
                    Rafa.aumentaScore(850)
                    if Rafa.energy > 100:
                        Rafa.energy -= 100
                        for i in range(len(atacando)):
                            screen.blit(cenario1, (0, 0))
                            Rafa.energiaLogo()
                            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                            screen.blit(portalJoaquino, (xj, yj))
                            Rafa.pontuacao()
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                screen.blit(portalJoaquino, (xj, yj))
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_width = 1199
                                while Rafa.poderx < display_width:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(portalJoaquino, (xj, yj))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (Rafa.poderx, Rafa.podery))
                                    Rafa.pontuacao()
                                    Rafa.poderx += 30
                                    #COLISION
                                    print(Rafa.poderx, xj)
                                        
                                    if Rafa.poderx >= inimigo.x:
                                        
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)

                                        if  colidiu == True:
                                            Rafa.poderx = Rafa.x+25
                                            if inimigo.hit(100) == True:
                                                fundo = pygame.image.load(os.path.join(folderImg,"youWin.jpg"))
                                                screen.blit(fundo,(0,0))
                                                time.sleep(0.5)
                                                ranking(score)
                                                
                                                break
                                            break
                                        break
                                    
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                                   
                        
                  
                    else:
                        print("Sem energia")
                    print(Rafa.energy)


                # superAtaque

                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    colidiu = False
                    Rafa.aumentaScore(-550)
                    if  Rafa.energy > 200:
                        Rafa.energy -= 200
                        Rafa.podery = 0
                        Rafa.poderx = enemyx
                        for i in range(len(atacando)):
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.energiaLogo()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                time.sleep(0.1)
                                Rafa.pontuacao()
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_height = 656
                                while Rafa.podery < display_height:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(portalJoaquino, (xj, yj))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (inimigo.x, Rafa.podery))
                                    screen.blit(atacando[i], (Rafa.x, Rafa.podery))
                                    Rafa.pontuacao()
                                    Rafa.podery += 20
                                    pygame.display.update()
                                    pygame.display.flip()
                                    #COLISION
                                    if Rafa.podery  >= 150 :
                                            
                                            Rafa.poderx = Rafa.x 
                                            time.sleep(0.1)
                                            screen.blit(atacando[i], (Rafa.x, Rafa.podery))
                                            Rafa.podery += 20
                                            Rafa.pontuacao()
                                            time.sleep(0.1)
                                            pygame.display.update()
                                            pygame.display.flip()
                                            if Rafa.podery >= Rafa.y + 20:
                                                print("Colidiu")
                                                colidiu = True
                                                RafaAtacado = pygame.image.load(os.path.join(folderPersonagem+"\RAFA", "atacado.png"))
                                                Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                                for c in range(12):
                                                    screen.blit(cenario1, (0, 0))
                                                    screen.blit(RafaAtacado, (Rafa.x, Rafa.y))
                                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                                    screen.blit(portalJoaquino, (xj, yj))
                                                    screen.blit(Rasencol[c], (Rafa.x, Rafa.y))
                                                    Rafa.hit(100)
                                                    Rafa.pontuacao()
                                                    pygame.display.update()
                                                    time.sleep(0.1)
                                                break
                                            break
                        
                        Rafa.poderx = Rafa.x+25
                        Rafa.podery = Rafa.y
                    else:
                        print(Rafa.name, " Sem energia")
                    print(Rafa.name, " has", Rafa.energy)



        if tecla[K_DOWN]:
            carregando = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.energiaLogo()
            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
            screen.blit(carregando, (Rafa.x, Rafa.y))
            Rafa.carregar()
            print(Rafa.energy)
            pygame.display.update()
            pygame.display.flip()
            # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x += Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            correndoEsquerda1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                Rafa.x -= Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        # Soldado BIT ATAQUES

        pygame.display.flip()
        pygame.display.update()


def fase3(score):
    fase = "Fase3"
    jogando = True
    # Inicializando a musica da fase
    
    # Iniciando contagem
    relogio = pygame.time.Clock()
    # Criando o personagem principal e settando seus moves
    RafaParado = pygame.image.load(os.path.join(
        folderPersonagem+"\RAFA", "PARADO.png"))


    RasenColision1 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision1.png"))
    RasenColision2 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision2.png"))
    RasenColision3 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3.png"))
    RasenColision4 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision3-4.png"))
    RasenColision5 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision4-5 1.png"))
    RasenColision6 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5.png"))
    RasenColision7 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision5-6.png"))
    RasenColision8 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision6.png"))
    RasenColision9 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision7.png"))
    RasenColision10 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision8.png"))
    RasenColision11 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision9.png"))
    RasenColision12 = pygame.image.load(os.path.join(folderPoderes+"\PoderRafa","Rasengancolision10.png"))

    inimigoParado = pygame.image.load(os.path.join(
        folderPersonagem+"\Matias", "MATIAS.png"))

    Rafa = Personagem("Rafa", 200, 100, 400, 20, score)
    inimigo = Inimigo("inimigo", 600, 500,5,300,800)
    
    capangaRas3 = pygame.image.load(os.path.join(
                folderPoderes+"\RasenganPoder", "ras3.png"))#x600 y350
    xj = 550
    yj = 50
    cenario1 = pygame.image.load(os.path.join(folderCenario, "floresta.jpg"))

    cont = 0

    inimigoAtaque = False

    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0, 0))
        licoes(fase)
        Rafa.energiaLogo()
        screen.blit(RafaParado, (Rafa.x, Rafa.y))
        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
        screen.blit(capangaRas3, (xj,yj))
        
        Rafa.pontuacao()
        
 
        
   
        #inimigo.movimentacao("ataque", cenario1, capagangaOf, Rafa.x)
        
       

        for event in pygame.event.get():
            
            pygame.display.update()
            pygame.display.flip()

            # Animação andar para frente
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                

                if event.key == K_UP:
                    inimigoAtaque = True
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
                    for i in range(len(pulando)):
                        screen.blit(cenario1,(0, 0))
                        Rafa.energiaLogo()
                        screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                        screen.blit(pulando[i], (Rafa.x, Rafa.y))
                        Rafa.pontuacao()
                        if i >= 2 and i < 4:
                            Rafa.y += 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        if i < 2:
                            Rafa.y -= 170
                            Rafa.x += 10
                            pygame.display.update()
                            pygame.display.flip()

                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
                        # ataque
                if event.key == K_SPACE:
                    inimigoAtaque = True
                    # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "atacando3.png"))
                    rasengan1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan1.png"))
                    rasengan2 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan2.png"))
                    rasengan3 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "rasengan3.png"))
                    atacando = [atacando1, atacando2, atacando3,
                                rasengan1, rasengan2, rasengan3]
                    # chamando function
                    colidiu = False
                    Rafa.aumentaScore(850)
                    if Rafa.energy > 100:
                        Rafa.energy -= 100
                        for i in range(len(atacando)):
                            screen.blit(cenario1, (0, 0))
                            Rafa.energiaLogo()
                            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                            screen.blit(capangaRas3, (xj,yj))
                            Rafa.pontuacao()
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y)) 
                                screen.blit(capangaRas3, (xj,yj))
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_width = 1199
                                while Rafa.poderx < display_width:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (Rafa.poderx, Rafa.podery))
                                    screen.blit(capangaRas3, (xj,yj))
                                    Rafa.pontuacao()
                                    Rafa.poderx += 30
                                    #COLISION
                                    print(Rafa.poderx, xj)
                                        
                                    if Rafa.poderx >= inimigo.x:
                                        
                                        print("Colidiu")
                                        colidiu = True
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            screen.blit(capangaRas3, (xj,yj))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        Rafa.poderx = Rafa.x+25
                                        if inimigo.hit(100) == True:
                                            fase4(Rafa.score)
                                        break
                                    
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                                   
                        
                  
                    else:
                        print("Sem energia")
                    print(Rafa.energy)


                # superAtaque

                if event.key == K_d:
                     # settando imgs
                    atacando1 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo1.png"))
                    atacando2 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo2.png"))
                    atacando3 = pygame.image.load(os.path.join(
                        folderPersonagem+"\RAFA", "pulo3.png"))
                    superR1 = pygame.image.load(os.path.join(
                        folderPoderes+"\PoderRafa", "superR1.png"))
                    atacando = [atacando1, atacando2, atacando3, superR1]
                    enemyx = 50
                    colidiu = False
                    Rafa.aumentaScore(450)
                    if  Rafa.energy > 200:
                        Rafa.energy -= 200
                        Rafa.podery = 0
                        Rafa.poderx = enemyx
                        for i in range(len(atacando)):
                            if i <= 2:
                                screen.blit(cenario1, (0, 0))
                                Rafa.energiaLogo()
                                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                screen.blit(atacando[i], (Rafa.x, Rafa.y))
                                Rafa.pontuacao()
                                time.sleep(0.1)
                                pygame.display.update()
                                pygame.display.flip()
                            if i > 2:  # display_height = 656
                                while Rafa.podery < display_height:
                                    screen.blit(cenario1, (0, 0))
                                    Rafa.energiaLogo()
                                    screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                                    screen.blit(atacando[2], (Rafa.x, Rafa.y))
                                    screen.blit(atacando[i], (inimigo.x, Rafa.podery))
                                    Rafa.podery += 20
                                    Rafa.pontuacao()
                                    pygame.display.update()
                                    pygame.display.flip()
                                    #COLISION
                                    if (Rafa.podery - inimigo.y) > -50 and (Rafa.podery - inimigo.y)<90:
                                        print("Colidiu")
                                        colidiu = True
                                        
                                        for c in range(12):
                                            screen.blit(cenario1, (0, 0))
                                            Rafa.energiaLogo()
                                            screen.blit(RafaParado, (Rafa.x, Rafa.y))
                                            Rasencol = [RasenColision1, RasenColision2,RasenColision3,RasenColision4,RasenColision5,RasenColision6,RasenColision7,RasenColision8,RasenColision9,RasenColision10,RasenColision11,RasenColision12]
                                            screen.blit(Rasencol[c], (inimigo.x,inimigo.y))
                                            Rafa.pontuacao()
                                            pygame.display.update()
                                            time.sleep(0.1)
                                    if  colidiu == True:
                                        time.sleep(0.1)
                                        Rafa.poderx = Rafa.x+25
                                       
                                        if inimigo.hit(100) == True:
                                                fase4(Rafa.score)
                                                #GAME WIN
                                        
                                        break
                                    else:                     
                                        time.sleep(0.025)
                                        pygame.display.update()
                                        pygame.display.flip()
                        
                        Rafa.poderx = Rafa.x+25
                        Rafa.podery = Rafa.y
                    else:
                        print(Rafa.name, " Sem energia")
                    print(Rafa.name, " has", Rafa.energy)




        if tecla[K_DOWN]:
            inimigoAtaque = True
            carregando = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "carregando.png"))
            screen.blit(cenario1, (0, 0))
            Rafa.energiaLogo()
            screen.blit(inimigoParado, (inimigo.x, inimigo.y))
            screen.blit(carregando, (Rafa.x, Rafa.y))
            screen.blit(capangaRas3, (xj,yj))
            Rafa.carregar()
            print(Rafa.energy)
            pygame.display.update()
            pygame.display.flip()
            # Mov para a direita
        if tecla[K_RIGHT]:
            correndoDireita1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight1.png"))
            correndoDireita2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "CorrendoRight2.png"))
            correndo = [correndoDireita1, correndoDireita2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                screen.blit(capangaRas3, (xj,yj))
                Rafa.x += Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)

        if tecla[K_LEFT]:
            # Rafa.movimentacao("esquerda")
            inimigoAtaque = True
            correndoEsquerda1 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft1.jpg.png"))
            correndoEsquerda2 = pygame.image.load(os.path.join(
                folderPersonagem+"\RAFA", "correndoLeft2.jpg.png"))
            correndo = [correndoEsquerda1, correndoEsquerda2]
            for i in range(len(correndo)):
                screen.blit(cenario1, (0, 0))
                Rafa.energiaLogo()
                screen.blit(inimigoParado, (inimigo.x, inimigo.y))
                screen.blit(correndo[i], (Rafa.x, Rafa.y))
                screen.blit(capangaRas3, (xj,yj))
                Rafa.x -= Rafa.velocidade
                Rafa.pontuacao()
                pygame.display.update()
                pygame.display.flip()

                time.sleep(0.1)
        #inimigoAtaque
        if inimigoAtaque:
            screen.blit(capangaRas3, (xj,yj))
            xj -= xj
            if xj < (Rafa.x - 20):
                print("colisao")
                screen.blit(capangaRas3, (Rafa.x,Rafa.y))
                Rafa.aumentaScore(-35)
                time.sleep(0.1)
                xj = 700
            inimigoAtaque = False
            pygame.display.update()
            pygame.display.flip()

            time.sleep(0.1)

        # Soldado BIT ATAQUES

        pygame.display.flip()
        pygame.display.update()

game_intro()

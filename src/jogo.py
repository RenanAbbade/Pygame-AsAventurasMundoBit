import pygame, sys
import os
import time
import random
import pygame.mixer
from pygame.locals import*

#Classe criadora de personagens
class Personagem(object):
    def __init__(self, name, life, energy,  y, x):
        self.alive = True
        self.name = name
        #self.image = listaMovimentosRafa
        self.life = life
        self.energy = energy
        self.x = x
        self.y = y
        self.velocidade = 40
    '''
    def movimentacao(self,evento):
        listaMov = []
        if evento == "direita":
            rafaCorrendo1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","CorrendoRight1.png"))
            rafaCorrendo2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","CorrendoRight2.png"))
            listaMov = [rafaCorrendo1,rafaCorrendo2]
            
            for i in listaMov:
                screen.blit(i,(self.x,self.y))
                self.x += self.velocidade
    '''

    
    def especial(self, enemy, lowEnergy):
        self.energy -=lowEnergy
        

    def hit(self, damage):
        self.life -=damage
        if self.life <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")
    
    def entraTela(self):
        if self.life == True:
            if self.x <= 0:
                self.x = 0
            if self.x >= 0:
                self.x = 1199


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
   
        if click[0] == 1 and action != None:
            action()
 
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("mistral",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#Sair do jogo
def quitgame():
    pygame.quit()
    quit()

#creditos
def creditos():
    
    creditos = pygame.image.load(os.path.join(folderImg,"CREDITOS.png"))
    screen.blit(creditos,(0,0))

#instruções
def inst():
 
    ins = pygame.image.load(os.path.join(folderImg,"instr.png"))
    screen.blit(ins,(0,0))
    


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
    #Musicas e img
    folderImg = "img"
    #Naruto
    gameOver = pygame.image.load(os.path.join(folderImg,"gameover.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render("-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(white))
    aviso = smallText.render("*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(white))
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
    #Musicas e img
    folderImg = "img"
    #Naruto
    youwin = pygame.image.load(os.path.join(folderImg,"youwin.jpg"))
    smallText = pygame.font.SysFont("mistral",15)
    ranque = smallText.render("-APERTE A TECLA DE ESPAÇO PARA IR AO RANKING!-",1,(black))
    aviso = smallText.render("*APÓS APERTAR ESPAÇO, ESCREVA SEU NOME NO SHEEL DO PYTHON PARA MELHOR VISÃO DA SUA PONTUAÇÃO",1,(black))
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
#menu

def tocarMusica(nomeMusica):
    pygame.mixer.pre_init()
    pygame.mixer.music.load(nomeMusica)
    pygame.mixer.music.play(-1)

def game_intro():

    intro = True
    folderImg = "img"
    menu = pygame.image.load(os.path.join(folderImg,"CAPA.PNG"))
    #Rodar música do menu
    tocarMusica('op.ogg')
    while intro == True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #colocar imagem do menu
        screen.blit(menu,(0,0))
        button("JOGO",600,540,50,50,white,bright_rasen,jogo)
        button("CRÉDITOS",0,560,100,50,Aqua,white,creditos)
        button("INSTRUÇÕES",0,510,100,50,LightSkyBlue,white,inst)
        button("SAIR",0,610,100,50,DeepSkyBlue,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

def fase1():
    #Inicializando a musica da fase
    tocarMusica('combate1.ogg')
    #screen.blit(Rafa)
    relogio = pygame.time.Clock()
    #Criando o personagem principal e settando seus moves
    parado = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","PARADO.png"))
    correndoDireita1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","CorrendoRight1.png"))
    correndoDireita2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","CorrendoRight2.png"))
    correndoEsquerda1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","correndoLeft1.jpg.png"))
    correndoEsquerda2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","correndoLeft2.jpg.png"))
    atacando1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","atacando1.png"))
    atacando2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","atacando2.png"))
    atacando3 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","atacando3.png"))
    pulando1 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","pulo1.png"))
    pulando2 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","pulo2.png"))
    pulando3 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","pulo3.png"))
    pulando4 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","pulo4.png"))
    pulando5 = pygame.image.load(os.path.join(folderPersonagem+"\RAFA","pulo5.png"))

    
    

    Rafa = Personagem("Rafa", 200, 100, 400, 20)
    cenario1 = pygame.image.load(os.path.join(folderCenario,"floresta2.jpg"))
    jogando = True
    cont = 0
    
    while jogando:
        relogio.tick(100)
        tempo = pygame.time.get_ticks()/1000
        pygame.display.flip()
        tecla = pygame.key.get_pressed()

        screen.blit(cenario1, (0,0))
        screen.blit(parado, (Rafa.x, Rafa.y))
         
        for event in pygame.event.get():
            pygame.display.update()
            pygame.display.flip()
                
                #Animação andar para frente
            if event.type ==  pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                        pulando = [pulando1,pulando2, pulando3, pulando4, pulando5]
                        for i in range(len(pulando)):
                            screen.blit(cenario1, (0,0))
                            screen.blit(pulando[i], (Rafa.x,Rafa.y))
                            if i >= 2 and i <4:
                                Rafa.y += 170
                                Rafa.x += 10
                                pygame.display.update()
                                pygame.display.flip()
                                
                            if i <2:
                                Rafa.y -= 170
                                Rafa.x += 10
                                pygame.display.update()
                                pygame.display.flip()
                                
                            pygame.display.update()
                            pygame.display.flip()
                            time.sleep(0.140)

                if event.key == K_SPACE:
                    atacando = [atacando1, atacando2, atacando3]
                    for i in range(len(atacando)):
                        screen.blit(cenario1, (0,0))
                        screen.blit(atacando[i], (Rafa.x,Rafa.y))
                        pygame.display.update()
                        pygame.display.flip()
                        time.sleep(0.140)
            
                #Mov para a direita
        if tecla[K_RIGHT]:  
                #Rafa.movimentacao("direita")
               
                correndo = [correndoDireita1,correndoDireita2]
                for i in range(len(correndo)):
                        screen.blit(cenario1, (0,0))
                        screen.blit(correndo[i], (Rafa.x,Rafa.y))
                        Rafa.x += Rafa.velocidade
                        pygame.display.update()
                        pygame.display.flip()
                
                        time.sleep(0.1)
              
                
        if tecla[K_LEFT]:
            #Rafa.movimentacao("esquerda")
            correndo = [correndoEsquerda1,correndoEsquerda2]
            for i in range(len(correndo)):
                    screen.blit(cenario1, (0,0))
                    screen.blit(correndo[i], (Rafa.x,Rafa.y))
                    Rafa.x -= Rafa.velocidade
                    pygame.display.update()
                    pygame.display.flip()
                
                    time.sleep(0.1)

        
            
          
      
        pygame.display.update()
        


        
        

#jogo
def jogo():
   fase1()

pygame.init()
 
display_width = 1199
display_height = 656

#Cores
black = (0,0,0)
white = (255,255,255)
rasen = (240,255,255)
bright_red = (255,255,255)
bright_rasen = (224,255,255)
DeepSkyBlue = (0,191,255)
LightSkyBlue = (135,206,250)
SkyBlue	= (135,206,235)
block_color = (53,115,255)
Aqua = (0,255,255)

#Sceen
folderImg = "img"
folderCenario = "img\Cenarios"
folderPersonagem = "img\Personagens"
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(' As Aventuras do Mundo Bit ')
clock = pygame.time.Clock()

game_intro() 
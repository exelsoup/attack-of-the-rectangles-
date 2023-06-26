import pygame
import numpy as np 
from os import path
import random
WIDTH = 1500
HEIGHT = 1000
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 50, 255)
pygame.init()
pygame.display.set_caption("Attack of the Robot arm")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
def Rmat(degree):
    radian=np.deg2rad(degree)
    cos=np.cos(radian)
    sin=np.sin(radian)
    R=np.array([[cos,-sin,0],[sin,cos,0],[0,0,1]])
    return R
def Tmat(tx,ty):
    T=np.array([[1,0,tx],[0,1,ty],[0,0,1]])
    return(T)
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')
def drawPolygon(V, M, screen, color):
    R3_2x2 = M[0:2,0:2]
    Tvec3 = M[0:2,2]
    V3=  V @ R3_2x2.T + Tvec3
    pygame.draw.polygon(screen, color, V3, 20)
    return (V3[1]+V3[2])/2 

def movie():
    i=0
    if stage==0:
        background = pygame.image.load(path.join(img_dir, "start.png")).convert()
        background_rect = background.get_rect()
        waiting = True
        while waiting:
            screen.blit(background, background_rect)
            clock.tick(FPS)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    i+=1
                    if i==4:    #### 그림 개수
                        waiting=False
                    else:  
                        background = pygame.image.load(path.join(img_dir, "start{}.png".format(i))).convert()
                        background_rect = background.get_rect()
               
    elif stage==2:
        background = pygame.image.load(path.join(img_dir, "s2.png")).convert()
        background_rect = background.get_rect()
        waiting = True
        while waiting:
            screen.blit(background, background_rect)
            clock.tick(FPS)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:

                    i+=1
                    if i==1:    #### 그림 개수
                        waiting=False
                    else:  
                        background = pygame.image.load(path.join(img_dir, "s2{}.png".format(i))).convert()
                        background_rect = background.get_rect()
    elif stage==3:
        background = pygame.image.load(path.join(img_dir, "s3.png")).convert()
        background_rect = background.get_rect()
        waiting = True
        while waiting:
            screen.blit(background, background_rect)
            clock.tick(FPS)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    i+=1
                    if i==3:    #### 그림 개수
                        waiting=False
                    else:  
                        background = pygame.image.load(path.join(img_dir, "s3{}.png".format(i))).convert()
                        background_rect = background.get_rect()
class bad_rect(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.w=random.uniform(30,70)
        self.h=random.uniform(30,70)
        self.color=np.random.randint(150,255,size=3)
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect= self.image.get_rect()
        self.rect.x=random.randint(WIDTH-10,WIDTH-1)
        self.rect.y=random.uniform(350,450)
        self.spx=random.uniform(-6,6)
        self.spy=random.uniform(-6,6)
        if stage==2.1 or stage==2.2 or stage==2.3:
            self.rect.x=0
            self.rect.y=random.randint(200,560)
            self.spy=0
            self.spx=random.uniform(1,7)
        
    def update(self):
        self.rect.x+=self.spx
        self.rect.y+=self.spy
        if stage!=2.3 and stage!=2.2:
            if (self.rect.x+self.w>WIDTH or self.rect.x<0):
                self.spx*=-1
            if (self.rect.y+self.h>HEIGHT or self.rect.y<0):
                self.spy*=-1
            if stage==1.2:
                self.color=np.random.uniform(150,255,size=3)
        else:
            if (self.rect.x>WIDTH):
                self.kill()

player_img1 = pygame.image.load(path.join(img_dir, "c1.png")).convert() 
player_img0 = pygame.image.load(path.join(img_dir, "c0.png")).convert() 
player_img1.set_colorkey(BLACK)
player_img0.set_colorkey(BLACK)

player_imgjet1=pygame.image.load(path.join(img_dir, "cj1.png")).convert()
player_imgjet0=pygame.image.load(path.join(img_dir, "cj0.png")).convert()
player_imgjet1.set_colorkey(BLACK)
player_imgjet0.set_colorkey(BLACK)
size=1
ms=2
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img1, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 25
        self.speedx = 0
        self.speedy=0 
        self.jump=True
        self.jet=0

    def update(self):  ## move
        if self.jet<=0:
            if (self.speedx>0):
                self.image = pygame.transform.scale(player_img1, (50, 50))     
                self.image.set_colorkey(BLACK)
            elif (self.speedx<0):
                self.image = pygame.transform.scale(player_img0, (50, 50))    
                self.image.set_colorkey(BLACK)
        else:
            if (self.speedx>0):
                self.image = pygame.transform.scale(player_imgjet1, (50, 50))     
                self.image.set_colorkey(BLACK)
            elif (self.speedx<0):
                self.image = pygame.transform.scale(player_imgjet0, (50, 50)) 
                self.image.set_colorkey(BLACK)
        keystate = pygame.key.get_pressed()
        self.speedx=0
        if stage!=3:                     
            if (self.speedy==0 and self.jump==False):
                if keystate[pygame.K_SPACE]: 
                        self.speedy=(-24)/size
                        self.jump=True
            else:                    
                self.speedy+= 1/size
                if self.rect.bottom>HEIGHT-2:  
                    if stage==1.1 or stage==1.2 or stage==1.3 or stage==2.1:
                        self.speedy=0
                        self.jump=False

                for o in objs:
                    if self.rect.left <= o[0] + o[2] and self.rect.right >= o[0] and self.rect.top <= o[1] + o[3] and self.rect.bottom >= o[1]:
                        if o[1]+o[3]+25>self.rect.top>o[1]+o[3]-25:
                            self.speedy=5
                        elif o[1]+25>self.rect.bottom>o[1]-25:
                            self.rect.bottom=o[1]
                            self.speedy=0
                            self.jump=2
                        elif o[0]-15<self.rect.right<o[0]+15:
                            if self.speedx>0:
                                self.speedx=0
                        elif o[0]+o[2]+15>self.rect.left>o[0]+o[2]-15:
                            if self.speedx<0:
                                self.speedx=0
                        if self.jump==2:
                            self.speedy=0
                            if keystate[pygame.K_SPACE]:
                                self.speedy=(-24)/size
                                self.jump=True
                    
                if stage!=1 and stage!=1.1 and stage!=1.2:
                    for s in strings:
                        if self.rect.left <= s[0] + s[2] and self.rect.right >=s[0] and self.rect.top <= s[1] + s[3] and self.rect.bottom >= s[1]:
                            if keystate[pygame.K_SPACE]:
                                self.speedy=0
                                self.jump=False

                if self.jet>0:
                    if keystate[pygame.K_SPACE]:
                        self.speedy-=(1.1)/size
                        if self.jump==1:
                            self.speedy+=(0.5)/size
                        self.jet-=0.07
                if self.rect.top==0:
                    if stage==1.1 or stage==1.2 or stage==1.3:
                        self.speedy=5
                        # self.rect.top=0
                    
              
        if keystate[pygame.K_LEFT]:
            self.speedx = (-8)/size
        if keystate[pygame.K_RIGHT]:
            self.speedx = (8)/size
            
        self.rect.x += self.speedx
        self.rect.y+=self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

def newrect():
    r = bad_rect()
    all_sprites.add(r)
    rects.add(r)
def obj():
    if stage==1.1:
        objs.append(pygame.draw.rect(screen,BLACK,(30+(40),HEIGHT-30-(120),80,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(270,HEIGHT-30-(130),130,60),20))
        objs.append(pygame.draw.rect(screen,BLACK,(170,HEIGHT-(290),180,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(450,HEIGHT-30-(400),100,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(670,HEIGHT-30-(600),80,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(750,HEIGHT-30-(750),80,70),20))
        objs.append(pygame.draw.rect(screen,BLACK,(590,HEIGHT-30-(800),140,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(390,HEIGHT-30-(600),150,60),20))
        objs.append(pygame.draw.rect(screen,BLACK,(30+(40),HEIGHT-30-(1050),180,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(1200,HEIGHT-500,80,70),20))
        objs.append(pygame.draw.rect(screen,BLACK,(1000,HEIGHT-550,25,70),20 ))
        objs.append(pygame.draw.rect(screen,BLUE,(1400,HEIGHT-450,200,70),20 ))
    elif stage==1.2:
        objs.append(pygame.draw.rect(screen,BLACK,(200,HEIGHT-130,80,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(350,HEIGHT-370,50,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(120,HEIGHT-600,25,25),20))
        objs.append(pygame.draw.rect(screen,BLACK,(1200,HEIGHT-300,300,90),20))
    elif stage==1.3:
        objs.append(pygame.draw.rect(screen,BLACK,(0,960,80,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(200,420,60,60),20))
        objs.append(pygame.draw.rect(screen,BLACK,(590,220,60,60),20))
        objs.append(pygame.draw.rect(screen,BLACK,(1250,490,320,60),20))
    elif stage==2.1:
        for a in range(7):
            objs.append(pygame.draw.rect(screen,BLACK,((120*a),900-(80*a),40,40),20))
        for a in range(5):
            objs.append(pygame.draw.rect(screen,BLACK,(570-(120*a),370-(80*a),40,40),20))
    elif stage==2.2:
        objs.append(pygame.draw.rect(screen,BLACK,(150,920,50,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(320,900,50,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(490,910,60,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(650,900,50,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(570,500,70,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(210,300,70,40),20))
        objs.append(pygame.draw.rect(screen,BLACK,(320,0,50,30),20))

    elif stage==2.3:
        objs.append(pygame.draw.rect(screen,BLACK,(450,995,60,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(300,950,60,50),20))
        objs.append(pygame.draw.rect(screen,BLACK,(420,840,50,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(550,700,150,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(700,580,120,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(610,440,90,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(530,350,120,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(320,300,80,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(220,210,90,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(260,115,60,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(350,50,50,30),20))
    elif stage==2.4:
        for i in range(10):
            objs.append(pygame.draw.rect(screen,BLACK,(390+(i*50),930-(i*30),50,30),20))
        objs.append(pygame.draw.rect(screen,BLACK,(600,80,100,30),20))
def string():
    if stage==1.3:
        strings.append(pygame.draw.rect(screen,BLACK,(205,440,10,400)))
        strings.append(pygame.draw.rect(screen,BLACK,(595,240,10,350)))
        strings.append(pygame.draw.rect(screen,BLACK,(920,0,10,600)))
    elif stage==2.4:
        strings.append(pygame.draw.rect(screen,BLACK,(760,0,10,600)))
           
                
        
jet_img = pygame.image.load(path.join(img_dir, "jet.png")).convert()
jetpack_img =pygame.transform.scale(jet_img, (30, 30)) 
jetpack_img.set_colorkey(BLACK)
class jet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.image = jetpack_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
def jetpack(x,y):
    j = jet(x, y)
    all_sprites.add(j)
    jets.add(j)
gameover=True
running = True
stage=0
x=0 

while running:

    if stage==0:
        movie()
        gameover=True
        stage=1.1
    elif stage==1.1:
        if gameover==True:
            background = pygame.image.load(path.join(img_dir, "stage1-1.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            all_sprites = pygame.sprite.Group()
            rects = pygame.sprite.Group()
            objs=[]
            obj()
            for i in range(8):
                newrect()
            player = Player()
            all_sprites.add(player)
            
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        pygame.draw.rect(screen,BLUE,(1400,HEIGHT-450,200,50))
        hits = pygame.sprite.spritecollide(player, rects, True, pygame.sprite.collide_circle)
        for hit in hits:
            newrect()
            player.kill()
            player = Player()
            all_sprites.add(player)

        if player.rect.right==WIDTH and (500<player.rect.bottom<600):
            stage=1.2
            gameover=True
        
    elif stage==1.2:
        if gameover==True:
            background = pygame.image.load(path.join(img_dir, "stage1-2.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            all_sprites = pygame.sprite.Group()
            jets = pygame.sprite.Group()
            objs=[]
            obj()
            player = Player()
            player.rect.centerx = 20
            player.rect.bottom = HEIGHT - 25
            all_sprites.add(player)
            jetpack(125,395)
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        hits = pygame.sprite.spritecollide(player, jets, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.jet=350

        if player.rect.right>WIDTH-30 and player.rect.top<=0:
            stage=1.3
            gameover=True
    elif stage==1.3:   
        if gameover==True:
            player = Player()
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            background = pygame.image.load(path.join(img_dir, "stage1-3.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            rects = pygame.sprite.Group()
            objs=[]
            mobjs=[]
            obj()
            strings=[]
            string()
            for i in range(4):
                newrect()
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        for s in strings:
            pygame.draw.rect(screen,(150,75,0),s,10)
        hits = pygame.sprite.spritecollide(player, rects, True, pygame.sprite.collide_circle)
        for hit in hits:
            newrect()
            player.kill()
            player = Player()
            all_sprites.add(player)
        if player.rect.right==WIDTH and (400<player.rect.bottom<500):
            stage=2
            gameover=True
    elif stage==2:
        movie()
        gameover=True
        stage=2.1
        WIDTH=800
        HEIGHT=1000
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        size=2.2
        player = Player()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
    if stage==2.1:   
        if gameover==True:
            background = pygame.image.load(path.join(img_dir, "stage2-1.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            rects = pygame.sprite.Group()
            jets = pygame.sprite.Group()
            objs=[]
            obj()
            strings=[]
            string()
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        if player.rect.top<=0 and stage==2.1:
            stage=2.2
            player.rect.bottom=HEIGHT-3
            gameover=True
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        for s in strings:
            pygame.draw.rect(screen,(150,75,0),s,10)
    elif stage==2.2:
        if gameover==True:
            background = pygame.image.load(path.join(img_dir, "stage2-2.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            rects=[]
            rects = pygame.sprite.Group()
            jets = pygame.sprite.Group()
            objs=[]
            obj()
            strings=[]
            string()
            jetpack(670,900)
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        hits = pygame.sprite.spritecollide(player, jets, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.jet=20
        if player.rect.top<=0 and stage==2.2:
            stage=2.3
            x=player.rect.left
            player.kill()
            gameover=True
        elif player.rect.top>=HEIGHT :
            stage=2.1
            player.rect.top=15
            gameover=True
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        for s in strings:
            pygame.draw.rect(screen,(150,75,0),s,10)
    elif stage==2.3:
        if gameover==True:
            blade = np.array([[0,0], [180, 0], [180,30],[0,30]])
            background = pygame.image.load(path.join(img_dir, "stage2-3.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            player = Player()
            player.rect.left=x
            player.speedy=-10
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            rects = pygame.sprite.Group()
            jets = pygame.sprite.Group()
            objs=[]
            obj()
            strings=[]
            string()
            k=0
            angle=0
        k+=1
        if k%40==0:
            newrect()
        hits = pygame.sprite.spritecollide(player, rects, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.rect.left+=25

        angle+=4
        M_1=Rmat(angle)@Tmat(0,-15)
        screen.blit(background, background_rect)
        drawPolygon(blade,Tmat(40,380)@M_1,screen,(205,50,205))
        drawPolygon(blade,Tmat(40,380)@Rmat(90)@M_1,screen,(205,250,205))
        drawPolygon(blade,Tmat(40,380)@Rmat(180)@M_1,screen,(50,200,205))
        drawPolygon(blade,Tmat(40,380)@Rmat(270)@M_1,screen,(105,100,205))
        pygame.draw.circle(screen,WHITE,(40,380),3)
        all_sprites.update()
        all_sprites.draw(screen)
        if player.rect.top<=0 and stage==2.3:
            stage=2.4
            x=player.rect.left
            player.kill()
            gameover=True
        elif player.rect.bottom>=HEIGHT :
            stage=2.2
            player.rect.top=15
            gameover=True
        if 560>player.rect.top>200:
            player.rect.x+=1.7
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        for s in strings:
            pygame.draw.rect(screen,(150,75,0),s,10)

    elif stage==2.4:
        if gameover==True:
            background = pygame.image.load(path.join(img_dir, "stage2-4.png")).convert()
            background_rect = background.get_rect()
            gameover=False
            player = Player()
            player.rect.left=x
            player.speedy=-10
            all_sprites = pygame.sprite.Group()
            all_sprites.add(player)
            rects = pygame.sprite.Group()
            objs=[]
            obj()
            strings=[]
            string()
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)

        if player.rect.bottom>=HEIGHT :
            stage=2.3
            player.rect.top=15
            gameover=True
        if 600<player.rect.left<650 and 70<player.rect.bottom<90:
            stage=3
        for o in objs:
            pygame.draw.rect(screen,BLACK,o,13)
        for s in strings:
            pygame.draw.rect(screen,(150,75,0),s,10)
    elif stage==3:
        WIDTH=1500
        HEIGHT=1000
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        movie()
        running=False

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
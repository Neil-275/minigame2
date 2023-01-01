from math import sqrt
import random
import pygame
import math

#intialize pygame
pygame.init()
maxW,maxH=900,500   
screen= pygame.display.set_mode((maxW,maxH))

def draw(player_car,x,y):
    screen.blit(player_car,(x, y))

def distance(a,b,x,y):
    return sqrt((a-x)*(a-x)+(b-y)*(b-y))

def resize(img,x,y):
    return pygame.transform.scale(img,(x,y))
running =True

#1 Right
#0 Left

spriteEnemy=[[],[]]
di=[-1,1]
class ENEMY:
    def __init__(self,x,idi,velocity):
        self.curSprite=0
        self.x=x
        self.y=3
        self.idi=idi
        self.velocity=velocity
    def newEnenmy(self):
        a=ENEMY(random.choice({-30,maxW}),random.choice({0,1}),random.randint(1,3))
        return a
    def run(self):
        self.curSprite+=0.4
        self.x+= self.velocity*di[self.idi]
        draw(spriteEnemy[self.idi][int(self.curSprite)%len(spriteEnemy[self.idi])],self.x,self.y)

class FIGHTER:
    def __init__(self):
        self.x=400
        self.y=200
        self.rangeImg=0
        self.idleSprite=[]
        self.curIdleSprite=0
        self.AttackSprite=[]
        self.curAttSprite=0
        self.attRange=150
        self.curAttRange=0
        self.idi=0
        self.active=0
        self.targetX,self.targetY=0,0
    def recover(self): #Chay khi active=0
        if self.curAttRange<self.attRange:
            self.curAttRange +=0.1   
        self.curIdleSprite+=0.01
        draw(self.idleSprite[di[self.idi]][int(self.curIdleSprite)%len(self.idleSprite[di[self.idi]])],self.x,self.y)
        #Left
        draw(resize(self.rangeImg,self.curAttRange,10),self.x-self.curAttRange,self.y+50)
        #Right
        draw(resize(self.rangeImg,self.curAttRange,10),self.x+20,self.y+50)
    def setAttack(self,idi,x,y):
        self.curAttSprite=0
        self.idi=idi
        self.active=1
        if abs(self.x-x)<=self.curAttRange:
            self.targetX=x
        else :
            self.targetX=self.x
        self.curAttRange=0
    def Attack(self): #Chay khi active=1
        direct=di[self.idi]
        if direct*self.x<direct*self.targetX:
            self.x+=7*direct
        # self.curAttSprite+=0.4
        # if self.curAttSprite<5:
        #     draw(self.AttackSprite[direct][int(self.curAttSprite)],self.x,self.y)
        # else:
        #     self.active=0
    

#INITIALIZE
fighter=FIGHTER()

for i in range(2):
    fighter.idleSprite.append([])
    for j in range(1,6,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.idleSprite[i].append(img)
fighter.rangeImg=pygame.image.load("img/rect.png")

enenmy=[]
obj=[]
while running:
    screen.fill((4,4,4))
    # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                fighter.setAttack(0,fighter.x,fighter.y)
                # for i in range(0,fighter.x-fighter.attRange,-0.5):
                #     if obj[i]!=-1:
                #         fighter.setAttack(0,obj[j])
                
            # if event.key== pygame.K_RIGHT:
            #     for i in range(0,fighter.x+fighter.attRange,0.5):
            #         if obj[i]!=-1:
            #             fighter.setAttack(0,obj[j])
            #             break
    fighter.recover()
    fighter.Attack()
    pygame.display.update()
   
    # for e in enemy:
    #     obj[e.x]=-1
    #     e.x+=e.velocity*e.idi
    #     if e.x<-50 or e.x>with:
    #         enemy.remove(e)
    #     obj[e.x]=e
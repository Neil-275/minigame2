from math import sqrt
import random
import pygame
import math

#intialize pygame
pygame.init()
maxW,maxH=900,500   
screen= pygame.display.set_mode((maxW,maxH))
bg=pygame.image.load("img/bg.png")
bg=pygame.transform.scale(bg,(maxW,maxH))

def draw(player_car,x,y):
    screen.blit(player_car,(x, y))

def distance(a,b,x,y):
    return sqrt((a-x)*(a-x)+(b-y)*(b-y))

def resize(img,x,y):
    return pygame.transform.scale(img,(x,y))


#1 Right
#0 Left

spriteEnemy=[]
spriteEnemy.append(resize(pygame.image.load("img/shuriken.png"),32,32))
di=[-1,1]
def newEnemy():
    a=ENEMY(random.choice([-30,maxW]),random.choice([0,1]),random.uniform(0.5,1))
    return a
class ENEMY:
    def __init__(self,x,idi,velocity):
        self.curSprite=0
        self.x=x
        self.y=fighter.y+40
        self.idi=idi
        self.velocity=velocity
    def run(self):
        self.curSprite+=0.4
        self.x+= self.velocity*di[self.idi]
        draw(spriteEnemy[int(self.curSprite)%len(spriteEnemy)],self.x,self.y)

class FIGHTER:
    def __init__(self):
        self.width=80
        self.height=130
        self.x=400
        self.y=320
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
        self.cnt=4
    def recover(self): #Chay khi active=0
        if self.curAttRange<self.attRange:
            self.curAttRange +=0.1   
        self.curIdleSprite+=0.01
        if self.active==0:
            draw(self.idleSprite[self.idi][int(self.curIdleSprite)%len(self.idleSprite[di[self.idi]])],self.x,self.y)
        #Left
        draw(resize(self.rangeImg,self.curAttRange,10),self.x-self.curAttRange,self.y+self.height*1.05)
        #Right
        draw(resize(self.rangeImg,self.curAttRange,10),self.x+self.width-20,self.y+self.height*1.05)
    def setAttack(self,idi,x):
        self.curAttSprite=random.choice([0,5,10,15])
        self.idi=idi
        self.active=1
        if abs(self.x-x)<=self.curAttRange:
            self.targetX=x 
            
        else :
            self.targetX=self.x
        self.curAttRange=0
        self.cnt=0
    def Attack(self): #Chay khi active=1
        direct=di[self.idi]
        if direct*self.x<direct*self.targetX:
            self.x+=5*direct
        self.curAttSprite+=0.021
        self.cnt+=0.021
        if self.cnt<5:
            draw(self.AttackSprite[self.idi][int(self.curAttSprite)],self.x,self.y)
        else:
            self.active=0
    

#INITIALIZE
fighter=FIGHTER()

for i in range(2):
    fighter.idleSprite.append([])
    fighter.AttackSprite.append([])
    for j in range(1,6,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        # img = resize(img,56,fighter.height)
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.idleSprite[i].append(img)
    #ATTACK
    for j in range(10,15,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        # img = resize(img,56,fighter.height)
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.AttackSprite[i].append(img)
    for j in range(18,23,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        # img = resize(img,56,fighter.height)
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.AttackSprite[i].append(img)
    for j in range(27,32,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        # img = resize(img,56,fighter.height)
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.AttackSprite[i].append(img)
    for j in range(6,11,1):
        img = pygame.image.load(f"img/lee-{j}.png")
        img = resize(img,fighter.width,fighter.height)
        if i==0:
            img=pygame.transform.flip(img,True,False)
        fighter.AttackSprite[i].append(img)
print (len(fighter.AttackSprite[0]))
fighter.rangeImg=pygame.image.load("img/rect.png")
enemy=[]
obj=[]

### INIT game
running =True
clock=pygame.time.Clock()
pivotTime=0
duration=random.uniform(500,1500)

while running:
    curTime=pygame.time.get_ticks()
    draw(bg,0,0)
    # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and fighter.active==0:
                # fighter.setAttack(0,fighter.x)
                maxx=0
                ko=0
                for e in enemy: 
                    if fighter.x-e.x<=fighter.curAttRange:
                        maxx=max(e.x,maxx)
                        ko=e
                fighter.setAttack(0,maxx)
                if ko!=0 :
                    enemy.remove(ko)
                
            if event.key==pygame.K_RIGHT and fighter.active==0:
                minn=1300
                for e in enemy: 
                    if e.x-fighter.x<=fighter.curAttRange:
                        minn=min(minn,e.x)
                        ko=e
                if minn==1300:
                    minn=fighter.x
                    ko=0
                fighter.setAttack(1,minn) 
                if ko!=0 :
                    enemy.remove(ko)
                       
    
    if fighter.active:
        fighter.Attack()
    fighter.recover()
    # img = pygame.image.load("img/lee-9.png")
    # img = resize(img,fighter.width,fighter.height)
    # draw(img,fighter.x,fighter.y)
    for e in enemy:
        e.run()
        if e.x<-40 or e.x>maxW+10:
            enemy.remove(e)
        if distance(e.x,e.y,fighter.x,fighter.y)<50:
            enemy.remove(e)
    if curTime-pivotTime>=duration:
        duration=duration=random.uniform(500,1500)

        pivotTime=curTime
        enemy.append(newEnemy())
    pygame.display.update()
    
    
        
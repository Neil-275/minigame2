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

bg=pygame.image.load("img/bg.png")
bg=pygame.transform.scale(bg,(maxW,maxH))
heart=resize(pygame.image.load("img/heart.png"),32,32)
wood=pygame.image.load("img/wood.png")
wood=resize(wood,160,80)
#1 Right
#0 Left

spriteEnemy=[]
spriteEnemy.append(resize(pygame.image.load("img/shuriken.png"),32,32))
di=[-1,1]
def newEnemy():
    a=ENEMY(random.choice([-30,maxW]),random.choice([0,1]),random.uniform(0.5,0.7))
    return a
class ENEMY:
    def __init__(self,x,idi,velocity):
        self.curSprite=0
        self.x=x
        self.y=fighter.y+40
        self.idi=idi
        self.velocityX=velocity
        self.velocityY=0
        self.kicked=0
    def run(self):
        self.curSprite+=0.4
        self.x+= self.velocityX*di[self.idi]
        self.y+= self.velocityY
        draw(spriteEnemy[int(self.curSprite)%len(spriteEnemy)],self.x,self.y)
    def kickedd(self):
        pass
        self.idi=1-self.idi
        self.velocityY=random.uniform(-1,1)
        self.velocityX=0.6

class FIGHTER:
    def __init__(self):
        self.health=3
        self.width=80
        self.height=125
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
        self.death=[]
        self.curDeath=0
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
        if self.idi==0:
            if direct*self.x<direct*(self.targetX+60):
                self.x+=3*direct
        if self.idi==1:
            if direct*self.x<direct*(self.targetX-60):
                self.x+=3*direct
        
        self.curAttSprite+=0.021
        self.cnt+=0.021
        if self.cnt<5:
            draw(self.AttackSprite[self.idi][int(self.curAttSprite)],self.x,self.y)
        else:
            self.active=0
    def die(self):
        self.curDeath+=0.01
        # if self.curDeath<len(self.death):
        draw(self.death[min(11,int(self.curDeath))],self.x,self.y-self.death[min(11,int(self.curDeath))].get_height()+self.height)
        # else :
        #     draw(self.death[11],self.x,self.y+self.death[11].get_height()+self.height)

#INITIALIZE
fighter=FIGHTER()

for i in range(2):
    fighter.idleSprite.append([])
    fighter.AttackSprite.append([])
    if i==0:
        for j in range(1,13,1):
            img = pygame.image.load(f"img/deathLee-{j}.png")
            fighter.death.append(img)
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
fighter.rangeImg=pygame.image.load("img/rect.png")
enemy=[]

### INIT game
running =True
clock=pygame.time.Clock()
pivotTime=0
end=0
duration=random.uniform(500,1000)
print(type(fighter))
while running:
    curTime=pygame.time.get_ticks()
    draw(bg,0,0)
    draw(wood,0,0)
    for i in range(fighter.health):
        draw(heart,(i+1)*36,10)
    if fighter.health==0:
        fighter.die()
        
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN and end ==0:
            if event.key==pygame.K_LEFT and fighter.active==0:
                # fighter.setAttack(0,fighter.x)
                maxx=0
                ko=None
                for e in enemy: 
                    if fighter.x-e.x<=fighter.curAttRange:
                        maxx=max(e.x,maxx)
                        ko=e
                fighter.setAttack(0,maxx)
                if ko!=None :
                    for e in enemy:
                        if e==ko:
                            e.kickedd()
                            break
                
            if event.key==pygame.K_RIGHT and fighter.active==0:
                minn=1300
                ko=None
                for e in enemy: 
                    if e.x-fighter.x<=fighter.curAttRange:
                        minn=min(minn,e.x)
                        ko=e
                if minn==1300:
                    minn=fighter.x
                    ko=None
                fighter.setAttack(1,minn) 
                if ko!=None :
                    for e in enemy:
                        if e==ko:
                            e.kickedd()
                            break
                       
    if end:
        pygame.display.update()
        continue
    if fighter.active:
        fighter.Attack()
    fighter.recover()
    if end==1:
        print(321)
    # img = pygame.image.load("img/lee-9.png")
    # img = resize(img,fighter.width,fighter.height)
    # draw(img,fighter.x,fighter.y)
    for e in enemy:
        e.run()
        if e.x<-40 or e.x>maxW+10:
            enemy.remove(e)
        if distance(e.x,e.y,fighter.x,fighter.y)<45:
            enemy.remove(e)
            fighter.health-=1
            if fighter.health==0:
                end=1
    if curTime-pivotTime>=duration:
        duration=duration=duration=random.uniform(500,1000)

        pivotTime=curTime
        enemy.append(newEnemy())
    pygame.display.update()
    
    
        
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

class FIGHTER:
    def __init__(self):
        self.x=0
        self.y=0
        self.rangeImg
        self.idleSprite=[[],[]]
        self.curIdleSprite=0
        self.AttackSprite=[[],[]]
        self.curAttSprite=0
        self.attRange=0
        self.curAttRange=0
        self.di=[1,-1]
        self.idi=0
        self.active=0
        self.targetX,self.targetY
    def recover(self): #Chay khi active=0
        if self.curAttRange<self.attRange:
            self.curAttRange +=1    
        self.curIdleSprite+=0.4
        draw(self.IdleSprite[self.di[self.idi]][int(self.curIdleSprite%len(self.idleSprite[self.di[self.idi]]))],self.x,self.y)
        #Left
        draw(resize(self.rangeImg,(self.curAttRange,20)),self.x-self.curAttRange,self.y)
        #Right
        draw(resize(self.rangeImg,(self.curAttRange,30)),self.x,self.y)
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
        direct=self.di[self.idi]
        if direct*self.x<direct*self.TargetX:
            self.x+=7*direct
        self.curAttSprite+=0.4
        if self.curAttSprite<5:
            draw(self.AttackSprite[direct][int(self.curAttSprite)],self.x,self.y)
        else:
            self.active=0
while running:
    screen.fill((4,4,4))
    # screen.blit(background,(0,0))
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running=False
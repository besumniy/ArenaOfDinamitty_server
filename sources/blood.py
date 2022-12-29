from sources.element import *

from random import randint

class blood():
    def __init__(self, x, y, c,p, r, w,o):
        self.vectX=x
        self.vectY=y
        self.color=c
        elem=element()
        elem.coord=[0,0,0,0,0,0,0,0]
        elem.coord[0]=p[0]
        elem.coord[1]=p[1]
        elem.calcF()
        elem.face=True
        elem.look="images\\blood.png"#add red ball
        elem.height=randint(5,25)
        elem.width=elem.height
        self.pers=[elem]
        self.radius=r
        #elem.height=r
        #elem.width=r
        self.weight=w
        self.owner=o
        self.i=0
    def todo(self,s=None):
        self.pers[0].coord[0]+=self.vectX
        self.pers[0].coord[1]+=self.vectY
        self.vectY-=self.weight
        if self.vectX>0 and self.vectX-self.weight/4>0:
            self.vectX-=self.weight/4
        elif self.vectX>0:
            self.vectX=0
        elif self.vectX<0 and self.vectX+self.weight/4<0:
            self.vectX+self.weight/4
        elif self.vectX<0:
            self.vectX=0
        self.i+=1

    def isOverlap(self,w):
        if self.i==30:
            w["peaces"].remove(self)

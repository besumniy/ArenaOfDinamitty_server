from sources.element import *


class peace():
    def __init__(self,e,o,w,p1,p2,p3=0):
            self.vectX=p1
            self.vectY=p2
            self.pers=e
            self.weight=p3
            self.owner=o
            self.w=w
            self.fly=True
        
    def todo(self,s=None):
        def do(p):
            for i in range(4):
                p.coord[i*2]+=self.vectX
                p.coord[i*2+1]+=self.vectY
            for child in p.child:
                do(child[0])

        do(self.pers[0])

        
        if self.vectX>0 and self.vectX-self.weight/4>=0:
                self.vectX-=self.weight/4
        elif self.vectX>0:
                self.vectX=0
        elif self.vectX<0 and self.vectX+self.weight/4<=0:
                self.vectX+=self.weight/4
        elif self.vectX<0:
                self.vectX=0

        platform=0
        #print(self.pers[0].coord)
        for j in range(len(self.w["map"][0].pers)):
                        #print(self.w["map"].pers[j].coord)
                        if (self.pers[0].coord[1]<=self.w["map"][0].pers[j].coord[7] and
                            self.pers[0].coord[0]>self.w["map"][0].pers[j].coord[0] and
                           self.pers[0].coord[0]<self.w["map"][0].pers[j].coord[2] and
                           (self.pers[0].coord[1]>=self.w["map"][0].pers[j].coord[1]
                            or self.pers[0].coord[1]-self.vectY>=self.w["map"][0].pers[j].coord[7])
                           ):
                            #print('ovlp')
                            self.vectY=0
                            self.fly=False
                            break

        #print(self.vectY, self.vectX)
        if self.fly:
            self.vectY-=self.weight
        else:
            if(self.pers[0].coord[1]<self.w["map"][0].pers[platform].coord[7]):
                                d=self.w["map"][0].pers[platform].coord[7]-self.pers[0].coord[1]
                                for i in range(4):
                                    self.pers[0].coord[i*2+1]+=d
                                print('oops')
            #print(self.pers[0].coord)
            #elif(self.pers[0].coord[3]!=self.w["map"].pers[platform].coord[7]):
            #    d=self.w["map"].pers[platform].coord[7]-self.pers[0].coord[3]
            #    self.pers[0].coord[3]+=d
            #    self.pers[0].coord[5]+=d
        #print(self.pers[0],self.pers[0].coord)
        
    def isOverlap(self,w):
        pass
    

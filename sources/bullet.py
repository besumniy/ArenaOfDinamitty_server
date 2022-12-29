from AoD import *
from sources.element import *

class bullet():
    def __init__(self, x, y, a,b, o,t):
        self.vectX=x
        self.vectY=y
        self.attack=a
        self.pers=b
        self.owner=o
        self.touch=t
    def todo(self,s=None):
        for i in range(4):
            self.pers[0].coord[i*2]+=self.vectX
            self.pers[0].coord[i*2+1]+=self.vectY
    def isOverlap(self, w,s=None):
        if s:
                w=s

        for i in range(len(w['warriors'])):
            if(w['warriors'][i]!=self.owner):
                for g in range(len(w['warriors'][i].pers)):
                 if w['warriors'][i].pers[g]:
                    #if(self.pers[0].overlap(self.w["warriors"][i].pers[g])):
                    if(line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]-self.vectX,self.pers[0].coord[1]-self.vectY,w['warriors'][i].pers[g].coord[0],w['warriors'][i].pers[g].coord[1],w["warriors"][i].pers[g].coord[6],w["warriors"][i].pers[g].coord[7]) or                       
                       line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]-self.vectX,self.pers[0].coord[1]-self.vectY,w['warriors'][i].pers[g].coord[0],w['warriors'][i].pers[g].coord[1],w["warriors"][i].pers[g].coord[2],w["warriors"][i].pers[g].coord[3]) or
                       line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]-self.vectX,self.pers[0].coord[1]-self.vectY,w['warriors'][i].pers[g].coord[4],w['warriors'][i].pers[g].coord[5],w["warriors"][i].pers[g].coord[2],w["warriors"][i].pers[g].coord[3]) or
                       line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]-self.vectX,self.pers[0].coord[1]-self.vectY,w['warriors'][i].pers[g].coord[4],w['warriors'][i].pers[g].coord[5],w["warriors"][i].pers[g].coord[6],w["warriors"][i].pers[g].coord[7])
                       ):
                       hurting_hit(w['warriors'][i].pers[g],w['warriors'][i],self.attack[0])
                            #if(self.w["warriors"][i].pers[g].parent!=None):
                                #for j in range(len(w.warriors.get(i).pers[g].parent.child)):
                                 #   if(self.w["warriors"][i].pers[g].parent.child[j]==self.w["warriors"][i].pers[g]):
                                  #      self.w["warriors"][i].pers[g].parent.child[j]=None
                                   #     self.w["warriors"][g].pers[g].parent=None
                            #self.w["warriors"][i].pers[g].fly=True
                            #self.w["warriors"][i].pers[g].health=0
                       return True
        for i in range(len(w['map'][0].pers)):
            if(self.pers[0].overlap(w['map'][0].pers[i])):
                return  True
        return False

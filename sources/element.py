from AoD import *

import math

class element():

    #def __init__(self, img="", c=[0,0, 0,0, 0,0, 0,0],c1=[0,0, 0,0, 0,0, 0,0]):
    #   self.look=img
    #   self.coord=c
    #   self.coord1=c1
	#len=new float[4];     !!im not remember what is this!!
    def __init__(self):
        self.coord=[0,0,0,0,0,0,0,0]
        self.coord1=[0,0,0,0,0,0,0,0]
        self.len=[0,0,0,0]
        self.width=0
        self.height=0
        self.weight=0

        self.child=[]#element
        self.parent=None

        self.health=0
        self.max_health=0

        self.fly=False

        self.face=True
        self.rotation=0#

        self.look=""
    def calcF(self):
        self.coord[2]=self.coord[0]+self.width
        self.coord[3]=self.coord[1]
        self.coord[4]=self.coord[2]
        self.coord[5]=self.coord[3]+self.height
        self.coord[6]=self.coord[0]
        self.coord[7]=self.coord[5]
        self.rotation=0
        #self.face=True
    def calc(self):
        self.coord[2]=self.coord[0]-self.width
        self.coord[3]=self.coord[1]
        self.coord[4]=self.coord[2]
        self.coord[5]=self.coord[3]+self.height
        self.coord[6]=self.coord[0]
        self.coord[7]=self.coord[5]
        self.rotation=0
        #self.face=False
    def set_fareaF(self,u):
        self.coord1[0]=(self.coord[0]+math.cos(math.radians(45+u))*self.len[0])
        self.coord1[1]=(self.coord[1]+math.sin(math.radians(45+u))*self.len[0])
        self.coord1[2]=(self.coord[2]+math.cos(math.radians(135+u))*self.len[1])
        self.coord1[3]=(self.coord[3]+math.sin(math.radians(135+u))*self.len[1])
        self.coord1[4]=(self.coord[4]+math.cos(math.radians(-135+u))*self.len[2])
        self.coord1[5]=(self.coord[5]+math.sin(math.radians(-135+u))*self.len[2])
        self.coord1[6]=(self.coord[6]+math.cos(math.radians(-45+u))*self.len[3])
        self.coord1[7]=(self.coord[7]+math.sin(math.radians(-45+u))*self.len[3])
        self.rotation=u
        #self.face=True
    def set_farea(self,u):
        self.coord1[0]=(self.coord[0]-math.cos(math.radians(45+u))*self.len[0])
        self.coord1[1]=(self.coord[1]+math.sin(math.radians(45+u))*self.len[0])
        self.coord1[2]=(self.coord[2]-math.cos(math.radians(135+u))*self.len[1])
        self.coord1[3]=(self.coord[3]+math.sin(math.radians(135+u))*self.len[1])
        self.coord1[4]=(self.coord[4]-math.cos(math.radians(-135+u))*self.len[2])
        self.coord1[5]=(self.coord[5]+math.sin(math.radians(-135+u))*self.len[2])
        self.coord1[6]=(self.coord[6]-math.cos(math.radians(-45+u))*self.len[3])
        self.coord1[7]=(self.coord[7]+math.sin(math.radians(-45+u))*self.len[3])
        self.rotation=u
        #self.face=True
        
    
    def make_pointsF(self,u):
        self.coord1[2]=(self.coord[0]+math.cos(math.radians(u))*self.width)
        self.coord1[3]=(self.coord[0]+math.sin(math.radians(u))*self.height)
        self.coord1[4]=(self.coord[2]+math.cos(math.radians(90+u))*self.width)
        self.coord1[5]=(self.coord[3]+math.sin(math.radians(90+u))*self.height)
        self.coord1[6]=(self.coord[4]+math.cos(math.radians(180+u))*self.width)
        self.coord1[7]=(self.coord[5]+math.sin(math.radians(180+u))*self.height)
        self.rotation=u
    def make_points(self,u):
        self.coord1[2]=(self.coord[0]-math.cos(math.radians(u))*self.width)
        self.coord1[3]=(self.coord[0]+math.sin(math.radians(u))*self.height)
        self.coord1[4]=(self.coord[2]-math.cos(math.radians(90+u))*self.width)
        self.coord1[5]=(self.coord[3]+math.sin(math.radians(90+u))*self.height)
        self.coord1[6]=(self.coord[4]-math.cos(math.radians(180+u))*self.width)
        self.coord1[7]=(self.coord[5]+math.sin(math.radians(180+u))*self.height)
        self.rotation=u

    def overlap(self, el):
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[2],self.coord[3],el.coord[0],el.coord[1],el.coord[2],el.coord[3])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[2],self.coord[3],el.coord[0],el.coord[1],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[2],self.coord[3],el.coord[4],el.coord[5],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[2],self.coord[3],el.coord[2],el.coord[3],el.coord[4],el.coord[5])):
            return True

        if(line_overlaps(self.coord[0],self.coord[1],self.coord[6],self.coord[7],el.coord[0],el.coord[1],el.coord[2],el.coord[3])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[6],self.coord[7],el.coord[0],el.coord[1],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[6],self.coord[7],el.coord[4],el.coord[5],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[0],self.coord[1],self.coord[6],self.coord[7],el.coord[2],el.coord[3],el.coord[4],el.coord[5])):
            return True

        if(line_overlaps(self.coord[4],self.coord[5],self.coord[6],self.coord[7],el.coord[0],el.coord[1],el.coord[2],el.coord[3])):
            return True
        if(line_overlaps(self.coord[4],self.coord[5],self.coord[6],self.coord[7],el.coord[0],el.coord[1],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[4],self.coord[5],self.coord[6],self.coord[7],el.coord[4],el.coord[5],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[4],self.coord[5],self.coord[6],self.coord[7],el.coord[2],el.coord[3],el.coord[4],el.coord[5])):
            return True

        if(line_overlaps(self.coord[2],self.coord[3],self.coord[4],self.coord[5],el.coord[0],el.coord[1],el.coord[2],el.coord[3])):
            return True
        if(line_overlaps(self.coord[2],self.coord[3],self.coord[4],self.coord[5],el.coord[0],el.coord[1],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[2],self.coord[3],self.coord[4],self.coord[5],el.coord[4],el.coord[5],el.coord[6],el.coord[7])):
            return True
        if(line_overlaps(self.coord[2],self.coord[3],self.coord[4],self.coord[5],el.coord[2],el.coord[3],el.coord[4],el.coord[5])):
            return True

        return False
    def line_overlaps(self,x,y,x1,y1,x2,y2,x3,y3):
        v1=(x3-x2)*(y-y2)-(y3-y2)*(x-x2)
        v2=(x3-x2)*(y1-y2)-(y3-y2)*(x1-x2)
        v3=(x1-x)*(y2-y)-(y1-y)*(x2-x)
        v4=(x1-x)*(y3-y)-(y1-y)*(x3-x)
        return (v1*v2<0) and (v3*v4)<0
        

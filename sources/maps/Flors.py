from sources.element import *
from sources.Map import *

class Area(Map):
    def __init__(self,w,h):
        super().__init__(w,h)
        
        #self.wall="images\\control fone.png"
        self.background="images//maps//Flors//background.png"

        self.pers=[element() for i in range(13)]
                   
        #middle floor plate
        self.pers[0].height= self.height/10
        self.pers[0].width=self.width
        self.pers[0].coord[1]=self.height+self.pers[0].height
        self.pers[0].coord[0]=0
        self.pers[0].calcF()

        self.pers[1].height=self.pers[0].height
        self.pers[1].width=self.pers[0].width
        self.pers[1].coord[0]=self.pers[0].coord[2]+self.pers[0].height*3
        self.pers[1].coord[1]=self.pers[0].coord[1]
        self.pers[1].calcF()

        self.pers[2].height=self.pers[0].height
        self.pers[2].width=self.pers[0].width
        self.pers[2].coord[0]=self.pers[0].coord[0]-self.pers[0].width-self.pers[0].height*3
        self.pers[2].coord[1]=self.pers[0].coord[1]
        self.pers[2].calcF()

        #down floor plate
        self.pers[3].height=self.pers[0].height
        self.pers[3].width=self.pers[0].width
        self.pers[3].coord[0]=self.pers[0].coord[0]
        self.pers[3].coord[1]=self.pers[0].coord[1]-self.pers[0].height-self.height
        self.pers[3].calcF()

        self.pers[4].height=self.pers[0].height
        self.pers[4].width=self.pers[0].width
        self.pers[4].coord[0]=self.pers[1].coord[0]
        self.pers[4].coord[1]=self.pers[3].coord[1]
        self.pers[4].calcF()

        self.pers[5].height=self.pers[0].height
        self.pers[5].width=self.pers[0].width
        self.pers[5].coord[0]=self.pers[2].coord[0]
        self.pers[5].coord[1]=self.pers[3].coord[1]
        self.pers[5].calcF()
        
        #up floor plate
        self.pers[6].height=self.pers[0].height
        self.pers[6].width=self.pers[0].width
        self.pers[6].coord[0]=self.pers[0].coord[0]
        self.pers[6].coord[1]=self.pers[0].coord[1]+self.pers[0].height+self.height
        self.pers[6].calcF()

        self.pers[7].height=self.pers[0].height
        self.pers[7].width=self.pers[0].width
        self.pers[7].coord[0]=self.pers[1].coord[0]
        self.pers[7].coord[1]=self.pers[6].coord[1]
        self.pers[7].calcF()

        self.pers[8].height=self.pers[0].height
        self.pers[8].width=self.pers[0].width
        self.pers[8].coord[0]=self.pers[2].coord[0]
        self.pers[8].coord[1]=self.pers[6].coord[1]
        self.pers[8].calcF()
        
        #gates
        self.pers[9].height=self.height+self.pers[0].height*2
        self.pers[9].width=self.pers[0].height*3
        self.pers[9].coord[0]=self.pers[2].coord[0]-self.pers[9].width
        self.pers[9].coord[1]=self.pers[3].coord[1]
        self.pers[9].calcF()
        
        self.pers[10].height=self.pers[9].height
        self.pers[10].width=self.pers[9].width
        self.pers[10].coord[0]=self.pers[2].coord[2]
        self.pers[10].coord[1]=self.pers[3].coord[1]
        self.pers[10].calcF()
        
        self.pers[11].height=self.pers[9].height
        self.pers[11].width=self.pers[9].width
        self.pers[11].coord[0]=self.pers[0].coord[2]
        self.pers[11].coord[1]=self.pers[3].coord[1]
        self.pers[11].calcF()
        
        self.pers[12].height=self.pers[9].height
        self.pers[12].width=self.pers[9].width
        self.pers[12].coord[0]=self.pers[1].coord[2]
        self.pers[12].coord[1]=self.pers[3].coord[1]
        self.pers[12].calcF()

        for i in range(13):
            self.pers[i].look=self.wall
            self.pers[i].face=True

        self.move=self.height/100
        
        self.places=[(self.pers[0].coord[6]+150,self.pers[0].coord[7]+10, 1),
            (self.pers[0].coord[4]-150,self.pers[0].coord[7]+10,0)]
            
    def todo(self,w):
        super().todo(w)
        
        for i in range(9,13):
            self.pers[i].coord[1]+=self.move
            self.pers[i].coord[3]+=self.move
            self.pers[i].coord[5]+=self.move
            self.pers[i].coord[7]+=self.move
            
        if self.pers[9].coord[7]==self.pers[3].coord[7] or self.pers[9].coord[7]==self.pers[6].coord[7]:
            self.move=-self.move
            
        if self.move>0:
         for i in range(9,13):
            for warrior in w['warriors']:
               if not warrior.fly:
                if self.pers[i]==w['map'][0].pers[warrior.platform]:
                    for elem in warrior.pers:
                        elem.coord[1]+=self.move
                        elem.coord[3]+=self.move
                        elem.coord[5]+=self.move
                        elem.coord[7]+=self.move

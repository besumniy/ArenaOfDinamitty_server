from sources.element import *
from sources.Map import *

class Area(Map):
    def __init__(self,w,h):
        super().__init__(w,h)
        
        self.wall="images\\control fone.png"

        self.pers=[element(),
                   element(),
                   element(),
                   element(),
                   element(),
                   element()]
        self.pers[0].height= self.height/10
        self.pers[0].width=self.pers[0].height*100
        self.pers[0].coord[1]=-self.pers[0].height
        self.pers[0].coord[0]=0
        self.pers[0].calcF()

        self.pers[1].height=self.pers[0].height*8
        self.pers[1].width=self.pers[0].height
        self.pers[1].coord[0]=self.pers[0].coord[4]-self.pers[0].width*0.8#
        self.pers[1].coord[1]=self.pers[0].coord[5]
        self.pers[1].calcF()

        self.pers[2].height=self.pers[0].height
        self.pers[2].width=self.pers[2].height*10
        self.pers[2].coord[0]=self.pers[2].height*45
        self.pers[2].coord[1]=self.pers[2].height*7
        self.pers[2].calcF()

        self.pers[3].height=self.pers[0].height
        self.pers[3].width=self.pers[2].width*10
        self.pers[3].coord[0]=-self.pers[3].width
        self.pers[3].coord[1]=-self.pers[3].height*1.5
        self.pers[3].calcF()

        self.pers[4].height=self.pers[0].height
        self.pers[4].width=self.pers[2].width
        self.pers[4].coord[0]=self.pers[0].coord[0]-self.pers[4].width*2
        self.pers[4].coord[1]=self.pers[0].coord[1]
        self.pers[4].calcF()

        self.pers[5].height=self.pers[0].height*8
        self.pers[5].width=self.pers[0].height
        self.pers[5].coord[0]=self.pers[4].coord[0]
        self.pers[5].coord[1]=self.pers[0].coord[1]
        self.pers[5].calcF()

        for i in range(6):
            self.pers[i].look=self.wall
            self.pers[i].face=True

        self.places=[(self.pers[0].coord[6],self.pers[0].coord[7], 1),
            (self.pers[0].coord[6]+self.pers[0].width/10,self.pers[0].coord[7],0)]
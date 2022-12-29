from sources.element import *
from sources.Map import *

class Area(Map):
    def __init__(self,w,h):
        super().__init__(w,h)
        
        #self.wall="images\\control fone.png"
        self.background="images//maps//Saint hole//background.png"
        self.heal_frame=1
        self.max_heal_frame=2

        self.pers=[element() for i in range(3)]
        
        self.pers[0].height= self.height/10
        self.pers[0].width=self.width*3
        self.pers[0].coord[1]=0
        self.pers[0].coord[0]=-self.pers[0].height#-self.width
        self.pers[0].calcF()

        self.pers[1].height=self.height*3
        self.pers[1].width=self.pers[0].height
        self.pers[1].coord[0]=self.pers[0].coord[0]-self.pers[1].width#
        self.pers[1].coord[1]=self.pers[0].coord[1]
        self.pers[1].calcF()

        self.pers[2].height=self.pers[1].height
        self.pers[2].width=self.pers[1].width
        self.pers[2].coord[0]=self.pers[0].coord[2]
        self.pers[2].coord[1]=self.pers[0].coord[3]
        self.pers[2].calcF()
        
        healing=element()
        healing.height=self.height
        healing.width=self.width
        healing.coord[0]=0
        healing.coord[1]=self.pers[0].height
        healing.look='images//maps//Saint hole//heal1.png'
        healing.calcF()
        healing.face=True
        self.extra_texture.append(healing)
        
        for i in range(3):
            self.pers[i].look=self.wall
            self.pers[i].face=True

        self.places=[(0,self.pers[0].coord[7]+10, 1),
            (self.width-150,self.pers[0].coord[7]+10,0)]
            
    def todo(self,w):
        super().todo(w)
        self.animation()
        
        for warrior in w['warriors']:
            for peace in warrior.pers:
             if peace:
                if point_in_rect(peace.coord[0],peace.coord[1],self.extra_texture[0]):
                    peace.health+=1
                if peace.health>peace.max_health:
                    peace.health=peace.max_health
        
    def animation(self):
        self.heal_frame+=1
        if self.heal_frame>self.max_heal_frame:
            self.heal_frame=1
        self.extra_texture[0].look='images//maps//Saint hole//heal'+str(self.heal_frame)+'.png'
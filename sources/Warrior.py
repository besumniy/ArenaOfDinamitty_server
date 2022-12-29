from sources.element import *

class warrior():
    def __init__(self, start,word,w,h,):
        self.width=1500
        self.client_width=w
        self.height=1000
        self.client_height=h
        self.scale=h/1000##
        print('scale:',self.scale)
        print('width:',w)
        self.a=self.height/100
        self.game_area_width=(h*1.5)
        self.side_w=(w-self.game_area_width)/3
        self.side1_x=self.game_area_width+self.side_w*2
        self.icon_size=self.side_w
        self.icon_x=self.side1_x
        self.vectX=0
        self.vectY=0
        self.w=word

        self.enemies=[]
        self.client_game_area_width=(h*1.5)
        self.client_side_w=(w-self.client_game_area_width)/3
        self.client_side1_x=self.client_game_area_width+self.client_side_w*2

        self.rdW=self.client_game_area_width-2*self.icon_size
        self.rdH=self.rdW/3
        self.rdX=(self.client_game_area_width-self.rdW)/2+self.client_side_w*2
        self.rdY=self.height/2-self.icon_size
        self.dokH=self.rdH/4
        self.dokW=self.rdW/3
        self.dokX=self.rdX+2*self.dokW
        self.dokY=self.rdY+self.rdH-self.dokH-self.icon_size/10
        self.messages=[{'a':False,'x':self.rdX,'y':self.rdY,'w':self.rdW,'h':self.rdH,'l':''},
                       {'a':False,'x':self.dokX,'y':self.dokY,'w':self.dokW,'h':self.dokH,'l':'images//exit.png'},
                       {'a':False,'x':self.dokX,'y':self.dokY-self.dokH,'w':self.dokW,'h':self.dokH,'l':'images//watch.png'}
                       ]

        self.dmgd=0
        self.DAMAGED_FRAME=60
        
        self.darkness=[]

    def buildBody(self,x,y):
        self.fly=True
        if self.face:
         self.pers[0].coord[0]=x
         self.pers[0].coord[1]=y
         self.pers[0].calcF()
         self.pers[0].set_fareaF(0)
         if self.pers[1]:
            self.pers[1].coord[0]=self.pers[0].coord[6]-(self.pers[1].width-self.pers[0].width)/2
            self.pers[1].coord[1]=self.pers[0].coord[1]-self.pers[1].height
            self.pers[1].calcF()
            self.pers[1].set_fareaF(0)

            if self.pers[2]:
                    self.pers[2].coord[6]=self.pers[1].coord[6]
                    self.pers[2].coord[7]=self.pers[1].coord[7]
                    self.pers[2].coord[0]=self.pers[2].coord[6]+math.cos(math.radians(225))*self.pers[2].height
                    self.pers[2].coord[1]=self.pers[2].coord[7]+math.sin(math.radians(225))*self.pers[2].height
                    self.pers[2].coord[2]=self.pers[2].coord[0]+math.cos(math.radians(315))*self.pers[2].width
                    self.pers[2].coord[3]=self.pers[2].coord[1]+math.sin(math.radians(315))*self.pers[2].width
                    self.pers[2].coord[4]=self.pers[2].coord[2]+math.cos(math.radians(45))*self.pers[2].height
                    self.pers[2].coord[5]=self.pers[2].coord[3]+math.sin(math.radians(45))*self.pers[2].height
                    self.pers[2].set_fareaF(135)

                    if self.pers[3]:
                            self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                            self.pers[3].coord[0]=self.pers[2].coord[0]
                            self.pers[3].calcF()
                            self.pers[3].set_fareaF(0)

            if self.pers[4]:
                    self.pers[4].coord[4]=self.pers[1].coord[4]
                    self.pers[4].coord[5]=self.pers[1].coord[5]
                    self.pers[4].coord[6]=self.pers[4].coord[4]+math.cos(math.radians(225))*self.pers[4].width
                    self.pers[4].coord[7]=self.pers[4].coord[5]+math.sin(math.radians(225))*self.pers[4].width
                    self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(315))*self.pers[4].height
                    self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(315))*self.pers[4].height
                    self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(45))*self.pers[4].width
                    self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(45))*self.pers[4].width
                    self.pers[4].set_fareaF(45)

                    if self.pers[5]:
                            self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                            self.pers[5].coord[0]=self.pers[4].coord[0]
                            self.pers[5].calcF()
                            self.pers[5].set_fareaF(0)
            if self.pers[6]:
                    self.pers[6].coord[6]=self.pers[1].coord[0]+(self.pers[1].width-self.pers[7].width*3)/2
                    self.pers[6].coord[7]=self.pers[1].coord[1]
            if self.pers[8]:
                    self.pers[8].coord[6]=self.pers[6].coord[6]+self.pers[7].width*2
                    self.pers[8].coord[7]=self.pers[1].coord[1]

         for wall in self.w["map"][0].pers:
                    if((wall.coord[0]<self.pers[1].coord[2] and wall.coord[0]>self.pers[1].coord[2]-self.pers[1].width)or
                       (wall.coord[6]<self.pers[1].coord[2] and wall.coord[6]>self.pers[1].coord[2]-self.pers[1].width)or
                       (wall.coord[0]<self.pers[0].coord[2] and wall.coord[0]>self.pers[0].coord[2]-self.pers[0].width)or
                       (wall.coord[6]<self.pers[0].coord[2] and wall.coord[6]>self.pers[0].coord[2]-self.pers[0].width) ):#add leg
                            d=wall.coord[0]-self.pers[1].coord[2]
                            for g in range(10):
                             if self.pers[g]:
                                for j in range(0,7,2):
                                    self.pers[g].coord[j]+=d
                                    self.pers[g].coord1[j]+=d
                            break
         for i in range(10):
             if self.pers[i]:
                    self.pers[i].face=True
        else:
         if self.pers[0]:
          self.pers[0].coord[0]=x
          self.pers[0].coord[1]=y
          self.pers[0].calc()
          self.pers[0].set_farea(0)
          if self.pers[1]:
            self.pers[1].coord[0]=self.pers[0].coord[6]+(self.pers[1].width-self.pers[0].width)/2
            self.pers[1].coord[1]=self.pers[0].coord[1]-self.pers[1].height
            self.pers[1].calc()
            self.pers[1].set_farea(0)

            if self.pers[4]:
                    self.pers[4].coord[6]=self.pers[1].coord[4]
                    self.pers[4].coord[7]=self.pers[1].coord[5]
                    self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(225))*self.pers[4].height
                    self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(225))*self.pers[4].height
                    self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(315))*self.pers[4].width
                    self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(315))*self.pers[4].width
                    self.pers[4].coord[4]=self.pers[4].coord[2]+math.cos(math.radians(45))*self.pers[4].height
                    self.pers[4].coord[5]=self.pers[4].coord[3]+math.sin(math.radians(45))*self.pers[4].height
                    self.pers[4].set_farea(45)

                    if self.pers[5]:
                            self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                            self.pers[5].coord[0]=self.pers[4].coord[2]
                            self.pers[5].calc()
                            self.pers[5].set_farea(0)
            if self.pers[2]:
                    self.pers[2].coord[4]=self.pers[1].coord[6]
                    self.pers[2].coord[5]=self.pers[1].coord[7]
                    self.pers[2].coord[6]=self.pers[2].coord[4]+math.cos(math.radians(225))*self.pers[2].width
                    self.pers[2].coord[7]=self.pers[2].coord[5]+math.sin(math.radians(225))*self.pers[2].width
                    self.pers[2].coord[0]=self.pers[2].coord[6]+math.cos(math.radians(315))*self.pers[2].height
                    self.pers[2].coord[1]=self.pers[2].coord[7]+math.sin(math.radians(315))*self.pers[2].height
                    self.pers[2].coord[2]=self.pers[2].coord[0]+math.cos(math.radians(45))*self.pers[2].width
                    self.pers[2].coord[3]=self.pers[2].coord[1]+math.sin(math.radians(45))*self.pers[2].width
                    self.pers[2].set_farea(135)

                    if self.pers[3]:
                            self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                            self.pers[3].coord[0]=self.pers[2].coord[2]
                            self.pers[3].calc()
                            self.pers[3].set_farea(0)

            if self.pers[6]:
                    self.pers[6].coord[6]=self.pers[1].coord[0]-(self.pers[1].width-self.pers[7].width*3)/2
                    self.pers[6].coord[7]=self.pers[1].coord[1]
            if self.pers[8]:
                    self.pers[8].coord[6]=self.pers[6].coord[6]-self.pers[6].width*2
                    self.pers[8].coord[7]=self.pers[1].coord[1]

            for wall in self.w["map"][0].pers:
                    if self.pers[1].overlap(wall):
                        self.fly=False
                    if((wall.coord[2]>self.pers[1].coord[2] and wall.coord[2]<self.pers[1].coord[2]+self.pers[1].width)or
                       (wall.coord[4]>self.pers[1].coord[2] and wall.coord[4]<self.pers[1].coord[2]+self.pers[1].width)or
                       (wall.coord[2]>self.pers[0].coord[2] and wall.coord[2]<self.pers[0].coord[2]+self.pers[0].width)or
                       (wall.coord[4]>self.pers[0].coord[2] and wall.coord[4]<self.pers[0].coord[2]+self.pers[0].width) ):
                            d=wall.coord[2]-self.pers[1].coord[2]
                            for g in range(10):
                             if self.pers[g]:
                                for j in range(0,7,2):
                                    self.pers[g].coord[j]+=d
                                    self.pers[g].coord1[j]+=d
                            break
         for i in range(10):
            if self.pers[i]:
                    self.pers[i].face=False
        

    
    
    
    def goLeft(self):
        m=self.w["map"][0]
        if(not self.fly and not self.legkick and self.pers[1] and self.pers[6] and self.pers[8]):
            r=True
            if(not self.face):
                for i in range(len(m.pers)):
                    if(
			(self.pers[1].coord[3]>m.pers[i].coord[1] and self.pers[1].coord[3]<m.pers[i].coord[7] and self.pers[1].coord[4]<m.pers[i].coord[2] and self.pers[1].coord[4]+self.go>=m.pers[i].coord[2])or
			(self.pers[1].coord[5]>m.pers[i].coord[1] and self.pers[1].coord[5]<m.pers[i].coord[7] and self.pers[1].coord[4]<m.pers[i].coord[2] and self.pers[1].coord[4]+self.go>=m.pers[i].coord[2])or
			(self.pers[0].coord[3]>m.pers[i].coord[0] and self.pers[1].coord[3]<m.pers[i].coord[7] and self.pers[0].coord[4]<m.pers[i].coord[2] and self.pers[0].coord[4]+self.go>=m.pers[i].coord[2])or
			(self.pers[0].coord[5]>m.pers[i].coord[0] and self.pers[1].coord[5]<m.pers[i].coord[7] and self.pers[0].coord[4]<m.pers[i].coord[2] and self.pers[0].coord[4]+self.go>=m.pers[i].coord[2])
			):
                        r=False
                        break
            else:
                for i in range(len(m.pers)):
                    if(
                        (self.pers[1].coord[1]>m.pers[i].coord[1] and self.pers[1].coord[1]<m.pers[i].coord[7] and self.pers[1].coord[0]<m.pers[i].coord[2] and self.pers[1].coord[0]+self.go>=m.pers[i].coord[2])or
                        (self.pers[1].coord[7]>m.pers[i].coord[1] and self.pers[1].coord[7]<m.pers[i].coord[7] and self.pers[1].coord[0]<m.pers[i].coord[2] and self.pers[1].coord[0]+self.go>=m.pers[i].coord[2])or
                        (self.pers[0].coord[1]>m.pers[i].coord[0] and self.pers[1].coord[1]<m.pers[i].coord[7] and self.pers[0].coord[0]<m.pers[i].coord[2] and self.pers[0].coord[0]+self.go>=m.pers[i].coord[2])or
                        (self.pers[0].coord[7]>m.pers[i].coord[0] and self.pers[1].coord[7]<m.pers[i].coord[7] and self.pers[0].coord[0]<m.pers[i].coord[2] and self.pers[0].coord[0]+self.go>=m.pers[i].coord[2])
                        ) or not (self.pers[7] or self.pers[9]):
                        r=False
                        break
            if(r):
                for i in range(6):
                 if(self.pers[i]):
                    for g in range(0,7,2):
                        self.pers[i].coord[g]-=self.go
                        self.pers[i].coord1[g]-=self.go
            self.i+=1
            if(self.i>30):
                self.i=-29
            u=0

            if(self.face):
                if(self.i>0):
                    if(self.i<16):
                        u=self.i*5
                    else:
                        u=(30-self.i)*5
                    if(self.pers[6]):
                            if(r):
                                self.pers[6].coord[6]-=self.go
                            self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[6].width
                            self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[6].width
                            self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[6].height
                            self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[6].height
                            self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[6].width
                            self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[6].width
                            self.pers[6].set_fareaF(u+self.ud)

                            if(self.pers[7]):
                                    self.pers[7].coord[6]=self.pers[6].coord[0]
                                    self.pers[7].coord[7]=self.pers[6].coord[1]
                                    self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[7].width
                                    self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[7].width
                                    self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[7].height
                                    self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[7].height
                                    self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[7].width
                                    self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[7].width
                                    self.pers[7].set_fareaF(u+self.ud)

                    u=-u

                    if(self.pers[8]):
                            if(r):
                                self.pers[8].coord[6]-=self.go
                            self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2+self.ud))*self.pers[8].width
                            self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2+self.ud))*self.pers[8].width
                            self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90+self.ud))*self.pers[8].height
                            self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90+self.ud))*self.pers[8].height
                            self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-180+self.ud))*self.pers[8].width
                            self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-180+self.ud))*self.pers[8].width
                            self.pers[8].set_fareaF(u/2+self.ud)

                            if(self.pers[9]):
                                    self.pers[9].coord[6]=self.pers[8].coord[0]
                                    self.pers[9].coord[7]=self.pers[8].coord[1]
                                    self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-self.ud1))*self.pers[9].width
                                    self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-self.ud1))*self.pers[9].width
                                    self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[9].height
                                    self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[9].height
                                    self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-180-self.ud1))*self.pers[9].width
                                    self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-180-self.ud1))*self.pers[9].width
                                    self.pers[9].set_fareaF(u+-self.ud1)
                else:
                    if(self.i<-14):
                        u=(30+self.i)*5
                    else:
                        u=self.i*-5
                    if(self.pers[8]):
                            if(r):
                                self.pers[8].coord[6]-=self.go
                            self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[8].width
                            self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[8].width
                            self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[8].height
                            self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[8].height
                            self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[8].width
                            self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[8].width
                            self.pers[8].set_fareaF(u+self.ud)

                            if(self.pers[9]):
                                    self.pers[9].coord[6]=self.pers[8].coord[0]
                                    self.pers[9].coord[7]=self.pers[8].coord[1]
                                    self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[9].width
                                    self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[9].width
                                    self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[9].height
                                    self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[9].height
                                    self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[9].width
                                    self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[9].width
                                    self.pers[9].set_fareaF(u+self.ud)

                    u=-u

                    if(self.pers[6]):
                            if(r):
                                self.pers[6].coord[6]-=self.go
                            self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u/2+self.ud))*self.pers[6].width
                            self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u/2+self.ud))*self.pers[6].width
                            self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u/2-90+self.ud))*self.pers[6].height
                            self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u/2-90+self.ud))*self.pers[6].height
                            self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u/2-180+self.ud))*self.pers[6].width
                            self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u/2-180+self.ud))*self.pers[6].width
                            self.pers[6].set_fareaF(u/2+self.ud)

                            if(self.pers[7]):
                                    self.pers[7].coord[6]=self.pers[6].coord[0]
                                    self.pers[7].coord[7]=self.pers[6].coord[1]
                                    self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-self.ud1))*self.pers[7].width
                                    self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-self.ud1))*self.pers[7].width
                                    self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[7].height
                                    self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[7].height
                                    self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-180-self.ud1))*self.pers[7].width
                                    self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-180-self.ud1))*self.pers[7].width
                                    self.pers[7].set_fareaF(u-self.ud1)

                if(self.pers[6]):
                        down_pos=self.pers[1].coord[1]-self.pers[7].height-self.pers[6].height+self.pers[0].height/10*self.s
                        for i in range(len(m.pers)):
                            if(i!=self.platform):
                                if(self.pers[7].coord[0]>m.pers[i].coord[0] and self.pers[7].coord[0]<=m.pers[i].coord[2] and self.pers[7].coord[1]+self.pers[7].height>=m.pers[i].coord[7] and self.pers[7].coord[1]<=m.pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=m.pers[i].coord[7]-down_pos
                                    self.coordY+=d
                                    for g in range(10):
                                     if self.pers[g]:
                                        for j in range(1,9,2):
                                            self.pers[g].coord[j]+=d
                                            self.pers[g].coord1[j]+=d
                                    self.platform=i
                else:
                        pass##!!!! if self.pers[7] else

            else:
                if(self.i>0):
                    if(self.i<16):
                        u=self.i*5
                    else:
                        u=(30-self.i)*5
                    if(r):
                        self.pers[6].coord[6]-=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].set_farea(u/2-self.ud)

                    if(self.pers[7]):
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].set_farea(u+self.ud1)

                    u=-u
                    if(r):
                        self.pers[8].coord[6]-=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].set_farea(u-self.ud)

                    if(self.pers[9]):
                            self.pers[9].coord[0]=self.pers[8].coord[2]+self.pers[9].width
                            self.pers[9].coord[1]=self.pers[8].coord[3]-self.pers[9].height
                            self.pers[9].calc()
                            self.pers[9].set_farea(0)
                else:
                    if(self.i<-14):
                        u=(30+self.i)*5
                    else:
                        u=self.i*-5
                    if(r):
                        self.pers[8].coord[6]-=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[8].width
                    self.pers[8].set_farea(u/2-self.ud)

                    if(self.pers[9]):
                            self.pers[9].coord[6]=self.pers[8].coord[0]
                            self.pers[9].coord[7]=self.pers[8].coord[1]
                            self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-180+self.ud1))*self.pers[9].width
                            self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-180+self.ud1))*self.pers[9].width
                            self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[9].height
                            self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[9].height
                            self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u+self.ud1))*self.pers[9].width
                            self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u+self.ud1))*self.pers[9].width
                            self.pers[9].set_farea(u+self.ud1)

                    u=-u

                    if(r):
                        self.pers[6].coord[6]-=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[6].width
                    self.pers[6].set_farea(u-self.ud)

                    if(self.pers[7]):
                            self.pers[7].coord[0]=self.pers[6].coord[2]+self.pers[7].width
                            self.pers[7].coord[1]=self.pers[6].coord[3]-self.pers[7].height
                            self.pers[7].calc()
                            self.pers[7].set_farea(0)

                if(self.pers[8]):
                        down_pos=self.pers[1].coord[1]-self.pers[9].height-self.pers[8].height+self.pers[0].height/10*self.s
                        for i in range(len(m.pers)):
                            if(i!=self.platform):
                                if(self.pers[9].coord[2]>m.pers[i].coord[0] and self.pers[9].coord[2]<=m.pers[i].coord[2] and self.pers[9].coord[3]+self.pers[9].height>=m.pers[i].coord[7] and self.pers[9].coord[3]<=m.pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=m.pers[i].coord[7]-down_pos
                                    self.coordY+=d
                                    for g in range(10):
                                     if self.pers[g]:
                                        for j in range(1,9,2):
                                            self.pers[g].coord[j]+=d
                                            self.pers[g].coord1[j]+=d
                                    self.platform=i
                else:
                        pass ###
        else:
                pass ### 6,8 nothing

    def goRight(self):
        m=self.w["map"][0]
        if(not self.fly and not self.legkick and self.pers[1] and self.pers[6] and self.pers[8]):
            r=True
            #level=0#
            if(self.face):
                for i in range(len(m.pers)):
                    if(
			(self.pers[1].coord[3]>m.pers[i].coord[1] and self.pers[1].coord[3]<m.pers[i].coord[7] and self.pers[1].coord[4]>m.pers[i].coord[0] and self.pers[1].coord[4]-self.go<=m.pers[i].coord[0])or
			(self.pers[1].coord[5]>m.pers[i].coord[1] and self.pers[1].coord[5]<m.pers[i].coord[7] and self.pers[1].coord[4]>m.pers[i].coord[0] and self.pers[1].coord[4]-self.go<=m.pers[i].coord[0])or
			(self.pers[0].coord[3]>m.pers[i].coord[0] and self.pers[1].coord[3]<m.pers[i].coord[7] and self.pers[0].coord[4]>m.pers[i].coord[0] and self.pers[0].coord[4]-self.go<=m.pers[i].coord[0])or
			(self.pers[0].coord[5]>m.pers[i].coord[0] and self.pers[1].coord[5]<m.pers[i].coord[7] and self.pers[0].coord[4]>m.pers[i].coord[0] and self.pers[0].coord[4]-self.go<=m.pers[i].coord[0])
			) or not(self.pers[9] or self.pers[7]):
                        r=False
                        break

            else:
                for i in range(len(m.pers)):
                    if(
                        (self.pers[1].coord[1]>m.pers[i].coord[1] and self.pers[1].coord[1]<m.pers[i].coord[7] and self.pers[1].coord[0]>m.pers[i].coord[0] and self.pers[1].coord[0]-self.go<=m.pers[i].coord[0])or
                        (self.pers[1].coord[7]>m.pers[i].coord[1] and self.pers[1].coord[7]<m.pers[i].coord[7] and self.pers[1].coord[0]>m.pers[i].coord[0] and self.pers[1].coord[0]-self.go<=m.pers[i].coord[0])or
                        (self.pers[0].coord[1]>m.pers[i].coord[0] and self.pers[1].coord[1]<m.pers[i].coord[7] and self.pers[0].coord[0]>m.pers[i].coord[0] and self.pers[0].coord[0]-self.go<=m.pers[i].coord[0])or
                        (self.pers[0].coord[7]>m.pers[i].coord[0] and self.pers[1].coord[7]<m.pers[i].coord[7] and self.pers[0].coord[0]>m.pers[i].coord[0] and self.pers[0].coord[0]-self.go<=m.pers[i].coord[0])
                        ) or not(self.pers[9] or self.pers[7]):
                        r=False
                        break
            if(r):
                for i in range(6):
                 if self.pers[i]:
                    for g in range(0,7,2):
                        self.pers[i].coord[g]+=self.go
                        self.pers[i].coord1[g]+=self.go
            self.i+=1
            if(self.i>30):
                self.i=-29
            u=0

            if(not self.face):
                #level=self.pers[7].coord[1]
                if(self.i>0):
                    if(self.i<16):
                        u=self.i*5
                    else:
                        u=(30-self.i)*5
                    if(r):
                        self.pers[6].coord[6]+=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].set_fareaF(u/1-self.ud)

                    if self.pers[7]:
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].set_fareaF(u+self.ud1)

                    u=-u
                    if(r):
                        self.pers[8].coord[6]+=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].set_fareaF(u-self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[6]=self.pers[8].coord[0]
                            self.pers[9].coord[7]=self.pers[8].coord[1]
                            self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[9].width
                            self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[9].width
                            self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[9].height
                            self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[9].height
                            self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[9].width
                            self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[9].width
                            self.pers[9].set_fareaF(u-self.ud)
                else:
                    if(self.i<-14):
                        u=(30+self.i)*5
                    else:
                        u=self.i*-5
                    if(r):
                        self.pers[8].coord[6]+=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[8].width
                    self.pers[8].set_fareaF(u/2-self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[6]=self.pers[8].coord[0]
                            self.pers[9].coord[7]=self.pers[8].coord[1]
                            self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-180+self.ud1))*self.pers[9].width
                            self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-180+self.ud1))*self.pers[9].width
                            self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[9].height
                            self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[9].height
                            self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u+self.ud1))*self.pers[9].width
                            self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u+self.ud1))*self.pers[9].width
                            self.pers[9].set_fareaF(u+self.ud1)

                    u=-u
                    if(r):
                        self.pers[6].coord[6]+=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[6].width
                    self.pers[6].set_fareaF(u-self.ud)

                    if self.pers[7]:
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[7].width
                            self.pers[7].set_fareaF(u-self.ud)

                if(self.pers[7]):
                        down_pos=self.pers[1].coord[1]-self.pers[7].height-self.pers[6].height+self.pers[0].height/10*self.s
                        for i in range(len(m.pers)):
                            if(i!=self.platform):
                                if(self.pers[7].coord[0]>m.pers[i].coord[0] and self.pers[7].coord[0]<=m.pers[i].coord[2] and self.pers[7].coord[1]+self.pers[7].height>=m.pers[i].coord[7] and self.pers[7].coord[1]<=m.pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=m.pers[i].coord[7]-down_pos
                                    self.coordY+=d
                                    for g in range(10):
                                     if self.pers[g]:
                                        for j in range(1,9,2):
                                            self.pers[g].coord[j]+=d
                                            self.pers[g].coord1[j]+=d
                                    self.platform=i
                else:
                        pass#

            else:
                #level=self.pers[9].coord[3]
                if(self.i>0):
                    if(self.i<16):
                        u=self.i*-5
                    else:
                        u=(30-self.i)*-5
                    if(r):
                        self.pers[6].coord[6]+=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[6].width
                    self.pers[6].set_farea(u/2+self.ud)###not face

                    if self.pers[7]:
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-self.ud1))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-self.ud1))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-180-self.ud1))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-180-self.ud1))*self.pers[7].width
                            self.pers[7].set_farea(u-self.ud1)
                    #print('grrr')
                    #print(r)
                    #print(u-self.ud1)
                    #print(self.pers[6].coord)

                    u=-u
                    if(r):
                        self.pers[8].coord[6]+=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[8].width
                    self.pers[8].set_farea(u+self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[0]=self.pers[8].coord[2]-self.pers[9].width
                            self.pers[9].coord[1]=self.pers[8].coord[3]-self.pers[9].height
                            self.pers[9].calcF()
                            self.pers[9].set_fareaF(0)#changed
                else:
                    if(self.i<-14):
                        u=(30+self.i)*-5
                    else:
                        u=self.i*5
                    if(r):
                        self.pers[8].coord[6]+=self.go
                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2+self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2+self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-180+self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-180+self.ud))*self.pers[8].width
                    self.pers[8].set_farea(u/2+self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[6]=self.pers[8].coord[0]
                            self.pers[9].coord[7]=self.pers[8].coord[1]
                            self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-self.ud1))*self.pers[9].width
                            self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-self.ud1))*self.pers[9].width
                            self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[9].height
                            self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[9].height
                            self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-180-self.ud1))*self.pers[9].width
                            self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-180-self.ud1))*self.pers[9].width
                            self.pers[9].set_farea(u-self.ud1)

                    u=-u

                    if(r):
                        self.pers[6].coord[6]+=self.go
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[6].width
                    self.pers[6].set_farea(u+self.ud)

                    if self.pers[7]:
                            self.pers[7].coord[0]=self.pers[6].coord[2]-self.pers[7].width
                            self.pers[7].coord[1]=self.pers[6].coord[3]-self.pers[7].height
                            self.pers[7].calcF()
                            self.pers[7].set_fareaF(0)#
                if self.pers[9]:
                        down_pos=self.pers[1].coord[1]-self.pers[9].height-self.pers[8].height+self.pers[0].height/10*self.s
                        for i in range(len(m.pers)):
                            if(i!=self.platform):
                                if(self.pers[9].coord[2]>m.pers[i].coord[0] and self.pers[9].coord[2]<=m.pers[i].coord[2] and self.pers[9].coord[3]+self.pers[9].height>=m.pers[i].coord[7] and self.pers[9].coord[3]<=m.pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=m.pers[i].coord[7]-down_pos
                                    self.coordY+=d
                                    for g in range(10):
                                     if self.pers[g]:
                                        for j in range(1,9,2):
                                            self.pers[g].coord[j]+=d
                                            self.pers[g].coord1[j]+=d
                                    self.platform=i
                else:
                        pass
        else:
                pass

    
    def reverce(self):
        self.face=not self.face
        self.buildBody(self.pers[0].coord[0],self.pers[0].coord[1])
    def toStatic(self):
     if(self.pers[1] and self.pers[6] and self.pers[8]):
        if(self.i==0):
            if(self.face):
                self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(self.ud))*self.pers[6].width
                self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(self.ud))*self.pers[6].width
                self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(-90+self.ud))*self.pers[6].height
                self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(-90+self.ud))*self.pers[6].height
                self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(-180+self.ud))*self.pers[6].width
                self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(-180+self.ud))*self.pers[6].width
                self.pers[6].set_fareaF(self.ud)

                self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(self.ud))*self.pers[8].width
                self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(self.ud))*self.pers[8].width
                self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(-90+self.ud))*self.pers[8].height
                self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(-90+self.ud))*self.pers[8].height
                self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(-180+self.ud))*self.pers[8].width
                self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(-180+self.ud))*self.pers[8].width
                self.pers[8].set_fareaF(self.ud)

                if self.pers[7]:
                        self.pers[7].coord[2]=self.pers[6].coord[6]+self.pers[7].width
                        self.pers[7].coord[3]=self.coordY
                        self.pers[7].coord[4]=self.pers[7].coord[2]+math.cos(math.radians(90-self.ud1))*self.pers[7].height
                        self.pers[7].coord[5]=self.pers[7].coord[3]+math.sin(math.radians(90-self.ud1))*self.pers[7].height
                        self.pers[7].coord[6]=self.pers[7].coord[4]+math.cos(math.radians(180-self.ud1))*self.pers[7].width
                        self.pers[7].coord[7]=self.pers[7].coord[5]+math.sin(math.radians(180-self.ud1))*self.pers[7].width
                        self.pers[7].coord[0]=self.pers[7].coord[6]+math.cos(math.radians(270-self.ud1))*self.pers[7].height
                        self.pers[7].coord[1]=self.pers[7].coord[7]+math.sin(math.radians(270-self.ud1))*self.pers[7].height
                        self.pers[7].set_fareaF(self.ud1)
                if self.pers[9]:
                        self.pers[9].coord[2]=self.pers[8].coord[6]+self.pers[9].width
                        self.pers[9].coord[3]=self.coordY
                        self.pers[9].coord[5]=self.pers[9].coord[3]+math.sin(math.radians(90-self.ud1))*self.pers[9].height
                        self.pers[9].coord[4]=self.pers[9].coord[2]+math.cos(math.radians(90-self.ud1))*self.pers[9].height
                        self.pers[9].coord[6]=self.pers[9].coord[4]+math.cos(math.radians(180-self.ud1))*self.pers[9].width
                        self.pers[9].coord[7]=self.pers[9].coord[5]+math.sin(math.radians(180-self.ud1))*self.pers[9].width
                        self.pers[9].coord[0]=self.pers[9].coord[6]+math.cos(math.radians(270-self.ud1))*self.pers[9].height
                        self.pers[9].coord[1]=self.pers[9].coord[7]+math.sin(math.radians(270-self.ud1))*self.pers[9].height
                        self.pers[9].set_fareaF(self.ud1)

            else:
                self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(180-self.ud))*self.pers[6].width
                self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(180-self.ud))*self.pers[6].width
                self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(-90-self.ud))*self.pers[6].height
                self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(-90-self.ud))*self.pers[6].height
                self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(-self.ud))*self.pers[6].width
                self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(-self.ud))*self.pers[6].width
                self.pers[6].set_farea(-self.ud)

                self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(180-self.ud))*self.pers[8].width
                self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(180-self.ud))*self.pers[8].width
                self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(-90-self.ud))*self.pers[8].height
                self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(-90-self.ud))*self.pers[8].height
                self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(-self.ud))*self.pers[8].width
                self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(-self.ud))*self.pers[8].width
                self.pers[8].set_farea(-self.ud)

                if self.pers[7]:
                        self.pers[7].coord[2]=self.pers[6].coord[6]-self.pers[7].width
                        self.pers[7].coord[3]=self.coordY
                        self.pers[7].coord[4]=self.pers[7].coord[2]+math.cos(math.radians(90+self.ud))*self.pers[7].height
                        self.pers[7].coord[5]=self.pers[7].coord[3]+math.sin(math.radians(90+self.ud))*self.pers[7].height
                        self.pers[7].coord[6]=self.pers[7].coord[4]+math.cos(math.radians(self.ud))*self.pers[7].width
                        self.pers[7].coord[7]=self.pers[7].coord[5]+math.sin(math.radians(self.ud))*self.pers[7].width
                        self.pers[7].coord[0]=self.pers[7].coord[6]+math.cos(math.radians(270+self.ud))*self.pers[7].height
                        self.pers[7].coord[1]=self.pers[7].coord[7]+math.sin(math.radians(270+self.ud))*self.pers[7].height
                        self.pers[7].set_farea(self.ud)
                if self.pers[9]:
                        self.pers[9].coord[2]=self.pers[8].coord[6]-self.pers[9].width
                        self.pers[9].coord[3]=self.coordY
                        self.pers[9].coord[5]=self.pers[9].coord[3]+math.sin(math.radians(90+self.ud))*self.pers[9].height
                        self.pers[9].coord[4]=self.pers[9].coord[2]+math.cos(math.radians(90+self.ud))*self.pers[9].height
                        self.pers[9].coord[6]=self.pers[9].coord[4]+math.cos(math.radians(self.ud))*self.pers[9].width
                        self.pers[9].coord[7]=self.pers[9].coord[5]+math.sin(math.radians(self.ud))*self.pers[9].width
                        self.pers[9].coord[0]=self.pers[9].coord[6]+math.cos(math.radians(270+self.ud))*self.pers[9].height
                        self.pers[9].coord[1]=self.pers[9].coord[7]+math.sin(math.radians(270+self.ud))*self.pers[9].height
                        self.pers[9].set_farea(self.ud)

        else:
            u=0
            if(self.i>0):
                if(self.face):
                    if(self.i<16):
                        self.i-=1
                        u=self.i*5
                    else:
                        self.i+=1
                        u=(30-self.i)*-5
                        if(self.i>29):
                            self.i=0
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u/2+self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u/2+self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u/2-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u/2-90+self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u/2-180+self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u/2-180+self.ud))*self.pers[6].width
                    self.pers[6].set_fareaF(u/2+self.ud)

                    if self.pers[7]:
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u+self.ud1))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-180+self.ud1))*self.pers[7].width
                            self.pers[7].set_fareaF(u+self.ud1)

                    u=-u

                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[8].width
                    self.pers[8].set_fareaF(u+self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[0]=self.pers[8].coord[2]-self.pers[9].width
                            self.pers[9].coord[1]=self.pers[8].coord[3]-self.pers[9].height
                            self.pers[9].calcF()
                            self.pers[9].set_fareaF(0)

                else:
                    if(self.i<16):
                        self.i-=1
                        u=self.i*-5
                    else:
                        self.i+=1
                        u=(30-self.i)*5
                        if(self.i>29):
                            self.i=0
                    self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[6].width
                    self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[6].height
                    self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[6].width
                    self.pers[6].set_farea(u/2+self.ud)

                    if self.pers[7]:
                            self.pers[7].coord[6]=self.pers[6].coord[0]
                            self.pers[7].coord[7]=self.pers[6].coord[1]
                            self.pers[7].coord[4]=self.pers[7].coord[6]+math.cos(math.radians(u-180-self.ud1))*self.pers[7].width
                            self.pers[7].coord[5]=self.pers[7].coord[7]+math.sin(math.radians(u-180-self.ud1))*self.pers[7].width
                            self.pers[7].coord[2]=self.pers[7].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[7].height
                            self.pers[7].coord[3]=self.pers[7].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[7].height
                            self.pers[7].coord[0]=self.pers[7].coord[2]+math.cos(math.radians(u-self.ud1))*self.pers[7].width
                            self.pers[7].coord[1]=self.pers[7].coord[3]+math.sin(math.radians(u-self.ud1))*self.pers[7].width
                            self.pers[7].set_farea(u-self.ud1)

                    u=-u

                    self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[8].width
                    self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[8].height
                    self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[8].width
                    self.pers[8].set_farea(u-self.ud)

                    if self.pers[9]:
                            self.pers[9].coord[0]=self.pers[8].coord[2]+self.pers[9].width
                            self.pers[9].coord[1]=self.pers[8].coord[3]-self.pers[9].height
                            self.pers[9].calc()
                            self.pers[9].set_farea(0)

            else:
                if(self.i<0):
                    if(self.face):
                        if(self.i<-14):
                            self.i-=1
                            u=(30+self.i)*5
                            if(self.i==-30):
                                self.i=0
                        else:
                            self.i+=1
                            u=self.i*5

                        self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2+self.ud))*self.pers[8].width
                        self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2+self.ud))*self.pers[8].width
                        self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90+self.ud))*self.pers[8].height
                        self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90+self.ud))*self.pers[8].height
                        self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-180+self.ud))*self.pers[8].width
                        self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-180+self.ud))*self.pers[8].width
                        self.pers[8].set_fareaF(u/2+self.ud)

                        if self.pers[9]:
                                self.pers[9].coord[6]=self.pers[8].coord[0]
                                self.pers[9].coord[7]=self.pers[8].coord[1]
                                self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u+self.ud1))*self.pers[9].width
                                self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u+self.ud1))*self.pers[9].width
                                self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[9].height
                                self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[9].height
                                self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-180+self.ud1))*self.pers[9].width
                                self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-180+self.ud1))*self.pers[9].width
                                self.pers[9].set_fareaF(u+self.ud1)

                        u=-u

                        self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[6].width
                        self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[6].width
                        self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[6].height
                        self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[6].height
                        self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[6].width
                        self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[6].width
                        self.pers[6].set_fareaF(u+self.ud)

                        if self.pers[7]:
                                self.pers[7].coord[0]=self.pers[6].coord[2]-self.pers[7].width
                                self.pers[7].coord[1]=self.pers[6].coord[3]-self.pers[7].height
                                self.pers[7].calcF()
                                self.pers[7].set_fareaF(0)

                    else:
                        if(self.i<-14):
                            self.i-=1
                            u=(30+self.i)*-5
                            if(self.i<-29):
                                self.i=0
                        else:
                            self.i+=1
                            u=self.i*-5
                        self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u/2-180-self.ud))*self.pers[8].width
                        self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u/2-180-self.ud))*self.pers[8].width
                        self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u/2-90-self.ud))*self.pers[8].height
                        self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u/2-90-self.ud))*self.pers[8].height
                        self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u/2-self.ud))*self.pers[8].width
                        self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u/2-self.ud))*self.pers[8].width
                        self.pers[8].set_farea(u/2-self.ud)

                        if self.pers[9]:
                                self.pers[9].coord[6]=self.pers[8].coord[0]
                                self.pers[9].coord[7]=self.pers[8].coord[1]
                                self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-180-self.ud1))*self.pers[9].width
                                self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-180-self.ud1))*self.pers[9].width
                                self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[9].height
                                self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[9].height
                                self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-self.ud1))*self.pers[9].width
                                self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-self.ud1))*self.pers[9].width
                                self.pers[9].set_farea(u-self.ud1)

                        u=-u

                        self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[6].width
                        self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[6].width
                        self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[6].height
                        self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[6].height
                        self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[6].width
                        self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[6].width
                        self.pers[6].set_farea(u-self.ud)

                        if self.pers[7]:
                                self.pers[7].coord[0]=self.pers[6].coord[2]+self.pers[7].width
                                self.pers[7].coord[1]=self.pers[6].coord[3]-self.pers[7].height
                                self.pers[7].calc()
                                self.pers[7].set_farea(0)
    
    def jump(self):
        if(not self.fly):
            self.vectY=self.height/15
            self.fly=True
            self.i=0
    
    def createDarkness(self):
        if self.face:
            distance=25
            looking_side=1
        else:
            distance=-1525
            looking_side=-1
        self.darkness=[]
        for peace in self.w['map'][0].pers:
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1],peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side#distance+(peace.width*(looking_side-1))/2
                        dark.coord[1]=peace.coord[1]
                        dark.width=1500
                        dark.height=peace.height
                        dark.coord[2]=dark.coord[0]+looking_side*dark.width
                        dark.coord[3]=dark.coord[1]
                        dark.coord[4]=dark.coord[2]
                        dark.coord[5]=dark.coord[3]+dark.height
                        dark.coord[6]=dark.coord[0]
                        dark.coord[7]=dark.coord[5]
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front 23.5 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]+1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side#distance+(peace.width*(looking_side-1))/2
                        dark.coord[1]=peace.coord[1]+25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[3]+25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]+1000
                        dark.coord[6]=peace.coord[6]+25*looking_side
                        dark.coord[7]=peace.coord[7]-25
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front 45 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]+1500,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[1]+25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[3]+25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]+1500
                        dark.coord[6]=peace.coord[6]+25*looking_side
                        dark.coord[7]=peace.coord[7]-25
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front 78.5 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[1]+25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[3]+25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]+2000
                        dark.coord[6]=peace.coord[6]+25*looking_side
                        dark.coord[7]=peace.coord[7]-25
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen up
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0],self.pers[0].coord[1]+1000,peace.coord[0],peace.coord[1],peace.coord[2],peace.coord[3]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]
                        dark.coord[1]=peace.coord[1]+25
                        dark.width=peace.width
                        dark.height=975
                        dark.coord[2]=peace.coord[2]
                        dark.coord[3]=dark.coord[1]
                        dark.coord[4]=dark.coord[2]
                        dark.coord[5]=dark.coord[3]+dark.height
                        dark.coord[6]=dark.coord[0]
                        dark.coord[7]=dark.coord[5]
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front -23.5 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]-500,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[7]-25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[5]-25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]-500
                        dark.coord[6]=peace.coord[6]+25*looking_side
                        dark.coord[7]=peace.coord[1]+25
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front -45 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]-1000,peace.coord[6],peace.coord[7],peace.coord[4],peace.coord[5]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[7]-25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[5]-25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]-1000
                        dark.coord[6]=peace.coord[6]+25*looking_side
                        dark.coord[7]=peace.coord[1]+25
                        dark.rotation=0
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen front -78.5 degree
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]-1500,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[7]-25
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=peace.coord[5]-25
                        dark.coord[4]=self.pers[0].coord[0]+1500*looking_side
                        dark.coord[5]=self.pers[0].coord[1]-1500
                        dark.coord[6]=peace.coord[6]-25*looking_side
                        dark.coord[7]=peace.coord[1]+25
                        dark.rotation=0
                        dark.rotation=0
                        self.darkness.append(dark)
                    #seen down
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1],self.pers[0].coord[0],self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[2],peace.coord[3]):
                        dark=element()
                        dark.look='images//darkness.png'
                        dark.coord[0]=peace.coord[0]+25*looking_side
                        dark.coord[1]=peace.coord[7]-25
                        dark.width=peace.width
                        dark.height=975
                        dark.coord[2]=peace.coord[2]-25*looking_side
                        dark.coord[3]=dark.coord[1]
                        dark.coord[4]=dark.coord[2]
                        dark.coord[5]=dark.coord[3]-1000
                        dark.coord[6]=dark.coord[0]
                        dark.coord[7]=dark.coord[5]
                        dark.rotation=0
                        self.darkness.append(dark)
                    
    def lookingOver(self):
        self.front_warriors=[]
        self.back_warriors=[]
        if self.face:
            looking_side=1
        else:
            looking_side=-1
        dy=self.total_height*1.5+10
        dy1=1000-self.pers[0].coord[1]
        for warrior in self.w['warriors']:
            for peace in warrior.pers: #no forget add cheking no blocking by walls
                if peace:
                 cont = True
                 for dark in self.darkness:
                        if point_in_rect(peace.coord[0],peace.coord[1],dark):
                            cont=False
                 if cont:
                    #seen front
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1],self.pers[0].coord[0]+3000*looking_side,self.pers[0].coord[1],peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front 23.5 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]+dy1/4,self.pers[0].coord[0]+3000*looking_side,self.pers[0].coord[1]+1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front 45 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]+dy1/2,self.pers[0].coord[0]+3000*looking_side,self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front 78.5 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]+dy*0.75,self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen up
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[1]+1000-dy,self.pers[0].coord[0],self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[2],peace.coord[3]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front -23.5 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]-dy/4,self.pers[0].coord[0]+3000*looking_side,self.pers[0].coord[1]-500,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front -45 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]-dy/2,self.pers[0].coord[0]+3000*looking_side,self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen front -78.5 degree
                    if line_overlaps(self.pers[0].coord[0]+1350*looking_side,self.pers[0].coord[1]-dy*0.75,self.pers[0].coord[0]+1500*looking_side,self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen down
                    if line_overlaps(self.pers[0].coord[0],self.pers[0].coord[7]-dy,self.pers[0].coord[0],self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[2],peace.coord[3]):
                        self.add_visible_warrior(warrior)
                        break#?
                    #seen back
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1],self.pers[0].coord[0]-1500*looking_side,self.pers[0].coord[1],peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back 22.5 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]+dy1/4,self.pers[0].coord[0]-1500*looking_side,self.pers[0].coord[1]+1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back 45 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]+dy1/2,self.pers[0].coord[0]-1500*looking_side,self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back 77.5 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]+dy1*0.75,self.pers[0].coord[0]-750*looking_side,self.pers[0].coord[1]+2000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back -22.5 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]-dy/4,self.pers[0].coord[0]-1500*looking_side,self.pers[0].coord[1]-500,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back -45 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]-dy/2,self.pers[0].coord[0]-1500*looking_side,self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                    #seen back -77.5 degree
                    if line_overlaps(self.pers[0].coord[0]-150*looking_side,self.pers[0].coord[1]-dy*0.75,self.pers[0].coord[0]-750*looking_side,self.pers[0].coord[1]-1000,peace.coord[0],peace.coord[1],peace.coord[6],peace.coord[7]):
                        self.add_back_warrior()
                        break#?
                   
        for icon in self.front_warriors:
            self.extra_icons.append(icon)
        for icon in self.back_warriors:
            self.extra_icons.append(icon)
    def add_visible_warrior(self,warrior):
     if self.face:
        if self.front_warriors==[]:
            self.front_warriors.append({'x':self.client_side1_x-self.icon_size,'y':0,'l':warrior.pers[0].look})
        else:
            self.front_warriors.append({'x':self.front_warriors[-1]['x']-self.icon_size/2,'y':0,'l':warrior.pers[0].look})
     else:
        if self.front_warriors==[]:
            self.front_warriors.append({'x':self.client_side_w*2,'y':0,'l':warrior.pers[0].look})
        else:
            self.front_warriors.append({'x':self.front_warriors[-1]['x']+self.icon_size/2,'y':0,'l':warrior.pers[0].look})
    def add_back_warrior(self):
     if self.face:
        if self.back_warriors==[]:
            self.back_warriors.append({'x':self.client_side_w*2,'y':0,'l':'images//somebody.png'})
        else:
            self.back_warriors.append({'x':self.back_warriors[-1]['x']+self.icon_size/2,'y':0,'l':'images//somebody.png'})
     else:
        if self.back_warriors==[]:
            self.back_warriors.append({'x':self.client_side1_x-self.icon_size,'y':0,'l':'images//somebody.png'})
        else:
            self.back_warriors.append({'x':self.back_warriors[-1]['x']+self.icon_size/2,'y':0,'l':'images//somebody.png'})
      
    def damaged(self):
        self.dmgd=self.DAMAGED_FRAME
    def bleeding(self,part):
        for child in part.child:
            if child[0]:
                if child[0].health<=0:
                    part.health-=1
                else:
                    self.damaged(child)
            else:
                part.health-=10
                #animation of bleeding
    def legcick_inertion(self):
        if(self.legkick):
            self.lk+=1
            u=0
            if(self.lk==37):
                self.lk=0
                self.legkick=False
            if(self.lk<19):
                u=5
            elif(self.lk>18):
                u=(36-self.lk)*5
            if(self.face):
                if self.pers[8] and self.pers[6]:
                        self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u+self.ud))*self.pers[8].width
                        self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u+self.ud))*self.pers[8].width
                        self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90+self.ud))*self.pers[8].height
                        self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90+self.ud))*self.pers[8].height
                        self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-180+self.ud))*self.pers[8].width
                        self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-180+self.ud))*self.pers[8].width
                        self.pers[8].set_fareaF(u+self.ud)

                        if self.pers[9]:
                                self.pers[9].coord[6]=self.pers[8].coord[0]
                                self.pers[9].coord[7]=self.pers[8].coord[1]
                                self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u+self.ud1))*self.pers[9].width
                                self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u+self.ud1))*self.pers[9].width
                                self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90+self.ud1))*self.pers[9].height
                                self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90+self.ud1))*self.pers[9].height
                                self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-180+self.ud1))*self.pers[9].width
                                self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-180+self.ud1))*self.pers[9].width
                                self.pers[9].set_fareaF(u+self.ud1)

                else:
                        if self.pers[8]:
                                pass
                        elif self.pers[6]:
                                pass
            else:
                if self.pers[8] and self.pers[6]:
                        u=-u
                        self.pers[8].coord[4]=self.pers[8].coord[6]+math.cos(math.radians(u-180-self.ud))*self.pers[8].width
                        self.pers[8].coord[5]=self.pers[8].coord[7]+math.sin(math.radians(u-180-self.ud))*self.pers[8].width
                        self.pers[8].coord[2]=self.pers[8].coord[4]+math.cos(math.radians(u-90-self.ud))*self.pers[8].height
                        self.pers[8].coord[3]=self.pers[8].coord[5]+math.sin(math.radians(u-90-self.ud))*self.pers[8].height
                        self.pers[8].coord[0]=self.pers[8].coord[2]+math.cos(math.radians(u-self.ud))*self.pers[8].width
                        self.pers[8].coord[1]=self.pers[8].coord[3]+math.sin(math.radians(u-self.ud))*self.pers[8].width
                        self.pers[8].set_fareaF(u-self.ud)

                        if self.pers[9]:
                                self.pers[9].coord[6]=self.pers[8].coord[0]
                                self.pers[9].coord[7]=self.pers[8].coord[1]
                                self.pers[9].coord[4]=self.pers[9].coord[6]+math.cos(math.radians(u-180-self.ud1))*self.pers[9].width
                                self.pers[9].coord[5]=self.pers[9].coord[7]+math.sin(math.radians(u-180-self.ud1))*self.pers[9].width
                                self.pers[9].coord[2]=self.pers[9].coord[4]+math.cos(math.radians(u-90-self.ud1))*self.pers[9].height
                                self.pers[9].coord[3]=self.pers[9].coord[5]+math.sin(math.radians(u-90-self.ud1))*self.pers[9].height
                                self.pers[9].coord[0]=self.pers[9].coord[2]+math.cos(math.radians(u-self.ud1))*self.pers[9].width
                                self.pers[9].coord[1]=self.pers[9].coord[3]+math.sin(math.radians(u-self.ud1))*self.pers[9].width
                                self.pers[9].set_fareaF(u+self.ud1)

                else:
                        if self.pers[6]:
                                pass
                        elif self.pers[8]:
                                pass
    def handcick_inertion(self, weapon=None):
        if(self.handkick):
            if self.pers[4]:
                self.hk+=1
                u=0
                if(self.hk==37):
                    self.hk=0
                    self.handkick=False
                elif(self.hk<19):
                    u=self.hk*5
                elif(self.hk>18):
                    u=(36-self.hk)*5
                if(self.face):
                    if(self.hk==0):
                     if(self.pers[4]):
                        self.pers[4].coord[4]=self.pers[1].coord[4]
                        self.pers[4].coord[5]=self.pers[1].coord[5]
                        self.pers[4].coord[6]=self.pers[4].coord[4]+math.cos(math.radians(-135))*self.pers[4].width
                        self.pers[4].coord[7]=self.pers[4].coord[5]+math.sin(math.radians(-135))*self.pers[4].width
                        self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(-45))*self.pers[4].height
                        self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(-45))*self.pers[4].height
                        self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(45))*self.pers[4].width
                        self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(45))*self.pers[4].width
                        self.pers[4].set_fareaF(135)

                        if(self.pers[5]):
                                self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                                self.pers[5].coord[0]=self.pers[4].coord[0]
                                self.pers[5].calcF()
                                self.pers[5].set_fareaF(0)
                                if weapon:
                                    weapon.coord[0]=self.pers[5].coord[0]
                                    weapon.coord[1]=self.pers[5].coord[1]
                                    weapon.calcF()
                    else:
                     if(self.pers[4]):
                        self.pers[4].coord[4]=self.pers[1].coord[4]
                        self.pers[4].coord[5]=self.pers[1].coord[5]
                        self.pers[4].coord[6]=self.pers[4].coord[4]+math.cos(math.radians(u-135))*self.pers[4].width
                        self.pers[4].coord[7]=self.pers[4].coord[5]+math.sin(math.radians(u-135))*self.pers[4].width
                        self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(u-45))*self.pers[4].height
                        self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(u-45))*self.pers[4].height
                        self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(u+45))*self.pers[4].width
                        self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(u+45))*self.pers[4].width
                        self.pers[4].set_fareaF(u+45)

                        if(self.pers[5]):
                                self.pers[5].coord[4]=self.pers[4].coord[2]
                                self.pers[5].coord[5]=self.pers[4].coord[3]
                                self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(u-135))*self.pers[5].width
                                self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(u-135))*self.pers[5].width
                                self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(u-45))*self.pers[5].height
                                self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(u-45))*self.pers[5].height
                                self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(u+45))*self.pers[5].width
                                self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(u+45))*self.pers[5].width
                                self.pers[5].set_fareaF(u+45)
                                if weapon:
                                    weapon.coord[0]=self.pers[5].coord[0]
                                    weapon.coord[1]=self.pers[5].coord[1]
                                    weapon.calcF()
                else:
                    if(self.hk==0):
                     if(self.pers[4]):
                        self.pers[4].coord[4]=self.pers[1].coord[4]
                        self.pers[4].coord[5]=self.pers[1].coord[5]
                        self.pers[4].coord[6]=self.pers[4].coord[4]+math.cos(math.radians(-45))*self.pers[4].width
                        self.pers[4].coord[7]=self.pers[4].coord[5]+math.sin(math.radians(-45))*self.pers[4].width
                        self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(-135))*self.pers[4].height
                        self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(-135))*self.pers[4].height
                        self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(135))*self.pers[4].width
                        self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(135))*self.pers[4].width
                        self.pers[4].set_farea(135)

                        if(self.pers[5]):
                                self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                                self.pers[5].coord[0]=self.pers[4].coord[0]
                                self.pers[5].calc()
                                self.pers[5].set_farea(0)
                                if weapon:
                                    weapon.coord[0]=self.pers[5].coord[0]
                                    weapon.coord[1]=self.pers[5].coord[1]
                                    weapon.calc()
                    else:
                     if(self.pers[4]):
                        u=-u
                        self.pers[4].coord[4]=self.pers[1].coord[4]
                        self.pers[4].coord[5]=self.pers[1].coord[5]
                        self.pers[4].coord[6]=self.pers[4].coord[4]+math.cos(math.radians(-45+u))*self.pers[4].width
                        self.pers[4].coord[7]=self.pers[4].coord[5]+math.sin(math.radians(-45+u))*self.pers[4].width
                        self.pers[4].coord[0]=self.pers[4].coord[6]+math.cos(math.radians(-135+u))*self.pers[4].height
                        self.pers[4].coord[1]=self.pers[4].coord[7]+math.sin(math.radians(-135+u))*self.pers[4].height
                        self.pers[4].coord[2]=self.pers[4].coord[0]+math.cos(math.radians(135+u))*self.pers[4].width
                        self.pers[4].coord[3]=self.pers[4].coord[1]+math.sin(math.radians(135+u))*self.pers[4].width
                        self.pers[4].set_farea(135+u)

                        if(self.pers[5]):
                                self.pers[5].coord[4]=self.pers[4].coord[2]
                                self.pers[5].coord[5]=self.pers[4].coord[3]
                                self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(u-45))*self.pers[5].width
                                self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(u-45))*self.pers[5].width
                                self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(u-135))*self.pers[5].height
                                self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(u-135))*self.pers[5].height
                                self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(u+135))*self.pers[5].width
                                self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(u+135))*self.pers[5].width
                                self.pers[5].set_farea(u+135)
                                if weapon:
                                    weapon.coord[0]=self.pers[5].coord[0]
                                    weapon.coord[1]=self.pers[5].coord[1]
                                    weapon.calc()
            elif self.pers[2]:
                self.hk+=1
                u=0
                if(self.hk==37):
                    self.hk=0
                    self.handkick=False
                elif(self.hk<19):
                    u=self.hk*5
                elif(self.hk>18):
                    u=(36-self.hk)*5
                if(self.face):
                    if(self.hk==0):
                     if self.pers[2]:
                             self.pers[2].coord[6]=self.pers[1].coord[6]
                             self.pers[2].coord[7]=self.pers[1].coord[7]
                             self.pers[2].coord[0]=(self.pers[2].coord[6]+math.cos(math.radians(225))*self.pers[2].height)
                             self.pers[2].coord[1]=(self.pers[2].coord[7]+math.sin(math.radians(225))*self.pers[2].height)
                             self.pers[2].coord[2]=(self.pers[2].coord[0]+math.cos(math.radians(315))*self.pers[2].width)
                             self.pers[2].coord[3]=(self.pers[2].coord[1]+math.sin(math.radians(315))*self.pers[2].width)
                             self.pers[2].coord[4]=(self.pers[2].coord[2]+math.cos(math.radians(45))*self.pers[2].height)
                             self.pers[2].coord[5]=(self.pers[2].coord[3]+math.sin(math.radians(45))*self.pers[2].height)
                             self.pers[2].set_fareaF(135)

                             if self.pers[3]:
                                     self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                                     self.pers[3].coord[0]=self.pers[2].coord[0]
                                     self.pers[3].calcF()
                                     self.pers[3].set_fareaF(0)
                    else:
                     if(self.pers[2]):
                        self.pers[2].coord[4]=self.pers[1].coord[6]
                        self.pers[2].coord[5]=self.pers[1].coord[7]
                        self.pers[2].coord[6]=self.pers[2].coord[4]+math.cos(math.radians(u-135))*self.pers[2].width
                        self.pers[2].coord[7]=self.pers[2].coord[5]+math.sin(math.radians(u-135))*self.pers[2].width
                        self.pers[2].coord[0]=self.pers[2].coord[6]+math.cos(math.radians(u-45))*self.pers[2].height
                        self.pers[2].coord[1]=self.pers[2].coord[7]+math.sin(math.radians(u-45))*self.pers[2].height
                        self.pers[2].coord[2]=self.pers[2].coord[0]+math.cos(math.radians(u+45))*self.pers[2].width
                        self.pers[2].coord[3]=self.pers[2].coord[1]+math.sin(math.radians(u+45))*self.pers[2].width
                        self.pers[2].set_fareaF(u+45)

                        if(self.pers[3]):
                                self.pers[3].coord[4]=self.pers[2].coord[2]
                                self.pers[3].coord[5]=self.pers[2].coord[3]
                                self.pers[3].coord[6]=self.pers[3].coord[4]+math.cos(math.radians(u-135))*self.pers[3].width
                                self.pers[3].coord[7]=self.pers[3].coord[5]+math.sin(math.radians(u-135))*self.pers[3].width
                                self.pers[3].coord[0]=self.pers[3].coord[6]+math.cos(math.radians(u-45))*self.pers[3].height
                                self.pers[3].coord[1]=self.pers[3].coord[7]+math.sin(math.radians(u-45))*self.pers[3].height
                                self.pers[3].coord[2]=self.pers[3].coord[0]+math.cos(math.radians(u+45))*self.pers[3].width
                                self.pers[3].coord[3]=self.pers[3].coord[1]+math.sin(math.radians(u+45))*self.pers[3].width
                                self.pers[3].set_fareaF(u+45)
                else:
                    if(self.hk==0):
                     if(self.pers[2]):
                        self.pers[2].coord[4]=self.pers[1].coord[6]
                        self.pers[2].coord[5]=self.pers[1].coord[7]
                        self.pers[2].coord[6]=(self.pers[2].coord[4]+math.cos(math.radians(225))*self.pers[2].width)
                        self.pers[2].coord[7]=(self.pers[2].coord[5]+math.sin(math.radians(225))*self.pers[2].width)
                        self.pers[2].coord[0]=(self.pers[2].coord[6]+math.cos(math.radians(315))*self.pers[2].height)
                        self.pers[2].coord[1]=(self.pers[2].coord[7]+math.sin(math.radians(315))*self.pers[2].height)
                        self.pers[2].coord[2]=(self.pers[2].coord[0]+math.cos(math.radians(45))*self.pers[2].width)
                        self.pers[2].coord[3]=(self.pers[2].coord[1]+math.sin(math.radians(45))*self.pers[2].width)
                        self.pers[2].set_farea(135)

                        if self.pers[3]:
                                self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                                self.pers[3].coord[0]=self.pers[2].coord[2]
                                self.pers[3].calc()
                                self.pers[3].set_farea(0)

                    else:
                     if(self.pers[2]):
                        u=-u
                        self.pers[2].coord[4]=self.pers[1].coord[6]
                        self.pers[2].coord[5]=self.pers[1].coord[7]
                        self.pers[2].coord[6]=self.pers[2].coord[4]+math.cos(math.radians(-45+u))*self.pers[2].width
                        self.pers[2].coord[7]=self.pers[2].coord[5]+math.sin(math.radians(-45+u))*self.pers[2].width
                        self.pers[2].coord[0]=self.pers[2].coord[6]+math.cos(math.radians(-135+u))*self.pers[2].height
                        self.pers[2].coord[1]=self.pers[2].coord[7]+math.sin(math.radians(-135+u))*self.pers[2].height
                        self.pers[2].coord[2]=self.pers[2].coord[0]+math.cos(math.radians(135+u))*self.pers[2].width
                        self.pers[2].coord[3]=self.pers[2].coord[1]+math.sin(math.radians(135+u))*self.pers[2].width
                        self.pers[2].set_farea(135+u)

                        if(self.pers[3]):
                                self.pers[3].coord[4]=self.pers[2].coord[2]
                                self.pers[3].coord[5]=self.pers[2].coord[3]
                                self.pers[3].coord[6]=self.pers[3].coord[4]+math.cos(math.radians(u-45))*self.pers[3].width
                                self.pers[3].coord[7]=self.pers[3].coord[5]+math.sin(math.radians(u-45))*self.pers[3].width
                                self.pers[3].coord[0]=self.pers[3].coord[6]+math.cos(math.radians(u-135))*self.pers[3].height
                                self.pers[3].coord[1]=self.pers[3].coord[7]+math.sin(math.radians(u-135))*self.pers[3].height
                                self.pers[3].coord[2]=self.pers[3].coord[0]+math.cos(math.radians(u+135))*self.pers[3].width
                                self.pers[3].coord[3]=self.pers[3].coord[1]+math.sin(math.radians(u+135))*self.pers[3].width
                                self.pers[3].set_farea(u+135)
    def fly_inertion(self,weapon=None):
        m=self.w["map"][0]
        if(self.fly):
                #check platform in upsteare
                for i in range(len(m.pers)):
                    if ((self.pers[0].coord[6]<m.pers[i].coord[2] and self.pers[0].coord[6]>m.pers[i].coord[0] and self.pers[0].coord[7]<m.pers[i].coord[1] and self.pers[0].coord[7]+self.vectY>m.pers[i].coord[1])or
					(self.pers[0].coord[4]<m.pers[i].coord[2] and self.pers[0].coord[4]>m.pers[i].coord[0] and self.pers[0].coord[7]<m.pers[i].coord[1] and self.pers[0].coord[7]+self.vectY>m.pers[i].coord[1])or
					(self.pers[0].coord[4]>m.pers[i].coord[2] and self.pers[0].coord[6]<m.pers[i].coord[0] and self.pers[0].coord[7]<m.pers[i].coord[1] and self.pers[0].coord[7]+self.vectY>m.pers[i].coord[1])):
                        self.vectY=0
                        d=m.pers[i].coord[1]-self.pers[0].coord[7]
                        for j in range(10):
                         if self.pers[j]:
                            for g in range(1,8,2):
                                self.pers[j].coord[g]+=d
                                self.pers[j].coord1[g]+=d
                        if weapon:
                            for g in range(1,8,2):
                                weapon.coord[g]+=d
                                weapon.coord1[g]+=d
                            self.coordY+=d
                            break
                for i in range(10):
                 if self.pers[i]:
                        for g in range(1,8,2):
                            self.pers[i].coord[g]+=self.vectY
                            self.pers[i].coord1[g]+=self.vectY
                if weapon:
                            for g in range(1,8,2):
                                weapon.coord[g]+=self.vectY
                                weapon.coord1[g]+=self.vectY
                self.coordY+=self.vectY
                self.vectY-=self.a

                #check falling to ground
                if self.pers[7] and self.pers[9] and self.pers[1]:
                   down_pos=self.pers[1].coord[1]-self.pers[7].height-self.pers[6].height+self.pers[0].height/10*self.s#????
                   for j in range(len(m.pers)):
                        if((self.pers[7].coord[1]<=m.pers[j].coord[7] 
                          and self.pers[7].coord[0]>m.pers[j].coord[0] 
                          and self.pers[7].coord[0]<m.pers[j].coord[2] 
                          and self.pers[7].coord[1]-self.vectY-self.a>=m.pers[j].coord[7])
                          or (self.pers[9].coord[1]<=m.pers[j].coord[7] 
                          and self.pers[9].coord[0]>m.pers[j].coord[0] 
                          and self.pers[9].coord[0]<m.pers[j].coord[2] 
                          and self.pers[9].coord[1]-self.vectY-self.a>=m.pers[j].coord[7])):
                            self.vectY=0
                            self.fly=False
                            if(self.pers[7].coord[3]<m.pers[j].coord[7]):#
                                #d=m.pers[j].coord[7]-self.pers[7].coord[1]
                                d=m.pers[j].coord[7]-down_pos
                                for i in range(10):
                                 if self.pers[i]:
                                    for g in range(1,8,2):
                                        self.pers[i].coord[g]+=d
                                        self.pers[i].coord1[g]+=d
                                if weapon:
                                    for g in range(1,8,2):
                                        weapon.coord[g]+=d
                                        weapon.coord1[g]+=d
                                self.coordY+=d
                            elif(self.pers[9].coord[3]<m.pers[j].coord[7]):
                                #d=m.pers[j].coord[7]-self.pers[9].coord[1]
                                d=m.pers[j].coord[7]-down_pos
                                for i in range(10):
                                 if self.pers[i]:
                                    for g in range(1,8,2):
                                        self.pers[i].coord[g]+=d
                                        self.pers[i].coord1[g]+=d#self.vectY
                                if weapon:
                                    for g in range(1,8,2):
                                        weapon.coord[g]+=d
                                        weapon.coord1[g]+=d
                                self.coordY+=d
                            self.platform=j
                            break
                else:
                        pass#!!
        else:
                if(self.pers[1]):
                        if((self.pers[1].coord[2]<m.pers[self.platform].coord[0] and 
                        self.pers[1].coord[0]<m.pers[self.platform].coord[0])or
                        (self.pers[1].coord[2]>m.pers[self.platform].coord[2] and 
                        self.pers[1].coord[0]>m.pers[self.platform].coord[2])):
                                self.fly=True
                                self.vectY-=self.a
    def animation(self):
        if self.dmgd!=0:
            #animation
            self.dmgd-=1
    def checkAlive(self):#imbpus check his file
        if self.pers[0].health<=0 or self.isAlive==False:
                self.isAlive=False
                self.canClick=2
                self.messages[0]['a']=True
                self.messages[1]['a']=True
                self.messages[2]['a']=True
                self.messages[0]['l']='images//youdead.png'
                self.screenpos=[self.pers[0].coord[4],self.pers[0].coord[7]]

    def init_icons(self):
        #self.side_w=(self.client_width-self.game_area_width)/3
        #self.side1_x=self.game_area_width+self.side_w*2
        #self.icon_size=self.side_w
        #self.icon_x=self.side1_x
        
        self.client_game_area_width=(self.client_height*1.5)
        self.client_side_w=(self.client_width-self.client_game_area_width)/3
        self.client_side1_x=self.client_game_area_width+self.client_side_w*2
        self.icon_size=self.client_side_w
        self.icon_x=self.client_side1_x

        self.rdW=self.client_game_area_width-2*self.icon_size
        self.rdH=self.rdW/3
        self.rdX=(self.client_game_area_width-self.rdW)/2+self.client_side_w*2
        self.rdY=self.client_height/2-self.icon_size
        self.dokH=self.rdH/4
        self.dokW=self.rdW/3
        self.dokX=self.rdX+2*self.dokW
        self.dokY=self.rdY+self.rdH-self.dokH-self.icon_size/10
        self.messages=[{'a':False,'x':self.rdX,'y':self.rdY,'w':self.rdW,'h':self.rdH,'l':''},
                       {'a':False,'x':self.dokX,'y':self.dokY,'w':self.dokW,'h':self.dokH,'l':'images//exit.png'},
                       {'a':False,'x':self.dokX,'y':self.dokY-self.dokH,'w':self.dokW,'h':self.dokH,'l':'images//watch.png'}
                       ]
    def returnCameraX(self):
        if self.canClick!=3:
            if(self.face):
                #return -(self.pers[0].coord[4]-(self.width/6)-self.pers[0].width*2.5+self.width/2)
                #self.dx=-(self.pers[0].coord[4]+((self.width/6)-self.pers[0].width/3-self.width/2))
                self.dx=self.pers[0].coord[0]-150#self.dx
            else:
                #return -(self.pers[0].coord[4]-self.width/2+self.width/12+self.pers[0].width*2.5)
                #self.dx=-(self.pers[0].coord[4]-self.width/2-self.width/12-self.pers[0].width*2.5)
                self.dx=self.pers[0].coord[2]+150-1500+self.pers[0].width#self.dx
        else:
            self.dx=self.screenpos[0]
        return self.dx
            #if(self.face):
                #self.dx=-(self.screenpos[0]+((self.width/6)-self.pers[0].width/3-self.width/2))
                #return self.dx
                #return self.screenpos[0]
            #else:
                #self.dx=-(self.screenpos[0]-self.width/2-self.width/12-self.pers[0].width*2.5)
                #return self.dx
    def returnCameraY(self):
        if self.canClick!=3:
        #return -(self.pers[0].coord[7]+self.height/10+self.pers[0].height+self.pers[1].height+self.pers[6].height+self.pers[7].height-self.height/2)
            #self.dy=-self.pers[0].coord[7]+self.height/2+self.pers[0].height
            self.dy= self.pers[0].coord[7]-self.total_height*1.5-10#self.dy
        else:
            self.dy=-self.screenpos[1]+self.height/2+self.pers[0].height
        return self.dy
    def transform_coords(self, x,y):
        scale=self.client_height/1000
        x=(x-self.client_side_w*2)/scale+self.returnCameraX()
        y=y/scale+self.returnCameraY()
        return [x,y]
    
    def upedLeft(self, touch):
            pass
    def clickLeft(self,touch):
        x=touch['x']
        y=touch['y']
        if self.canClick==1:
            ret=False
            if( x<self.client_side_w*0.75 and y<self.client_side_w*2):
                self.goLeft()
                self.was_go=True
                ret=True
            elif(x>self.client_side_w*1.25 and x<self.client_side_w*2 and y<self.client_side_w*2):
                self.goRight()
                self.was_go=True
                ret=True
            if(x<self.client_side_w*2 and y<self.client_side_w*0.75):
                self.sit()
                self.was_sit=True
                ret=True
            if(x>self.client_side_w*4/3 and x<self.client_side_w*2 and y>self.client_side_w*1.25 and y<self.client_side_w*2):
                ret=True
                self.jump()
                self.vectX=640
            elif(x<self.client_side_w*2/3 and y>self.client_side_w*1.25 and y<self.client_side_w*2):
                ret=True
                self.jump()
                self.vectX=640
            elif(x<self.client_side_w*2 and y>self.client_side_w*1.25 and y<self.client_side_w*2 and
            		not(self.last_coord_x<self.client_side_w*2 and self.last_coord_y>self.client_side_w*1.25 and self.last_coord_y<self.client_side_w*2)):
                ret=True
                self.jump()
            self.last_coord_x=x
            self.last_coord_y=y
            return ret
        return False
    def clickLeft1(self, touch):
        x=touch['x']
        y=touch['y']
        #print('x',self.side_w,self.side_w*2,'y',self.side_w,self.side_w*3)
        #print(self.canClick)
        #print(self)
        if self.canClick==1:
                if(x>self.client_side_w and x<self.client_side_w*2 and y>self.client_side_w*2 and y<(self.client_side_w*3)):
                        self.reverce()
                #if(x>d/2 and x<self.width/6-d/2 and y>self.width/6/3*2 and y<self.width/6+d/2 ):
                #        self.jump()
    def clickCenter1(self,touch):
        x=touch['x']
        y=touch['y']
        if self.canClick==2:
                if(x>self.messages[1]['x'] and x<self.messages[1]['x']+self.messages[1]['w'] and y<self.client_height-self.messages[1]['y'] and y>self.client_height-self.messages[1]['y']-self.messages[1]['h']):
                    self.exitGame=True
                    print('exit')
                    #send message to server back to menu
                if(x>self.messages[2]['x'] and x<self.messages[2]['x']+self.messages[2]['w'] and y<self.client_height-self.messages[2]['y'] and y>self.client_height-self.messages[2]['y']-self.messages[2]['h']):
                    self.canClick=3
                    self.messages[0]['l']=False
                    self.messages[1]['l']=False
                    self.messages[2]['l']=False
                    self.screenpos=[self.pers[0].coord[4],self.pers[0].coord[7]]

    def clickCenter(self, touch):
        pass
    def upedCenter(self, touch):
            pass
    
    def clickRight(self, touch):
        pass
    
    def clickRight1(self,touch):
        x=touch['x']
        y=touch['y']
        if(self.canClick==3):
            if(x>self.icons[0]['x'] and x<self.icons[0]['x']+self.icon_size and y<self.client_height-self.icons[0]['y'] and y>self.client_height-self.icons[0]['y']-self.icon_size):
                self.exitGame=True
    
    def upedRight(self,touch):
            pass
    
    
    
    def bot(self):
        #if self.canClick!=0:
                #self.handKikc()

        self.inertion()
        self.animation()
        self.attack()

        #self.intoFly()

        for i in range(len(self.extra_functions)):
                self.extra_functions[i](self)
        if self.isAlive==False:
                self.endGame=True


    #public abstract void draw(SpriteBatch sb);
    #public abstract void drawLeft(SpriteBatch sb, Texture fone, Texture control, Texture reverce, float x, float y, float w, float h);
    #public abstract void drawRight(SpriteBatch sb, Texture fone, float x, float y, float w, float h);
    #public abstract boolean clickLeft(int x, int y,map m);
    #public abstract void clickLeft1(int x, int y,map m);//change map to word
    #public abstract void clickRight(int x,int y, map m);//word
    #public abstract void clickCenter(int x,int y, Word w);
    #public abstract void goLeft(map m);
    #public abstract void goRight(map m);
    #public abstract void reverce();
    #public abstract void jump();
    #public abstract void sit();
    #public abstract void stand();
    #public abstract void toStatic();
	#public abstract void inertion(map m);
	#public abstract void attack(Word w);
	#public abstract void animation();
	#public abstract float returnCameraX();
	#public abstract float returnCameraY();
	#public abstract void bot(SpriteBatch batch, Word w, map m)

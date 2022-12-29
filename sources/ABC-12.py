from AoD import *
from sources.Warrior import *
from sources.element import *
from sources.bullet import *
from sources.blood import *
from sources.peace import *

from sources.Map import *#


import math
from threading import Timer


def DestroyToDo(self,s=None):
        #overlaps
        pass
		#o i need make checking to face
def clr(self=None,s=None,w=None):
        if self==None:
                self=s

def reabilitation(self):
        if(self.isAlive):
                self.canClick=1
        print(self.extra_draws)
        self.extra_draws.remove(Rectangle(pos=(self.rdX,self.rdY),size=(self.rdW,self.rdH),source='images\\stun.png'))#clearit
        print(self.extra_draws)
def stuned(self):
        self.canClick=0
        #with self.canv:
        self.extra_draws.append(Rectangle(pos=(self.rdX,self.rdY),size=(self.rdW,self.rdH),source='images\\stun.png'))#maybe save
        self.r=reabilitation
        Timer(2, self.reabilitation).start()#formula for time
        print(self.extra_functions)
        #self.extra_functions.pop(stuned)
        #print(self.extra_functions)



class Warrior(warrior):
    def __init__(self, start,word,w,h):
        super().__init__(start,word,w,h)

        self.go=[]

        self.pers=[element(),#head	0
              element(),#body		1
              element(),#hand up	2
              element(),#hand down	3
              element(),#hand up1	4
              element(),#hand down1	5
              element(),#leg up         6
              element(),#leg down	7
              element(),#leg up1	8
              element()]#leg down1	9

        self.health=[element(),#head	0
              element(),#body		1
              element(),#hand up	2
              element(),#hand down	3
              element(),#hand up1	4
              element(),#hand down1	5
              element(),#leg up         6
              element(),#leg down	7
              element(),#leg up1	8
              element()]#leg down1	9

        #xx=2
        self.attacks=[#attack,power,type
            (10, 500,"melee"),#hand
            (20, 730,"melee"),#leg
            (15, 400,"saw",85),#saw
            (30, 1000,"stun",40),#hummer
            (4, 550,"stun",10)#gun
	    ]
        self.stan_possibility=0.95
        self.crit_possibility=0.1

        self.arm_animation=["images//minions//ABC-12//animation//change weapon 1.png","images//minions//ABC-12//animation//change weapon 2.png"]

        self.head="images//minions//ABC-12//head.png"
        self.body="images//minions//ABC-12//body.png"
        self.up="images//minions//ABC-12//up.png"
        self.foot="images//minions//ABC-12//foot.png"
        self.arm="images//minions//ABC-12//arm.png"

        self.head_h="images//minions//ABC-12//head_health.png"
        self.body_h="images//minions//ABC-12//body_health.png"
        self.up_h="images//minions//ABC-12//up_health.png"
        self.foot_h="images//minions//ABC-12//foot_health.png"
        self.arm_h="images//minions//ABC-12//arm_health.png"

        self.gun="images//minions//ABC-12//gun.png"
        self.saw="images//minions//ABC-12//saw.png"
        self.hummer="images//minions//ABC-12//hummer.png"

        self.bull="images//minions//ABC-12//bullet.png"

        self.bullets_n=10000
        self.can_shoot=True
        self.can_shoot1=True

        self.pers[0].height=self.height/10
        self.pers[0].width=self.pers[0].height
        #self.pers[0].height=100
        #self.pers[0].width=100
        self.pers[0].look=self.head
        self.pers[0].len[0]=self.pers[0].width/5
        self.pers[0].len[1]=self.pers[0].len[0]
        self.pers[0].len[2]=self.pers[0].len[0]
        self.pers[0].len[3]=self.pers[0].len[0]
        self.health[0].height=self.width/6/3.7
        self.health[0].width=self.health[0].height
        self.health[0].look=self.head_h
        self.pers[0].health=3000
        self.pers[0].max_health=self.pers[0].health
        self.pers[0].weight=20

        self.pers[1].width=self.pers[0].width*2
        self.pers[1].height=self.pers[0].width*2.4
        self.pers[1].look=self.body
        self.pers[1].len[0]=self.pers[1].width/5
        self.pers[1].len[1]=self.pers[1].len[0]
        self.pers[1].len[2]=self.pers[1].len[0]
        self.pers[1].len[3]=self.pers[1].len[0]
        self.health[1].width=self.health[0].width*2
        self.health[1].height=self.health[0].width*2.4
        self.health[1].look=self.body_h
        self.pers[1].health=5000
        self.pers[1].max_health=self.pers[1].health
        self.pers[1].weight=300

        self.pers[2].width=self.pers[0].height/3
        self.pers[2].height=self.pers[0].height
        self.pers[2].look=self.up
        self.pers[2].len[0]=self.pers[2].width/3
        self.pers[2].len[1]=self.pers[2].len[0]
        self.pers[2].len[2]=self.pers[2].len[0]
        self.pers[2].len[3]=self.pers[2].len[0]
        self.health[2].width=self.health[0].height/3
        self.health[2].height=self.health[0].height
        self.health[2].look=self.up_h
        self.pers[2].health=4000
        self.pers[2].max_health=self.pers[2].health
        self.pers[2].weight=45

        self.pers[3].width=self.pers[2].width/70*74
        self.pers[3].height=self.pers[2].height/180*188
        self.pers[3].look=self.arm
        self.pers[3].len[0]=self.pers[3].width/3
        self.pers[3].len[1]=self.pers[3].len[0]
        self.pers[3].len[2]=self.pers[3].len[0]
        self.pers[3].len[3]=self.pers[3].len[0]
        self.health[3].width=self.health[2].width/70*74
        self.health[3].height=self.health[2].height/180*188
        self.health[3].look=self.arm_h
        self.pers[3].health=4000
        self.pers[3].max_health=self.pers[3].health
        self.pers[3].weight=45

        self.pers[4].width=self.pers[2].width
        self.pers[4].height=self.pers[2].height
        self.pers[4].look=self.up
        self.pers[4].len[0]=self.pers[4].width/3
        self.pers[4].len[1]=self.pers[4].len[0]
        self.pers[4].len[2]=self.pers[4].len[0]
        self.pers[4].len[3]=self.pers[4].len[0]
        self.health[4].width=self.health[2].width
        self.health[4].height=self.health[2].height
        self.health[4].look=self.up_h
        self.pers[4].health=4000
        self.pers[4].max_health=self.pers[4].health
        self.pers[4].weight=45

        self.pers[5].width=self.pers[3].width
        self.pers[5].height=self.pers[3].height
        self.pers[5].look=self.arm
        self.pers[5].len[0]=self.pers[5].width/3
        self.pers[5].len[1]=self.pers[5].len[0]
        self.pers[5].len[2]=self.pers[5].len[0]
        self.pers[5].len[3]=self.pers[5].len[0]
        self.health[5].width=self.health[3].width
        self.health[5].height=self.health[3].height
        self.health[5].look=self.arm_h
        self.pers[5].health=4000
        self.pers[5].max_health=self.pers[5].health
        self.pers[5].weight=45

        self.pers[6].width=self.pers[2].width
        self.pers[6].height=self.pers[2].height
        self.pers[6].look=self.up
        self.pers[6].len[0]=self.pers[6].width/3
        self.pers[6].len[1]=self.pers[6].len[0]
        self.pers[6].len[2]=self.pers[6].len[0]
        self.pers[6].len[3]=self.pers[6].len[0]
        self.health[6].width=self.health[2].width
        self.health[6].height=self.health[2].height
        self.health[6].look=self.up_h
        self.pers[6].health=4000
        self.pers[6].max_health=self.pers[6].health
        self.pers[6].weight=55

        self.pers[7].width=self.pers[6].width/70*61
        self.pers[7].height=self.pers[6].height/180*157
        self.pers[7].look=self.foot
        self.pers[7].len[0]=self.pers[7].width/3
        self.pers[7].len[1]=self.pers[7].len[0]
        self.pers[7].len[2]=self.pers[7].len[0]
        self.pers[7].len[3]=self.pers[7].len[0]
        self.health[7].width=self.health[6].width/70*61
        self.health[7].height=self.health[6].height/180*157
        self.health[7].look=self.foot_h
        self.pers[7].health=4000
        self.pers[7].max_health=self.pers[7].health
        self.pers[7].weight=55

        self.pers[8].width=self.pers[6].width
        self.pers[8].height=self.pers[6].height
        self.pers[8].look=self.up
        self.pers[8].len[0]=self.pers[8].width/3
        self.pers[8].len[1]=self.pers[8].len[0]
        self.pers[8].len[2]=self.pers[8].len[0]
        self.pers[8].len[3]=self.pers[8].len[0]
        self.health[8].width=self.health[6].width
        self.health[8].height=self.health[6].height
        self.health[8].look=self.up_h
        self.pers[8].health=4000
        self.pers[8].max_health=self.pers[8].health
        self.pers[8].weight=55

        self.pers[9].width=self.pers[7].width
        self.pers[9].height=self.pers[7].height
        self.pers[9].look=self.foot
        self.pers[9].len[0]=self.pers[9].width/3
        self.pers[9].len[1]=self.pers[9].len[0]
        self.pers[9].len[2]=self.pers[9].len[0]
        self.pers[9].len[3]=self.pers[9].len[0]
        self.health[9].width=self.health[7].width
        self.health[9].height=self.health[7].height
        self.health[9].look=self.foot_h
        self.pers[9].health=4000
        self.pers[9].max_health=self.pers[9].health
        self.pers[9].weight=55

        self.total_weight=0
        for i in range(10):
            self.total_weight+=self.pers[i].weight

        self.total_height=self.pers[0].height+self.pers[1].height+self.pers[8].height+self.pers[9].height

        if(start[2]==1):
            self.face=True
        else:
            self.face=False
        self.buildBody(start[0],start[1]+self.pers[9].height+self.pers[8].height+self.pers[1].height)
        
        self.coordY=self.pers[1].coord[1]
        if self.pers[6] or self.pers[8]:
            if self.pers[6]:
                self.coordY-=self.pers[6].height
            else:
                self.coordY-=self.pers[8].height
            if self.pers[7] or self.pers[9]:
                if self.pers[7]:
                    self.coordY-=self.pers[7].height
                else:
                    self.coordY-=self.pers[9].height

        self.health[7].coord[0]=self.side_w-self.health[7].width##
        self.health[7].coord[1]=self.total_height#
        self.health[7].calcF()
        self.health[7].set_fareaF(0)

        self.health[9].coord[0]=self.health[7].coord[0]+self.health[9].width*2
        self.health[9].coord[1]=self.health[7].coord[1]
        self.health[9].calcF()
        self.health[9].set_fareaF(0)

        self.health[6].coord[0]=self.health[7].coord[6]
        self.health[6].coord[1]=self.health[7].coord[7]
        self.health[6].calcF()
        self.health[6].set_fareaF(0)

        self.health[8].coord[0]=self.health[9].coord[6]
        self.health[8].coord[1]=self.health[9].coord[7]
        self.health[8].calcF()
        self.health[8].set_fareaF(0)

        self.health[1].coord[0]=self.health[6].coord[6]-(self.health[1].width-self.health[7].width*3)/2
        self.health[1].coord[1]=self.health[6].coord[7]
        self.health[1].calcF()
        self.health[1].set_fareaF(0)

        self.health[0].coord[0]=self.health[1].coord[6]+(self.health[1].width-self.health[0].width)/2
        self.health[0].coord[1]=self.health[1].coord[7]
        self.health[0].calcF()
        self.health[0].set_fareaF(0)

        self.health[2].coord[6]=self.health[1].coord[6]
        self.health[2].coord[7]=self.health[1].coord[7]
        self.health[2].coord[0]=(self.health[2].coord[6]+math.cos(math.radians(225))*self.health[2].height)
        self.health[2].coord[1]=(self.health[2].coord[7]+math.sin(math.radians(225))*self.health[2].height)
        self.health[2].coord[2]=(self.health[2].coord[0]+math.cos(math.radians(315))*self.health[2].width)
        self.health[2].coord[3]=(self.health[2].coord[1]+math.sin(math.radians(315))*self.health[2].width)
        self.health[2].coord[4]=(self.health[2].coord[2]+math.cos(math.radians(45))*self.health[2].height)
        self.health[2].coord[5]=(self.health[2].coord[3]+math.sin(math.radians(45))*self.health[2].height)
        self.health[2].set_fareaF(135)

        self.health[3].coord[1]=self.health[2].coord[1]-self.health[3].height
        self.health[3].coord[0]=self.health[2].coord[0]
        self.health[3].calcF()
        self.health[3].set_fareaF(0)

        self.health[4].coord[4]=self.health[1].coord[4]
        self.health[4].coord[5]=self.health[1].coord[5]
        self.health[4].coord[6]=(self.health[4].coord[4]+math.cos(math.radians(225))*self.health[4].width)
        self.health[4].coord[7]=(self.health[4].coord[5]+math.sin(math.radians(225))*self.health[4].width)
        self.health[4].coord[0]=(self.health[4].coord[6]+math.cos(math.radians(315))*self.health[4].height)
        self.health[4].coord[1]=(self.health[4].coord[7]+math.sin(math.radians(315))*self.health[4].height)
        self.health[4].coord[2]=(self.health[4].coord[0]+math.cos(math.radians(45))*self.health[4].width)
        self.health[4].coord[3]=(self.health[4].coord[1]+math.sin(math.radians(45))*self.health[4].width)
        self.health[4].set_fareaF(45)

        self.health[5].coord[1]=self.health[4].coord[1]-self.health[5].height
        self.health[5].coord[0]=self.health[4].coord[0]
        self.health[5].calcF()
        self.health[5].set_fareaF(0)###

        for i in range(len(self.health)):
                for j in range(1,8,2):
                        self.health[i].coord[j]=self.height-self.health[i].coord[j]


        self.pers[0].parent=None
        self.pers[0].child=[[self.pers[1],[0,1,0,0]]]
        self.pers[1].parent=[self.pers[0],[6,7,0,0]]

        self.pers[1].child=[[self.pers[2],[4,5, 0,0]],[self.pers[4],[6,7,0,0]],[self.pers[6],[0,1,0,0]],[self.pers[8],[2,3,0,0]]]
        self.pers[2].parent=self.pers[1]
        self.pers[4].parent=self.pers[1]
        self.pers[6].parent=self.pers[1]
        self.pers[8].parent=self.pers[1]

        self.pers[2].child=[[self.pers[3],[0,1,0,0]]]
        self.pers[3].parent=[self.pers[2],[6,7,0,0]]

        self.pers[4].child=[[self.pers[5],[0,1,0,0]]]
        self.pers[5].parent=[self.pers[4],[6,7,0,0,]]

        self.pers[6].child=[self.pers[7],[0,1,0,0]]
        self.pers[7].parent=[self.pers[6],[6,7,0,0]]

        self.pers[8].child=[[self.pers[9]],[0,1,0,0]]
        self.pers[9].parent=[self.pers[8],[6,7,0,0]]

        self.go=self.pers[0].width/10

        self.fly=True
        #self.fly=False
        self.legkick=False
        self.handkick=False

        self.left_arm_animation=False
        self.write_arm_animation=False

        #self.coordY=self.pers[7].coord[3]
        self.ud=0
        self.ud1=0

        self.icons_pctr=["images//minions//ABC-12//icons//fist kikc.png",
			"images//minions//ABC-12//icons//foot kikc.png",
			"images//minions//ABC-12//icons//weapon gun.png",
			"images//minions//ABC-12//icons//weapon saw.png",
			"images//minions//ABC-12//icons//weapon hummer.png",
			"images//minions//ABC-12//icons//selfdestruction.png"]
        self.fr="images//minions//ABC-12//icons//frame.png"
        #self.icons = [[self.width-self.width/12+self.width/120,self.icon_size/5,self.icons_pctr[0]]]#x/y/icn
        #self.icons.append([self.icons[0][0],self.icons[0][1]+self.icon_size+self.icon_size/5,self.icons_pctr[1]])
        #self.icons.append([self.icons[0][0],self.icons[1][1]+self.icon_size+self.icon_size/5,self.icons_pctr[0]])
        #self.icons.append([self.icons[0][0],self.icons[2][1]+self.icon_size+self.icon_size/5,self.icons_pctr[0]])
        #self.icons.append([self.icons[0][0],self.icons[3][1]+self.icon_size+self.icon_size/5,self.icons_pctr[5]])

        #self.extra_icons=[[self.width-self.width/12-(self.icon_size/5+self.icon_size)*4,None,self.icons_pctr[2]],
        #                  [self.width-self.width/12-(self.icon_size/5+self.icon_size)*3,None,self.icons_pctr[3]],
        #                  [self.width-self.width/12-(self.icon_size/5+self.icon_size)*2,None,self.icons_pctr[4]],
        #                  [self.width-self.width/12-(self.icon_size/5+self.icon_size),None,self.icons_pctr[0]]]

        self.hand2img=self.icons_pctr[0]
        self.hand3img=self.icons_pctr[0]
        
        self.icons = [{'x':self.icon_x,'y':self.client_height-self.icon_size,'l':self.icons_pctr[0]}]#x/y/icn
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[0]['y']-self.icon_size,'l':self.icons_pctr[1]})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[1]['y']-self.icon_size,'l':self.icons_pctr[0]})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[2]['y']-self.icon_size,'l':self.icons_pctr[0]})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[3]['y']-self.icon_size,'l':self.icons_pctr[5]})

        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[1]['y']-self.icon_size,'l':self.fr})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[2]['y']-self.icon_size,'l':self.fr})

        self.extra_icons_position=-1000###
        self.extra_icons=[{'x':self.icons[0]['x']-(self.icon_size)*4,'y':-self.icon_size,'l':self.icons_pctr[2]},#
                          {'x':self.icons[0]['x']-(self.icon_size)*3,'y':-self.icon_size,'l':self.icons_pctr[3]},
                          {'x':self.icons[0]['x']-(self.icon_size)*2,'y':-self.icon_size,'l':self.icons_pctr[4]},
                          {'x':self.icons[0]['x']-(self.icon_size),'y':-self.icon_size,'l':self.icons_pctr[0]}]

        self.realyD="images//minions//ABC-12//icons//wannaSelfdestruction.png"
        self.rdW=self.game_area_width-2*self.icon_size
        self.rdH=self.rdW/3
        self.rdX=(self.game_area_width-self.rdW)/2+self.side_w*2
        self.rdY=self.height/2-self.icon_size
        self.realyDok="images//minions//ABC-12//icons//destroy.png"
        self.dokH=self.rdH/3
        self.dokW=self.rdW/3
        self.dokX=self.rdX+self.dokW
        self.dokY=self.rdY+self.icon_size/10
        self.destroyMessage=False

        self.messages.append({'a':self.destroyMessage,'x':self.rdX,'y':self.rdY,'w':self.rdW,'h':self.rdH,'l':self.realyD})
        self.messages.append({'a':self.destroyMessage,'x':self.dokX,'y':self.dokY,'w':self.dokW,'h':self.dokH,'l':self.realyDok})



        self.i=0
        self.s=0
        self.lk=0
        self.hk=0
        self.ud=0#
        self.ud1=0#
        self.platform=0

        self.wai=0
        self.lai=0
        self.laa_style=4
        self.waa_style=4

        self.c_s=0
        self.last_coord_x=0
        self.last_coord_y=0

        self.was_go=False
        self.was_sit=False

        self.isAlive=True
        self.canClick=1
        self.endGame=False
        self.exitGame=False

        self.extra_functions=[]
        self.extra_draws=[]

        self.centerTouch=[]
    def init_icons(self):
       super().init_icons()
       self.drawHealth()
       if(self.canClick==3):
        self.icons=[{'x':self.icon_x,'y':0,'l':''}]
       else:
        self.icons = [{'x':self.icon_x,'y':self.client_height-self.icon_size,'l':self.icons_pctr[0]}]#x/y/icn
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[0]['y']-self.icon_size,'l':self.icons_pctr[1]})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[1]['y']-self.icon_size,'l':self.hand2img})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[2]['y']-self.icon_size,'l':self.hand3img})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[3]['y']-self.icon_size,'l':self.icons_pctr[5]})

        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[1]['y']-self.icon_size,'l':self.fr})
        self.icons.append({'x':self.icons[0]['x'],'y':self.icons[2]['y']-self.icon_size,'l':self.fr})

        self.extra_icons=[{'x':self.icons[0]['x']-(self.icon_size)*4,'y':self.extra_icons_position,'l':self.icons_pctr[2]},#
                          {'x':self.icons[0]['x']-(self.icon_size)*3,'y':self.extra_icons_position,'l':self.icons_pctr[3]},
                          {'x':self.icons[0]['x']-(self.icon_size)*2,'y':self.extra_icons_position,'l':self.icons_pctr[4]},
                          {'x':self.icons[0]['x']-(self.icon_size),'y':self.extra_icons_position,'l':self.icons_pctr[0]}]

        self.messages.append({'a':self.destroyMessage,'x':self.rdX,'y':self.rdY,'w':self.rdW,'h':self.rdH,'l':self.realyD})
        self.messages.append({'a':self.destroyMessage,'x':self.dokX,'y':self.dokY,'w':self.dokW,'h':self.dokH,'l':self.realyDok})
        
    def drawHealth(self):
        self.health[0].width=self.client_side_w/2
        self.health[0].height=self.health[0].width
        
        self.health[1].width=self.health[0].width*2
        self.health[1].height=self.health[0].width*2.4
        
        self.health[2].width=self.health[0].height/3
        self.health[2].height=self.health[0].height
        
        self.health[3].width=self.health[2].width/70*74
        self.health[3].height=self.health[2].height/180*188
        
        self.health[4].width=self.health[2].width
        self.health[4].height=self.health[2].height
        
        self.health[5].width=self.health[3].width
        self.health[5].height=self.health[3].height
        
        self.health[6].width=self.health[2].width
        self.health[6].height=self.health[2].height
        
        self.health[7].width=self.health[6].width/70*61
        self.health[7].height=self.health[6].height/180*157
        
        self.health[8].width=self.health[6].width
        self.health[8].height=self.health[6].height
        
        self.health[9].width=self.health[7].width
        self.health[9].height=self.health[7].height
        
        
        self.health[7].coord[0]=self.client_side_w-self.health[7].width*2##
        self.health[7].coord[1]=self.client_side_w*4#self.total_height#
        self.health[7].calcF()
        self.health[7].set_fareaF(0)

        self.health[9].coord[0]=self.health[7].coord[0]+self.health[9].width*2
        self.health[9].coord[1]=self.health[7].coord[1]
        self.health[9].calcF()
        self.health[9].set_fareaF(0)

        self.health[6].coord[0]=self.health[7].coord[6]
        self.health[6].coord[1]=self.health[7].coord[7]
        self.health[6].calcF()
        self.health[6].set_fareaF(0)

        self.health[8].coord[0]=self.health[9].coord[6]
        self.health[8].coord[1]=self.health[9].coord[7]
        self.health[8].calcF()
        self.health[8].set_fareaF(0)

        self.health[1].coord[0]=self.health[6].coord[6]-(self.health[1].width-self.health[7].width*3)/2
        self.health[1].coord[1]=self.health[6].coord[7]
        self.health[1].calcF()
        self.health[1].set_fareaF(0)

        self.health[0].coord[0]=self.health[1].coord[6]+(self.health[1].width-self.health[0].width)/2
        self.health[0].coord[1]=self.health[1].coord[7]
        self.health[0].calcF()
        self.health[0].set_fareaF(0)

        self.health[2].coord[6]=self.health[1].coord[6]
        self.health[2].coord[7]=self.health[1].coord[7]
        self.health[2].coord[0]=(self.health[2].coord[6]+math.cos(math.radians(225))*self.health[2].height)
        self.health[2].coord[1]=(self.health[2].coord[7]+math.sin(math.radians(225))*self.health[2].height)
        self.health[2].coord[2]=(self.health[2].coord[0]+math.cos(math.radians(315))*self.health[2].width)
        self.health[2].coord[3]=(self.health[2].coord[1]+math.sin(math.radians(315))*self.health[2].width)
        self.health[2].coord[4]=(self.health[2].coord[2]+math.cos(math.radians(45))*self.health[2].height)
        self.health[2].coord[5]=(self.health[2].coord[3]+math.sin(math.radians(45))*self.health[2].height)
        self.health[2].set_fareaF(135)

        self.health[3].coord[1]=self.health[2].coord[1]-self.health[3].height
        self.health[3].coord[0]=self.health[2].coord[0]
        self.health[3].calcF()
        self.health[3].set_fareaF(0)

        self.health[4].coord[4]=self.health[1].coord[4]
        self.health[4].coord[5]=self.health[1].coord[5]
        self.health[4].coord[6]=(self.health[4].coord[4]+math.cos(math.radians(225))*self.health[4].width)
        self.health[4].coord[7]=(self.health[4].coord[5]+math.sin(math.radians(225))*self.health[4].width)
        self.health[4].coord[0]=(self.health[4].coord[6]+math.cos(math.radians(315))*self.health[4].height)
        self.health[4].coord[1]=(self.health[4].coord[7]+math.sin(math.radians(315))*self.health[4].height)
        self.health[4].coord[2]=(self.health[4].coord[0]+math.cos(math.radians(45))*self.health[4].width)
        self.health[4].coord[3]=(self.health[4].coord[1]+math.sin(math.radians(45))*self.health[4].width)
        self.health[4].set_fareaF(45)

        self.health[5].coord[1]=self.health[4].coord[1]-self.health[5].height
        self.health[5].coord[0]=self.health[4].coord[0]
        self.health[5].calcF()
        self.health[5].set_fareaF(0)

        for i in range(len(self.health)):
                for j in range(1,8,2):
                        self.health[i].coord[j]=self.height-self.health[i].coord[j]
    
    def goLeft(self):
        if(not self.fly and not self.legkick and self.pers[1] and self.pers[6] and self.pers[8]):
            r=True
            if(not self.face):
                for i in range(len(self.w["map"][0].pers)):
                    if(
			(self.pers[1].coord[3]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[3]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[4]<self.w["map"][0].pers[i].coord[2] and self.pers[1].coord[4]+self.go>=self.w["map"][0].pers[i].coord[2])or
			(self.pers[1].coord[5]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[5]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[4]<self.w["map"][0].pers[i].coord[2] and self.pers[1].coord[4]+self.go>=self.w["map"][0].pers[i].coord[2])or
			(self.pers[0].coord[3]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[3]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[4]<self.w["map"][0].pers[i].coord[2] and self.pers[0].coord[4]+self.go>=self.w["map"][0].pers[i].coord[2])or
			(self.pers[0].coord[5]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[5]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[4]<self.w["map"][0].pers[i].coord[2] and self.pers[0].coord[4]+self.go>=self.w["map"][0].pers[i].coord[2])
			):
                        r=False
                        break
            else:
                for i in range(len(self.w["map"][0].pers)):
                    if(
                        (self.pers[1].coord[1]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[1]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[0]<self.w["map"][0].pers[i].coord[2] and self.pers[1].coord[0]+self.go>=self.w["map"][0].pers[i].coord[2])or
                        (self.pers[1].coord[7]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[7]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[0]<self.w["map"][0].pers[i].coord[2] and self.pers[1].coord[0]+self.go>=self.w["map"][0].pers[i].coord[2])or
                        (self.pers[0].coord[1]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[1]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[0]<self.w["map"][0].pers[i].coord[2] and self.pers[0].coord[0]+self.go>=self.w["map"][0].pers[i].coord[2])or
                        (self.pers[0].coord[7]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[7]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[0]<self.w["map"][0].pers[i].coord[2] and self.pers[0].coord[0]+self.go>=self.w["map"][0].pers[i].coord[2])
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
                        for i in range(len(self.w["map"][0].pers)):
                            if(i!=self.platform):
                                if(self.pers[7].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[7].coord[0]<=self.w["map"][0].pers[i].coord[2] and self.pers[7].coord[1]+self.pers[7].height>=self.w["map"][0].pers[i].coord[7] and self.pers[7].coord[1]<=self.w["map"][0].pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=self.w["map"][0].pers[i].coord[7]-down_pos
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
                        for i in range(len(self.w["map"][0].pers)):
                            if(i!=self.platform):
                                if(self.pers[9].coord[2]>self.w["map"][0].pers[i].coord[0] and self.pers[9].coord[2]<=self.w["map"][0].pers[i].coord[2] and self.pers[9].coord[3]+self.pers[9].height>=self.w["map"][0].pers[i].coord[7] and self.pers[9].coord[3]<=self.w["map"][0].pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=self.w["map"][0].pers[i].coord[7]-down_pos
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
        if(not self.fly and not self.legkick and self.pers[1] and self.pers[6] and self.pers[8]):
            r=True
            #level=0#
            if(self.face):
                for i in range(len(self.w["map"][0].pers)):
                    if(
			(self.pers[1].coord[3]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[3]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[4]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[4]-self.go<=self.w["map"][0].pers[i].coord[0])or
			(self.pers[1].coord[5]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[5]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[4]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[4]-self.go<=self.w["map"][0].pers[i].coord[0])or
			(self.pers[0].coord[3]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[3]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[4]>self.w["map"][0].pers[i].coord[0] and self.pers[0].coord[4]-self.go<=self.w["map"][0].pers[i].coord[0])or
			(self.pers[0].coord[5]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[5]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[4]>self.w["map"][0].pers[i].coord[0] and self.pers[0].coord[4]-self.go<=self.w["map"][0].pers[i].coord[0])
			) or not(self.pers[9] or self.pers[7]):
                        r=False
                        break

            else:
                for i in range(len(self.w["map"][0].pers)):
                    if(
                        (self.pers[1].coord[1]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[1]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[0]-self.go<=self.w["map"][0].pers[i].coord[0])or
                        (self.pers[1].coord[7]>self.w["map"][0].pers[i].coord[1] and self.pers[1].coord[7]<self.w["map"][0].pers[i].coord[7] and self.pers[1].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[0]-self.go<=self.w["map"][0].pers[i].coord[0])or
                        (self.pers[0].coord[1]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[1]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[0].coord[0]-self.go<=self.w["map"][0].pers[i].coord[0])or
                        (self.pers[0].coord[7]>self.w["map"][0].pers[i].coord[0] and self.pers[1].coord[7]<self.w["map"][0].pers[i].coord[7] and self.pers[0].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[0].coord[0]-self.go<=self.w["map"][0].pers[i].coord[0])
                        ) or not(self.pers[9] or self.pers[7]):
                        r=False
                        print(self.face)
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
                        for i in range(len(self.w["map"][0].pers)):
                            if(i!=self.platform):
                                if(self.pers[7].coord[0]>self.w["map"][0].pers[i].coord[0] and self.pers[7].coord[0]<=self.w["map"][0].pers[i].coord[2] and self.pers[7].coord[1]+self.pers[7].height>=self.w["map"][0].pers[i].coord[7] and self.pers[7].coord[1]<=self.w["map"][0].pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=self.w["map"][0].pers[i].coord[7]-down_pos
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
                        for i in range(len(self.w["map"][0].pers)):
                            if(i!=self.platform):
                                if(self.pers[9].coord[2]>self.w["map"][0].pers[i].coord[0] and self.pers[9].coord[2]<=self.w["map"][0].pers[i].coord[2] and self.pers[9].coord[3]+self.pers[9].height>=self.w["map"][0].pers[i].coord[7] and self.pers[9].coord[3]<=self.w["map"][0].pers[i].coord[7]):
                                    #d=m.pers[i].coord[7]-m.pers[self.platform].coord[7]
                                    d=self.w["map"][0].pers[i].coord[7]-down_pos
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
    def jump(self):
        if(not self.fly):
            self.vectY=self.height/15
            self.fly=True
            self.i=0

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
    def sit(self):
         if(not self.fly):
             d=self.pers[0].height/10
             if(self.s<14):
                self.s+=1
                for i in range(6):
                 if self.pers[i]:
                    for g in range(1,8,2):
                        self.pers[i].coord[g]-=d
                        self.pers[i].coord1[g]-=d
                if self.pers[6]:
                        self.pers[6].coord[7]-=d
                        self.pers[6].coord[1]-=d
                if self.pers[8]:
                        self.pers[8].coord[7]-=d
                        self.pers[8].coord[1]-=d

                self.ud=5*self.s
                self.ud1=5*self.s
    def stand(self):
      if self.pers[1] and self.pers[6] and self.pers[8]:
        if(self.s!=0):
            self.s-=1
            d=self.pers[0].height/10
            for i in range(6):
                if self.pers[i]:
                    for g in range(1,8,2):
                        self.pers[i].coord[g]+=d
                        self.pers[i].coord1[g]+=d
            if self.pers[6]:
                    self.pers[6].coord[7]+=d
                    self.pers[6].coord[1]+=d
            if self.pers[8]:
                    self.pers[8].coord[7]+=d
                    self.pers[8].coord[1]+=d

            self.ud=5*self.s
            self.ud1=5*self.s
    def fall(self):
            pass
    def wake_up(self):
            pass

    def inertion(self):
        self.legcick_inertion()
        self.handcick_inertion()
        self.fly_inertion()
        
        if(self.vectX<0):
                    for i in range(10):
                     if self.pers[i]:
                        for g in range(0,8,2):
                            self.pers[i].coord[g]+=self.vectX
                            self.pers[i].coord1[g]+=self.vectX
                    self.vectX+=self.total_weight
                    for i in range(len(self.w["map"][0].pers)):
                        for o in [0,1,6,7,8,9]:#8 and 9 its self.fall()
                         if self.pers[o]:
                           if(self.pers[o].coord[0]>self.pers[o].coord[2]):
                            if((self.pers[o].line_overlaps(self.pers[o].coord[2],self.pers[o].coord[3],self.pers[o].coord[2]+self.vectX,self.pers[o].coord[3],self.w["map"][0].pers[i].coord[4],self.w["map"][0].pers[i].coord[5],self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[3])
                                and self.pers[o].coord[3]!=self.w["map"][0].pers[i].coord[5] ) or
                               self.pers[o].line_overlaps(self.pers[o].coord[4],self.pers[o].coord[5],self.pers[o].coord[4]+self.vectX,self.pers[o].coord[5],self.w["map"][0].pers[i].coord[4],self.w["map"][0].pers[i].coord[5],self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[3])
                               ):#make square 0,1 0+v,1 6,7 6+v,7
                                            print('>')
                                            print([self.pers[o].coord[3]])
                                            print([self.w["map"][0].pers[i].coord[5]])
                                            d=self.pers[o].coord[2]-self.w["map"][0].pers[i].coord[2]#
                                            print(self.pers[o].coord[2])
                                            print([self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[0]])
                                            for j in range(10):
                                                    for g in range(0,8,2):
                                                            self.pers[j].coord[g]-=d
                                                            self.pers[j].coord1[g]-=d
                                            print(self.pers[o].coord[2])
                           elif(self.pers[o].line_overlaps(self.pers[o].coord[0],self.pers[o].coord[1],self.pers[o].coord[0]+self.vectX,self.pers[o].coord[1],self.w["map"][0].pers[i].coord[4],self.w["map"][0].pers[i].coord[5],self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[3])or
                                self.pers[o].line_overlaps(self.pers[o].coord[6],self.pers[o].coord[7],self.pers[o].coord[6]+self.vectX,self.pers[o].coord[7],self.w["map"][0].pers[i].coord[4],self.w["map"][0].pers[i].coord[5],self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[7])
                                ):
                                            print('<')
                                            print(self.pers[o].coord[0])
                                            print([self.w["map"][0].pers[i].coord[2],self.w["map"][0].pers[i].coord[0]])
                                            d=self.pers[o].coord[0]-self.w["map"][0].pers[i].coord[2]
                                            for j in range(10):
                                                    for g in range(0,8,2):
                                                            self.pers[j].coord[g]-=d
                                                            self.pers[j].coord1[g]-=d
                                            print(self.pers[o].coord[0])
                                            self.vectX=0
                                            #break
                    if(self.vectX>0):
                        self.vectX=0

        elif(self.vectX>0):
                    for i in range(10):
                     if self.pers[i]:
                        for g in range(0,8,2):
                            self.pers[i].coord[g]+=self.vectX
                            self.pers[i].coord1[g]+=self.vectX
                    self.vectX-=self.total_weight#self.pers[0].width/5
                    for i in range(len(self.w["map"][0].pers)):
                     for o in [0,1,6,7,8,9]:#8 and 9 its self.fall()
                        if self.pers[o]:
                         if(self.pers[o].coord[0]>self.pers[o].coord[2]):
                            if(self.pers[o].line_overlaps(self.pers[o].coord[0],self.pers[o].coord[1],self.pers[o].coord[0]+self.vectX,self.pers[o].coord[1],self.w["map"][0].pers[i].coord[0],self.w["map"][0].pers[i].coord[1],self.w["map"][0].pers[i].coord[6],self.w["map"][0].pers[i].coord[7]) or
                               self.pers[o].line_overlaps(self.pers[o].coord[6],self.pers[o].coord[7],self.pers[o].coord[6]+self.vectX,self.pers[o].coord[7],self.w["map"][0].pers[i].coord[0],self.w["map"][0].pers[i].coord[1],self.w["map"][0].pers[i].coord[6],self.w["map"][0].pers[i].coord[7])
                               ):
                                   d=self.pers[o].coord[0]-self.w["map"][0].pers[i].coord[0]
                                   print('>')
                                   for j in range(10):
                                                   for g in range(0,8,2):
                                                           self.pers[j].coord[g]-=d
                                                           self.pers[j].coord1[g]-=d
                                   self.vectX=0
                                   #break
                         elif((self.pers[o].line_overlaps(self.pers[o].coord[2],self.pers[o].coord[3],self.pers[o].coord[2]+self.vectX,self.pers[o].coord[3],self.w["map"][0].pers[i].coord[0],self.w["map"][0].pers[i].coord[1],self.w["map"][0].pers[i].coord[6],self.w["map"][0].pers[i].coord[7])
                               and self.pers[o].coord[3]!=m.pers[i].coord[5] )or
                              self.pers[o].line_overlaps(self.pers[o].coord[4],self.pers[o].coord[5],self.pers[o].coord[4]+self.vectX,self.pers[o].coord[5],self.w["map"][0].pers[i].coord[0],self.w["map"][0].pers[i].coord[1],self.w["map"][0].pers[i].coord[6],self.w["map"][0].pers[i].coord[7])
                              ):
                                           d=self.pers[o].coord[2]-self.w["map"][0].pers[i].coord[0]
                                           print('<')
                                           print(o)
                                           print(i)
                                           for j in range(10):
                                                   for g in range(0,8,2):
                                                           self.pers[j].coord[g]-=d
                                                           self.pers[j].coord1[g]-=d
                                           self.vectX=0
                                           #break

                    if(self.vectX<0):
                        self.vectX=0
        #if self.pers[1].health<=0:
        self.bleeding(self.pers[0])
        self.checkAlive()

        #if not self.isAlive:

    def animation(self):
        super().animation()
        if(self.left_arm_animation and self.pers[3]):
            if(self.lai<11):
                self.lai+=1
                self.pers[3].look=self.arm_animation[self.lai%2]
                self.pers[3].width=self.pers[0].width*2
                self.pers[3].height=self.pers[3].width
                self.pers[3].coord[0]=self.pers[2].coord[0]-self.pers[3].width/2
                self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                self.pers[3].calcF()
                self.pers[3].set_fareaF(0)
            else:
                if(self.laa_style==1):
                    self.pers[3].width=self.pers[4].width/70*185
                    self.pers[3].height=self.pers[4].height/180*102
                    self.pers[3].look=self.gun
                    if(self.face):
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[0]
                        self.pers[3].calcF()
                        self.pers[3].set_fareaF(0)
                    else:
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[2]
                        self.pers[3].calc()
                        self.pers[3].set_farea(0)
                    self.lai=0
                    self.left_arm_animation=False
                elif(self.laa_style==2):
                    self.pers[3].width=self.pers[4].width/70*166
                    self.pers[3].height=self.pers[4].height/180*131
                    self.pers[3].look=self.saw
                    if(self.face):
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[0]
                        self.pers[3].calcF()
                        self.pers[3].set_fareaF(0)
                    else:
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[2]
                        self.pers[3].calc()
                        self.pers[3].set_farea(0)
                    self.lai=0
                    self.left_arm_animation=False
                elif(self.laa_style==3):
                    self.pers[3].width=self.pers[4].width/70*97
                    self.pers[3].height=-self.pers[4].height/180*159
                    self.pers[3].look=self.hummer
                    if(self.face):
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[0]
                        self.pers[3].calcF()
                        self.pers[3].set_fareaF(0)
                    else:
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[2]
                        self.pers[3].calc()
                        self.pers[3].set_farea(0)
                    self.lai=0
                    self.left_arm_animation=False
                elif(self.laa_style==4):
                    self.pers[3].width=self.pers[4].width/70*74
                    self.pers[3].height=self.pers[4].height/180*188
                    self.pers[3].look=self.arm
                    if(self.face):
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[0]
                        self.pers[3].calcF()
                        self.pers[3].set_fareaF(0)
                    else:
                        self.pers[3].coord[1]=self.pers[2].coord[1]-self.pers[3].height
                        self.pers[3].coord[0]=self.pers[2].coord[2]
                        self.pers[3].calc()
                        self.pers[3].set_farea(0)
                    self.lai=0
                    self.left_arm_animation=False
        if(self.write_arm_animation and self.pers[5]):
            if(self.wai<11):
                self.wai+=1
                self.pers[5].look=self.arm_animation[self.wai%2]
                self.pers[5].width=self.pers[0].width*2
                self.pers[5].height=self.pers[5].width
                self.pers[5].coord[0]=self.pers[4].coord[0]-self.pers[5].width/2
                self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                self.pers[5].calcF()
                self.pers[5].set_fareaF(0)
            else:
                if(self.waa_style==1):
                    self.pers[5].width=self.pers[4].width/70*185
                    self.pers[5].height=self.pers[4].height/180*102
                    self.pers[5].look=self.gun
                    if(self.face):
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[0]
                        self.pers[5].calcF()
                        self.pers[5].set_fareaF(0)
                    else:
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[2]
                        self.pers[5].calc()
                        self.pers[5].set_farea(0)
                    self.wai=0
                    self.write_arm_animation=False
                elif(self.waa_style==2):
                    self.pers[5].width=self.pers[4].width/70*166
                    self.pers[5].height=-self.pers[4].height/180*131
                    self.pers[5].look=self.saw
                    if(self.face):
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[0]
                        self.pers[5].calcF()
                        self.pers[5].set_fareaF(0)
                    else:
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[2]
                        self.pers[5].calc()
                        self.pers[5].set_farea(0)
                    self.wai=0
                    self.write_arm_animation=False
                elif(self.waa_style==3):
                    self.pers[5].width=self.pers[4].width/70*97
                    self.pers[5].height=-self.pers[4].height/180*159
                    self.pers[5].look=self.hummer
                    if(self.face):
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[0]
                        self.pers[5].calcF()
                        self.pers[5].set_fareaF(0)
                    else:
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[2]
                        self.pers[5].calc()
                        self.pers[5].set_farea(0)
                    self.wai=0
                    self.write_arm_animation=False
                elif(self.waa_style==4):
                    self.pers[5].width=self.pers[4].width/70*74
                    self.pers[5].height=self.pers[4].height/180*188
                    self.pers[5].look=self.arm
                    if(self.face):
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[0]
                        self.pers[5].calcF()
                        self.pers[5].set_fareaF(0)
                    else:
                        self.pers[5].coord[1]=self.pers[4].coord[1]-self.pers[5].height
                        self.pers[5].coord[0]=self.pers[4].coord[2]
                        self.pers[5].calc()
                        self.pers[5].set_farea(0)
                    self.wai=0
                    self.write_arm_animation=False
                print(self.pers[5].look)
                print(self.pers[5].coord)
    def attack(self):
        w=self.w
        #print(self.handkick)
        #print(self.waa_style)
        if(self.handkick):
                #print(self.waa_style)
                if self.waa_style==4:
                        atack=self.attacks[0]#todo array?
                elif self.waa_style==3:
                        atack=self.attacks[3]
                elif self.waa_style==2:
                        atack=self.attacks[2]
                elif self.waa_style==1:
                        atack=self.attacks[4]
                #print(self.waa_style)
                #print(atack)
                for i in range(len(self.w["warriors"])):
                        if(self.w["warriors"][i]!=self):
                                for g in range(len(self.w["warriors"][i].pers)):
                                 if w['warriors'][i].pers[g]:
                                    if hurting(self.pers[5],self.w["warriors"][i].pers[g],self.w["warriors"][i],atack) or hurting(self.pers[4],self.w["warriors"][i].pers[g],self.w["warriors"][i],atack):#OR?
                                                if(atack[2]=='stun'):
                                                        if(randint(0,101)<=atack[3]*self.w["warriors"][i].stan_possibility):
                                                                #self.w["warriors"][i].extra_functions.append(stuned)
                                                                stuned(self.w["warriors"][i])
                                                if(atack[2]=='saw'):
                                                        if(randint(0,101)<=atack[3]*self.w["warriors"][i].crit_possibility):
                                                                self.w["warriors"][i].crited(self.w["warriors"][i].pers[g],self.pers[5],atack)
                                                                if(not self.w["warriors"][i].pers[g]):
                                                                        break
                                #print(g)
                                #if(self.w["warriors"][i].pers[g].parent!=None):
                                 #   print('hmm')
                                  #  for j in range(len(self.w["warriors"][i].pers[g].parent.child)):
                                   #     if(self.w["warriors"][i].pers[g].parent.child[j]==self.w["warriors"][i].pers[g]):
                                    #        self.w["warriors"][i].pers[g].parent.child[j]=None
                                     #   self.w["warriors"][i].pers[g].parent=None
                                    #self.w["warriors"][i].pers[g].fly=True
                                    #self.w["warriors"][i].pers[g].health=0

        if(self.legkick):
         if self.pers[8]:
            for i in range(len(self.w["warriors"])):
                #print(i)
                if(self.w["warriors"][i]!=self):
                    #print('uuu')
                    for g in range(len(self.w["warriors"][i].pers)):
                     if w['warriors'][i].pers[g]:
                        #print('r')
                        hurting(self.pers[8],self.w["warriors"][i].pers[g],self.w["warriors"][i],self.attacks[1])
                                #if(self.w["warriors"][i].pers[g].parent!=None):
                                 #   for j in range(len(self.w["warriors"][i].pers[g].parent.child)):
                                  #      if(self.w["warriors"][i].pers[g].parent.child[j]==self.w["warriors"][i].pers[g]):
                                   #         self.w["warriors"][i].pers[g].parent.child[j]=None
                                    #    self.w["warriors"][i].pers[g].parent=None
                                    #self.w["warriors"][i].pers[g].fly=True
                                    #self.w["warriors"][i].pers[g].health=0
                        #print('lll')
            #print('t')
        #print(self.laa_style)
         elif self.pers[6]:
            for i in range(len(self.w["warriors"])):
                #print(i)
                if(self.w["warriors"][i]!=self):
                    #print('uuu')
                    for g in range(len(self.w["warriors"][i].pers)):
                     if w['warriors'][i].pers[g]:
                        #print('r')
                        hurting(self.pers[6],self.w["warriors"][i].pers[g],self.w["warriors"][i],self.attacks[1])


    def legKikc(self):
        if(not self.legkick):
            self.legkick=True
            if(self.face):
                if self.pers[6]:
                        self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(self.ud))*self.pers[6].width
                        self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(self.ud))*self.pers[6].width
                        self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(-90+self.ud))*self.pers[6].height
                        self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(-90+self.ud))*self.pers[6].height
                        self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(-180+self.ud))*self.pers[6].width
                        self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(-180+self.ud))*self.pers[6].width
                        self.pers[6].set_fareaF(self.ud)

                        if self.pers[7]:
                                self.pers[7].coord[2]=self.pers[6].coord[6]+self.pers[7].width
                                self.pers[7].coord[3]=self.coordY
                                self.pers[7].coord[4]=self.pers[7].coord[2]+math.cos(math.radians(90-self.ud1))*self.pers[7].height
                                self.pers[7].coord[5]=self.pers[7].coord[3]+math.sin(math.radians(90-self.ud1))*self.pers[7].height
                                self.pers[7].coord[6]=self.pers[7].coord[4]+math.cos(math.radians(180-self.ud1))*self.pers[7].width
                                self.pers[7].coord[7]=self.pers[7].coord[5]+math.sin(math.radians(180-self.ud1))*self.pers[7].width
                                self.pers[7].coord[0]=self.pers[7].coord[6]+math.cos(math.radians(270-self.ud1))*self.pers[7].height
                                self.pers[7].coord[1]=self.pers[7].coord[7]+math.sin(math.radians(270-self.ud1))*self.pers[7].height
                                self.pers[7].set_fareaF(-self.ud1)
            else:
                if self.pers[6]:
                        self.pers[6].coord[4]=self.pers[6].coord[6]+math.cos(math.radians(180-self.ud))*self.pers[6].width
                        self.pers[6].coord[5]=self.pers[6].coord[7]+math.sin(math.radians(180-self.ud))*self.pers[6].width
                        self.pers[6].coord[2]=self.pers[6].coord[4]+math.cos(math.radians(-90-self.ud))*self.pers[6].height
                        self.pers[6].coord[3]=self.pers[6].coord[5]+math.sin(math.radians(-90-self.ud))*self.pers[6].height
                        self.pers[6].coord[0]=self.pers[6].coord[2]+math.cos(math.radians(-self.ud))*self.pers[6].width
                        self.pers[6].coord[1]=self.pers[6].coord[3]+math.sin(math.radians(-self.ud))*self.pers[6].width
                        self.pers[6].set_farea(-self.ud)

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
    def handKikc(self):
        if(not self.handkick):
         self.handkick=True
         if self.pers[5]:
            if(self.waa_style==1):
                if(self.face):
                    self.pers[5].coord[6]=self.pers[4].coord[0]
                    self.pers[5].coord[7]=self.pers[4].coord[1]
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[4]=self.pers[5].coord[2]+math.cos(math.radians(135))*self.pers[5].height
                    self.pers[5].coord[5]=self.pers[5].coord[3]+math.sin(math.radians(135))*self.pers[5].height
                    self.pers[5].set_fareaF(45)
                else:
                    self.pers[5].coord[4]=self.pers[2].coord[2]
                    self.pers[5].coord[5]=self.pers[2].coord[3]
                    self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(-45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(-45))*self.pers[5].width
                    self.pers[5].set_farea(135)
            if(self.waa_style==2):
                if(self.face):
                    self.pers[5].coord[6]=self.pers[4].coord[0]
                    self.pers[5].coord[7]=self.pers[4].coord[1]
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[4]=self.pers[5].coord[2]+math.cos(math.radians(135))*self.pers[5].height
                    self.pers[5].coord[5]=self.pers[5].coord[3]+math.sin(math.radians(135))*self.pers[5].height
                    self.pers[5].set_fareaF(45)
                else:
                    self.pers[5].coord[4]=self.pers[2].coord[2]
                    self.pers[5].coord[5]=self.pers[2].coord[3]
                    self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(-45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(-45))*self.pers[5].width
                    self.pers[5].set_farea(135)
            if(self.waa_style==3):
                if(self.face):
                    self.pers[5].coord[6]=self.pers[4].coord[0]
                    self.pers[5].coord[7]=self.pers[4].coord[1]
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[4]=self.pers[5].coord[2]+math.cos(math.radians(135))*self.pers[5].height
                    self.pers[5].coord[5]=self.pers[5].coord[3]+math.sin(math.radians(135))*self.pers[5].height
                    self.pers[5].set_fareaF(45)
                else:
                    self.pers[5].coord[4]=self.pers[2].coord[2]
                    self.pers[5].coord[5]=self.pers[2].coord[3]
                    self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(-45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(-45))*self.pers[5].width
                    self.pers[5].set_farea(135)
            if(self.waa_style==4):
                if(self.face):
                    self.pers[5].coord[6]=self.pers[4].coord[0]
                    self.pers[5].coord[7]=self.pers[4].coord[1]
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-45))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(45))*self.pers[5].width
                    self.pers[5].coord[4]=self.pers[5].coord[2]+math.cos(math.radians(135))*self.pers[5].height
                    self.pers[5].coord[5]=self.pers[5].coord[3]+math.sin(math.radians(135))*self.pers[5].height
                    self.pers[5].set_fareaF(45)
                else:
                    self.pers[5].coord[4]=self.pers[2].coord[2]
                    self.pers[5].coord[5]=self.pers[2].coord[3]
                    self.pers[5].coord[6]=self.pers[5].coord[4]+math.cos(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[7]=self.pers[5].coord[5]+math.sin(math.radians(135))*self.pers[5].width
                    self.pers[5].coord[0]=self.pers[5].coord[6]+math.cos(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[1]=self.pers[5].coord[7]+math.sin(math.radians(-135))*self.pers[5].height
                    self.pers[5].coord[2]=self.pers[5].coord[0]+math.cos(math.radians(-45))*self.pers[5].width
                    self.pers[5].coord[3]=self.pers[5].coord[1]+math.sin(math.radians(-45))*self.pers[5].width
                    self.pers[5].set_farea(135)
    def crited(self, part,weapon, demage):
        #create blood
        self.w["peaces"].append(blood(20,20,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        self.w["peaces"].append(blood(0,20,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        self.w["peaces"].append(blood(-20,-20,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        self.w["peaces"].append(blood(-20,0,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        self.w["peaces"].append(blood(0,0,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        self.w["peaces"].append(blood(20,0,(0,0,1),[weapon.coord[6],weapon.coord[7]],randint(5,15),10,self))
        #
        part.health-=demage[0]
        #if weapon overlap part in special points: cut this part!!!
    def selfDestroy(self):
     if self.pers[1]:
        self.pers[1].parent=None
        self.pers[0].child=[]
        self.pers[0].look="images//minions//ABC-12//dhead.png"#
#rebuild body(?)
        dhead=DHead([self.pers[0]],self,self.w,math.degrees(math.acos((self.pers[0].coord[2]-self.pers[0].coord[0])/self.pers[0].width)),80)
        #dhead.todo=DestroyToDo
        #dhead.isOverlap=clr
        self.w["peaces"].append(dhead)
        self.canClick=0
     else:
             pass
    def r(self):
            pass
    def reabilitation(self):
            self.r(self)
    #clickleft

    #clickleft1

    def upedLeft(self, touch):
            pass
    def clickRight(self, touch):
        pass
    def clickRight1(self,touch):
        super().clickRight1(touch)
        x=touch['x']
        y=touch['y']
        if self.canClick==1:
            self.c_s=0
            if(x>self.icons[0]['x'] and x<self.icons[0]['x']+self.icon_size and y<self.client_height-self.icons[0]['y'] and y>self.client_height-self.icons[0]['y']-self.icon_size):
                self.handKikc()
                self.extra_icons_position=-self.icon_size
                        
            elif(x>self.icons[1]['x'] and x<self.icons[1]['x']+self.icon_size and y<self.client_height-self.icons[1]['y'] and y>self.client_height-self.icons[1]['y']-self.icon_size):
                self.legKikc()
                self.extra_icons_position=-self.icon_size
            elif(x>self.icons[2]['x'] and x<self.icons[2]['x']+self.icon_size and y<self.client_height-self.icons[2]['y'] and y>self.client_height-self.icons[2]['y']-self.icon_size and self.pers[5]):
                self.c_s=1
                self.extra_icons_position=self.icons[2]['y']
            elif(x>self.icons[3]['x'] and x<self.icons[3]['x']+self.icon_size and y<self.client_height-self.icons[3]['y'] and y>self.client_height-self.icons[3]['y']-self.icon_size and self.pers[3]):
                self.c_s=2
                self.extra_icons_position=self.icons[3]['y']
            elif(x>self.icons[4]['x'] and x<self.icons[4]['x']+self.icon_size and y<self.client_height-self.icons[4]['y'] and y>self.client_height-self.icons[4]['y']-self.icon_size):
                self.c_s=3
                self.destroyMessage=True
            elif  self.extra_icons_position!=-self.icon_size:
                  self.extra_icons_position=-self.icon_size
    def upedRight(self,touch):
            pass
    def CanShoot(self):
            self.can_shoot=True
    def CanShoot1(self):
            self.can_shoot1=True
    def clickCenter(self, touch):
        unwas=True
        for t in self.centerTouch:
                if t['id']==touch['id']:
                        unwas=False
                        t['x']=self.transform_coords(touch['x'],touch['y'])[0]
                        t['y']=self.transform_coords(touch['x'],touch['y'])[1]
                        break
        if unwas:
                self.centerTouch.append({'x':self.transform_coords(touch['x'],touch['y'])[0],'y':self.transform_coords(touch['x'],touch['y'])[1],'id':touch['id']})
        if self.canClick==1:
           if(self.c_s==0):
                if self.bullets_n>0:
                        x,y=self.transform_coords(touch['x'],touch['y'])
                        if(self.laa_style==1 and self.left_arm_animation==False  and self.can_shoot):
                            ug = (math.acos(((self.pers[3].coord[2]) * x + (self.pers[3].coord[1]) * y) / (math.sqrt((self.pers[3].coord[2]) * (self.pers[3].coord[2]) + (self.pers[3].coord[1]) * (self.pers[3].coord[1])) * math.sqrt(x * x + y * y))))
                            A=[self.centerTouch[0]['x']-(self.pers[3].coord[2]),self.centerTouch[0]['y']-(self.pers[3].coord[1])]
                            dl=math.sqrt(A[0]**2+A[1]**2)
                            power = self.pers[0].height * 2
                            b=[element()]
                            b[0].height=self.pers[0].height/15
                            b[0].width=b[0].height*3
                            b[0].look=self.bull
                            b[0].coord[2]=self.pers[3].coord[2]
                            b[0].coord[1]=self.pers[3].coord[1]
                            b[0].coord[0]=b[0].coord[2]+A[0]/dl*b[0].width
                            b[0].coord[3]=b[0].coord[1]+A[1]/dl*b[0].width
                            b[0].coord[6]=b[0].coord[0]-(A[1]/dl)*b[0].height
                            b[0].coord[5]=b[0].coord[3]+(A[0]/dl)*b[0].height
                            b[0].coord[4]=b[0].coord[6]-(A[0]/dl)*b[0].width
                            b[0].coord[7]=b[0].coord[5]-(A[1]/dl)*b[0].width
                            b[0].face=self.face
                            #self.w["bullets"].append(bullet(math.cos(ug) * power, math.sin(ug) * power, (120, 10, "saw"),b,self))
                            self.w["bullets"].append(bullet(A[0]/dl * power, A[1]/dl * power, (120, 10, "saw",1),b,self,touch))
                            self.bullets_n-=1
                            self.can_shoot=False
                            Timer(0.3, self.CanShoot).start()
                            #Clock.schedule_interval(self.CanShoot, 1)
                        if(self.waa_style==1 and self.write_arm_animation==False  and self.can_shoot1):
                            #ug =(math.acos(((self.pers[5].coord[2]+self.dx) * x + (self.pers[5].coord[1]+self.dy) * y) / (math.sqrt((self.pers[5].coord[2]+self.dx) * (self.pers[5].coord[2]+self.dx) + (self.pers[5].coord[1]+self.dy) * (self.pers[5].coord[1]+self.dy)) * math.sqrt(x * x + y * y))))
                            if(self.laa_style==1 and self.left_arm_animation==False and len(self.centerTouch)>1):
                                    A=[self.centerTouch[1]['x']-(self.pers[5].coord[2]+self.dx),self.centerTouch[1]['y']-(self.pers[5].coord[1]+self.dy)]
                            else:
                                    A=[self.centerTouch[0]['x']-(self.pers[5].coord[2]+self.dx),self.centerTouch[0]['y']-(self.pers[5].coord[1]+self.dy)]
                            dl=math.sqrt(A[0]**2+A[1]**2)
                            power = self.pers[0].height * 2
                            b=[element()]
                            b[0].height=self.pers[0].height/15
                            b[0].width=b[0].height*3
                            b[0].look=self.bull
                            b[0].coord[2]=self.pers[5].coord[2]
                            b[0].coord[1]=self.pers[5].coord[1]
                            b[0].coord[0]=b[0].coord[2]+A[0]/dl*b[0].width
                            b[0].coord[3]=b[0].coord[1]+A[1]/dl*b[0].width
                            b[0].coord[6]=b[0].coord[0]-(A[1]/dl)*b[0].height
                            b[0].coord[5]=b[0].coord[3]+(A[0]/dl)*b[0].height
                            b[0].coord[4]=b[0].coord[6]-(A[0]/dl)*b[0].width
                            b[0].coord[7]=b[0].coord[5]-(A[1]/dl)*b[0].width
                            b[0].face=self.face
                            #self.w["bullets"].append(bullet(math.cos(ug) * power, math.sin(ug) * power, (120, 10, "saw"),b,self))
                            self.w["bullets"].append(bullet(A[0]/dl * power, A[1]/dl * power, (120, 10, "saw",1),b,self,touch))
                            self.bullets_n-=1
                            self.can_shoot1=False
                            Timer(0.3, self.CanShoot1).start()
                            #Clock.schedule_interval(self.CanShoot1, 1)
        if self.canClick==3:
            if touch['x']>self.width/2:
                self.screenpos[0]+=self.go
            else:
                self.screenpos[0]-=self.go
            if touch['y']>self.height/2:
                self.screenpos[1]+=self.go
            else:
                self.screenpos[1]-=self.go
    def clickCenter1(self, touch):
        super().clickCenter1(touch)
        x=touch['x']
        y=touch['y']
        if self.canClick==1:
            if(self.c_s==1):
                if(x>self.extra_icons[0]['x'] and x<self.extra_icons[0]['x']+self.icon_size and y<self.client_height-self.extra_icons[0]['y'] and y>self.client_height-self.extra_icons[0]['y']-self.icon_size):
                    if(self.laa_style!=1):
                        self.left_arm_animation=True
                        self.laa_style=1
                        self.lai=0
                        self.hand2img=self.extra_icons[0]['l']
                elif(x>self.extra_icons[1]['x'] and x<self.extra_icons[1]['x']+self.icon_size and y<self.client_height-self.extra_icons[1]['y'] and y>self.client_height-self.extra_icons[1]['y']-self.icon_size):
                    if(self.laa_style!=2):
                        self.left_arm_animation=True
                        self.laa_style=2
                        self.lai=0
                        self.icons[2]['l']=self.extra_icons[1]['l']
                elif(x>self.extra_icons[2]['x'] and x<self.extra_icons[2]['x']+self.icon_size and y<self.client_height-self.extra_icons[2]['y'] and y>self.client_height-self.extra_icons[2]['y']-self.icon_size):
                    if(self.laa_style!=3):
                        self.left_arm_animation=True
                        self.laa_style=3
                        self.lai=0
                        self.hand2img=self.extra_icons[2]['l']
                elif(x>self.extra_icons[3]['x'] and x<self.extra_icons[3]['x']+self.icon_size and y<self.client_height-self.extra_icons[3]['y'] and y>self.client_height-self.extra_icons[3]['y']-self.icon_size):
                    if(self.laa_style!=4):
                        self.left_arm_animation=True
                        self.laa_style=4
                        self.lai=0
                        self.hand2img=self.extra_icons[3]['l']
                self.c_s=0
                self.can_shoot1=False
                self.extra_icons_position=-self.icon_size
                Timer(0.25, self.CanShoot1).start()#
            elif (self.c_s==2):
                if(x>self.extra_icons[0]['x'] and x<self.extra_icons[0]['x']+self.icon_size and y<self.client_height-self.extra_icons[0]['y'] and y>self.client_height-self.extra_icons[0]['y']-self.icon_size):
                    if(self.waa_style!=1):
                        self.write_arm_animation=True
                        self.waa_style=1
                        self.wai=0
                        self.hand3img=self.extra_icons[0]['l']
                elif(x>self.extra_icons[1]['x'] and x<self.extra_icons[1]['x']+self.icon_size and y<self.client_height-self.extra_icons[1]['y'] and y>self.client_height-self.extra_icons[1]['y']-self.icon_size):
                    if(self.waa_style!=2):
                        self.write_arm_animation=True
                        self.waa_style=2
                        self.wai=0
                        self.hand3img=self.extra_icons[1]['l']
                elif(x>self.extra_icons[2]['x'] and x<self.extra_icons[2]['x']+self.icon_size and y<self.client_height-self.extra_icons[2]['y'] and y>self.client_height-self.extra_icons[2]['y']-self.icon_size):
                    if(self.waa_style!=3):
                        self.write_arm_animation=True
                        self.waa_style=3
                        self.wai=0
                        self.hand3img=self.extra_icons[2]['l']
                elif(x>self.extra_icons[3]['x'] and x<self.extra_icons[3]['x']+self.icon_size and y<self.client_height-self.extra_icons[3]['y'] and y>self.client_height-self.extra_icons[3]['y']-self.icon_size):
                    if(self.waa_style!=4):
                        self.write_arm_animation=True
                        self.waa_style=4
                        self.wai=0
                        self.hand3img=self.extra_icons[3]['y']
                self.c_s=0
                self.extra_icons_position=-self.icon_size
                self.can_shoot=False
                Timer(0.25, self.CanShoot).start()
            elif (self.c_s==3):
                #if(x>self.dokX and x<self.dokX+self.dokW and y<self.height-self.dokY and y>self.height-self.dokY-self.dokH):
                if(x>self.dokX and x<self.dokX+self.dokW and y<self.client_height-self.dokY and y>self.client_height-self.dokY-self.dokH):
                    self.selfDestroy()
                self.c_s=0
                self.destroyMessage=False
    def upedCenter(self, touch):
            for t in self.centerTouch:
                if t['id']==touch['id']:
                    self.centerTouch.remove(t)#
                    print(self.centerTouch)
    def bot(self):
        if self.canClick!=0:
                self.handKikc()
        self.waa_style=2
        self.pers[5].width=self.pers[4].width/70*166
        self.pers[5].height=self.pers[4].height/180*131
        self.pers[5].look=self.saw
        self.inertion()
        self.animation()
        self.attack()

        for i in range(len(self.extra_functions)):
                self.extra_functions[i](self)
        if self.isAlive==False:
                self.endGame=True

class DHead():
    def __init__(self,e,o,w,p1,p2):
            self.ug=p1
            self.power=p2
            self.pers=e
            self.owner=o
            self.w=w

    def todo(self,s=None):
        if(self.power>0):
            self.pers[0].coord[0]=self.pers[0].coord[0]+math.cos(math.radians(self.ug+90))*self.power
            self.pers[0].coord[1]=self.pers[0].coord[1]+math.sin(math.radians(self.ug+90))*self.power
            self.pers[0].coord[2]=self.pers[0].coord[0]+math.cos(math.radians(self.ug))*self.pers[0].width
            self.pers[0].coord[3]=self.pers[0].coord[1]+math.sin(math.radians(self.ug))*self.pers[0].width
            self.pers[0].coord[4]=self.pers[0].coord[2]+math.cos(math.radians(self.ug+90))*self.pers[0].height
            self.pers[0].coord[5]=self.pers[0].coord[3]+math.sin(math.radians(self.ug+90))*self.pers[0].height
            self.pers[0].coord[6]=self.pers[0].coord[4]+math.cos(math.radians(self.ug+180))*self.pers[0].width
            self.pers[0].coord[7]=self.pers[0].coord[5]+math.sin(math.radians(self.ug+180))*self.pers[0].width
            self.ug-=5
            self.pers[0].rotation=self.ug
            self.power-=1
        elif self.power==0:
            self.pers[0].coord[0]=self.pers[0].coord[0]-self.pers[0].width*4#?
            self.pers[0].coord[1]=self.pers[0].coord[1]-self.pers[0].height*4#?
            self.pers[0].width*=10
            self.pers[0].height*=10
            self.pers[0].calcF()
            self.pers[0].look="images\\minions\\ABC-12\\animation\\change weapon 1.png"
            self.power-=1
        elif self.power>-51:
            self.pers[0].look="images\\minions\\ABC-12\\animation\\change weapon "+ (str)((-self.power)%2+1)+".png"
            #print(self.pers[0].look)
            #overlap and attack
            self.power-=1

    def isOverlap(self,w):
         if self.power==-51:
            self.owner.isAlive=False
            self.owner.canClick=2
            self.pers[0].width=0
            self.pers[0].height=0
            self.pers[0].calcF()
            self.owner.screenpos=[self.pers[0].coord[4],self.pers[0].coord[7]]
            self.w["peaces"].remove(self)

            self.owner.messages[0]['a']=True
            self.owner.messages[1]['a']=True
            self.owner.messages[2]['a']=True
            self.owner.messages[0]['l']='images//youdead.png'
            #with self.owner.canv:
            #    self.owner.youdead=Rectangle(pos=(self.owner.rdX,self.owner.rdY),size=(self.owner.rdW,self.owner.rdH),source='images\\youdead.png')
            #    self.owner.youdeadC=Rectangle(pos=(self.owner.rdX+self.owner.rdW/2,self.owner.rdY+self.owner.rdH/20),size=(self.owner.rdW/603*281,self.owner.rdH/216*42),source='images\\exit.png')
            #    self.owner.youdeadW=Rectangle(pos=(self.owner.rdX+self.owner.rdW/2,self.owner.youdeadC.pos[1]+self.owner.youdeadC.size[1]+self.owner.rdH/20),size=(self.owner.rdW/603*281,self.owner.rdH/216*42),source='images\\watch.png')
            self.power-=1



#robot=ABC_12(1000,500,(1000.0, 0.0, 1),0)
#robot.i=-31
#robot.toStatic()
#w=[Map(1000,500),[robot],[],[]]
#robot.selfDestroy(w)
#while True:
#    self.w["peaces"][0].todo(self.w["peaces"][0])
#robot.waa_style=2
#robot.write_arm_animation=True
#robot.clickCenter1(35,35,[Map(1000,500),[robot],[],[]])
#robot.waa_style=3
#while(robot.write_arm_animation):
#    robot.animation()
#robot.pers[0].overlap(robot.pers[3])
#robot.jump()
#robot=ABC_12(1000,500,(0.0, 0.0, 1))
#word=[Map(100,700),[robot],[],[]]
#robot.handKikc()
#while True:
#    robot.toStatic()
#    robot.inertion(Map(1000,500))
#    robot.attack(word)
#    robot.goRight(Map(1000,500))
#robot.animation()
#robot.attack(10)

#robot.bot()

#robot.drawLeft_init(0,'','','',10,10)

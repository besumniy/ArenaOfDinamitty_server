from sources.element import *

#from kivy.core.window import Window
#from kivy.graphics import * #

from random import randint

class Map():
    def __init__(self,w,h):
        self.height=1000#?
        self.width=1500

        ###
        ##self.directoty="images\\"
        self.wall="images\\control fone.png"
        self.background=None
        self.extra_texture=[]

       

    def returnPlace(self):
        r=randint(0,len(self.places)-1)
        return self.places.pop(r)
        
    def todo(self,w):
        self.w=w
        for warrior in self.w['warriors']:
            if warrior.pers[0].coord[7]<self.height*(-3):
               warrior.pers[0].health=0

print('ok')
#print(m.returnPlace())
#print(m.returnPlace())

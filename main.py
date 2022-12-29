import importlib

import threading
import socket
import json

import os

from random import randint

query=[]
using_ports=set()
using_port=8082

def with_client(client,i):
    client['get']=json.loads(str(client['connection'].recv(1024),'utf-8')[2:])
    #print('ok:',client['get'])
    #client[0].sendall('wait'.encode('utf-8'))

    threading.Thread(target=GET,args=[client,i]).start()
    threading.Thread(target=SEND,args=[client,i]).start()
    threading.Thread(target=WAITING,args=[client]).start()

    #while True:
    #    if not client[2]:
    #        #print('nowget',i)
    #        client[2]=json.loads(str(client[0].recv(1024),'utf-8')[2:])
    #        print(client[2])
    #        while not client[3]:
    #            pass
    #        for send in client[3]:
    #            client[0].sendall(send)
    #        print(client[3])
    #        client[3]=None

def GET(client,i):
 while client:
    if not client['get']:
        try:
            #print('nowget',i)
            client['get']=json.loads(str(client['connection'].recv(1024),'utf-8')[2:])
            #print(client['get'],i,'lol')
            #while not client[3]:
            #    pass
            #print('nowsend',i)
        except:
            pass
            #print('OOOPS')
        #if client['get']:
        #    print(client['get'],i,'i geted')
def SEND(client,i):
 while client:
    if client['send']:
            for send in client['send']:
                client['connection'].sendall(send)
            #print(client['send'],i,'sended')
            client['send']=None
def QUERY():
 while True:
    if len(query)>0:
        if query[0]['get']:
            if query[0]['get']['c']=='cancel':
                query[0]['get']=None
                print('ready to cancel',query[0]['send'])
                query[0]['send']=[(6).to_bytes(4,byteorder='big'),'cancel'.encode('utf-8')]
                while query[0]['send']: 
                    print('hehe')
                query[0]['send']=[(4).to_bytes(4,byteorder='big'),'wait'.encode('utf-8')]
                threading.Thread(target=WAITING,args=[query[0]]).start()
                query.remove(query[0])
                print('CANCEL EPTIT', query)
    for i in range(1,len(query)):
     #if query[0]['get'] and query[i]['get']:
        if query[i]['get']:
            if query[i]['get']['c']=='cancel':
                query[i]['get']=None
                query[0]['send']=[(6).to_bytes(4,byteorder='big'),'cancel'.encode('utf-8')]
                while query[0]['send']: 
                    print('hehe')
                query[0]['send']=[(4).to_bytes(4,byteorder='big'),'wait'.encode('utf-8')]
                threading.Thread(target=WAITING,args=[query[i]]).start()
                query.remove(query[i])
                print('CANCEL EPTIT', query)
                break
        if query[0]['info']['n']!=query[i]['info']['n']:
            warriors=[query[0],query[i]]
            query.remove(query[i])
            query.remove(query[0])
            threading.Thread(target=FIGHT_PRE,args=[warriors]).start()
        

def WAITING(client):
 while True:
  if client['get']:
    print('ahah',client['send'])
    get=client['get']['c']
    print('super',get)
    if(get=='directories.txt'):
        path=get
        print(path)
        file=open(path,'rb')##
        data=file.read()
        file.close()
        print(len(data))
        client['connection'].sendall(len(data).to_bytes(4,byteorder='big'))
        client['connection'].sendall(data)
        print()
        file.close()

        path=str(client['connection'].recv(1024),'utf-8')[2:]
        while(path != "finished"):
            print(path)
            file=open(path,'rb')##
            data=file.read()
            file.close()
            client['connection'].sendall(len(data).to_bytes(4,byteorder='big'))
            client['connection'].sendall(data)
            path=str(client['connection'].recv(1024),'utf-8')[2:]
        #disconnect?
    if(get=="fight"):
        client['get']=None
        #send ok
        while not client['get']:
            print(client['send'])
        #for_query=client
        #for_query['warrior_name']=client['get']['n']
        client['info']=client['get']
        client['get']=None
        print(client)
        query.append(client)
    if get=='buy':
        pass
    #client['get']=None
    #print('hmmmm')
    return

def FIGHT_PRE(warriors):
 players=[]
 for warrior in warriors:
        #while not warrior['info']:
        #  pass
        get=warrior['info']
        del warrior['info']
        players.append({'name':get['n'],#players=[]
                'width':0,#get['w'],
                'height':0,#get['h'],
                'warrior':warrior})
 #players[0]['warrior']['get']=None
 #players[1]['warrior']['get']=None
 players[0]['warrior']['send']=[(len(players[1]['name'])).to_bytes(4,byteorder='big'),players[1]['name'].encode('utf-8')]
 players[0]['save']=[(len(players[1]['name'])).to_bytes(4,byteorder='big'),players[1]['name'].encode('utf-8')]
 players[1]['warrior']['send']=[(len(players[0]['name'])).to_bytes(4,byteorder='big'),players[0]['name'].encode('utf-8')]
 players[1]['save']=[(len(players[0]['name'])).to_bytes(4,byteorder='big'),players[0]['name'].encode('utf-8')]


 ########
 num=0
 while True:
    ready=True
    #print('damn:',players)
    for player in players:
     if player['warrior']['get']:
     #while not player['warrior'][2]:
     #    pass
        get=player['warrior']['get']['c']
        if get=='ready':
            print('ok')
            #player['warrior']['send']=[(4).to_bytes(4,byteorder='big'),'okay'.encode('utf-8')]
        if get!='ready':
            print('ALARM!!!')#maybe change send to cl[3]=send
            ready=False
            path=get
            print(path)
            files=os.listdir("sources\\images\\minions\\"+path)
            player['warrior']['get']=True#?
            player['warrior']['send']=None
            send_warrior(files,"sources\\images\\minions\\"+path,player['warrior'])
            player['warrior']['get']=None
            player['warrior']['send']=(['finished'.encode('utf-8')])
     else:
          ready=False
          #if num>10:
          #    for send in player['warrior'][3]:
          #      client[0].sendall(send)
          #    player['warrior'][2]=json.loads(str(conn.recv(1024),'utf-8')[2:])
          
     num+=1

    if ready:
            #for player in players:
            #    player['warrior'][2]=None#?
            print('yahoo')
            Map=importlib.import_module("sources.maps."+maps[2][:-3])#randint(0,len(maps)-1)][:-3])#
            area=Map.Area(1000,1500)
            print(area)
            w=[]
            warriors=[]
            word={'map':[area],'warriors':warriors,'bullets':[],'peaces':[]}#map,warriors,bullets,peaces
            print(players)
            #key=[]
            for player in players:
                #threading.Thread(target=GET_SIZE,args=[player,warriors,w,area,word,key]).start()
                #player['warrior']['get']=None
                #print(player['warrior']['send'])
                #while not player['warrior']['get']:
                #    print(player['warrior'])
                #print(player['warrior']['get'])
                #player['width']=player['warrior']['get']['w']
                #player['height']=player['warrior']['get']['h']
                #player['warrior']['send']=[(4).to_bytes(4,byteorder='big'),'yeah'.encode('utf-8')]
                print(player)
                warrior=importlib.import_module("sources."+player['name']).Warrior(area.returnPlace(),word,player['width'],player['height'])
                warriors.append(warrior)
                w.append({'warrior':warrior,'player':player['warrior']})
                player['warrior']['get']=None
            print(players)
            #while key!=['ok','ok']:
            #    print('waiting....',key)
            w[0]['warrior'].enemies=[w[1]['warrior']]
            w[1]['warrior'].enemies=[w[0]['warrior']]
            
            threading.Thread(target=FIGHT,args=[word,w]).start()
            return

def GET_SIZE(player,warriors,w,area,word,key):
                player['warrior']['get']=None
                print(player['warrior']['send'])
                while not player['warrior']['get']:
                    print(player['warrior'])
                print(player['warrior']['get'])
                player['width']=player['warrior']['get']['w']
                player['height']=player['warrior']['get']['h']
                player['warrior']['send']=[(4).to_bytes(4,byteorder='big'),'yeah'.encode('utf-8')]
                print(player)
                warrior=importlib.import_module("sources."+player['name']).Warrior(area.returnPlace(),word,player['width'],player['height'])
                warriors.append(warrior)
                w.append({'warrior':warrior,'player':player['warrior']})
                player['warrior']['get']=None
                key.append('ok')
                print('KEY;',key)
def FIGHT(word,warriors):
    print('wrrrs:',warriors)
    while True:
     for warrior in warriors:
         #print('warrior1: ',warrior)
         threading.Thread(target=send_world,args=[word,warrior]).start()
         #print('warrior_sended: ',warrior)
     for warrior in warriors:
        if warrior['player']['get']:
                get=warrior['player']['get']
                #print(get)
                #print(warrior)

                warrior['warrior'].touches=get['t']
                warrior['warrior'].touchesD=get['d']
                warrior['warrior'].touchesU=get['u']
                warrior['warrior'].client_width=get['s']['w']
                warrior['warrior'].client_height=get['s']['h']
                warrior['warrior'].init_icons()
                warrior['warrior'].createDarkness()
                warrior['warrior'].lookingOver()
                
                #print(get)
                #print(warrior['warrior'].icons)

                for touch in warrior['warrior'].touchesD:
                    if(touch['x']<warrior['warrior'].client_side_w*2):#fix it
                        #print('clickleft1')
                        warrior['warrior'].clickLeft1(touch)
                    elif(touch['x']>warrior['warrior'].client_side1_x):
                        #print('clickright1')
                        warrior['warrior'].clickRight1(touch)
                    #elif(touch['x']>side_w*2 and touch['x']<side1_x):
                    else:
                        #print('clickcenter1')
                        warrior['warrior'].clickCenter1(touch)
                for touch in warrior['warrior'].touchesU:
                    if(touch['x']<warrior['warrior'].client_side_w*2):
                        #print('upleft')
                        warrior['warrior'].upedLeft(touch)
                    elif(touch['x']>warrior['warrior'].client_side1_x):
                        #print('upRight')
                        warrior['warrior'].upedRight(touch)
                    #if(touch['x']>side_w*2 and touch['x']<side1_x):
                    else:
                        #print('upCenter')
                        warrior['warrior'].upedCenter(touch)
                for touch in warrior['warrior'].touches:
                    if(touch['x']<warrior['warrior'].client_side_w*2):
                        #print('clickleft')
                        warrior['warrior'].clickLeft(touch)
                    elif(touch['x']>warrior['warrior'].client_side1_x):
                        warrior['warrior'].clickRight(touch)
                        #print('clickright')
                    #if(touch['x']>side_w and touch['x']<side1_x):
                    else:
                        print('clickcenter')
                        warrior['warrior'].clickCenter(touch)
                #print('its ok')
                warrior['player']['get']=None

        if(not warrior['warrior'].was_go):
                    warrior['warrior'].toStatic()
        if(not warrior['warrior'].was_sit):
                    warrior['warrior'].stand()

        warrior['warrior'].was_go=False
        warrior['warrior'].was_sit=False
        warrior['warrior'].inertion()
        warrior['warrior'].animation()
        warrior['warrior'].attack()

        for i in range(len(warrior['warrior'].extra_functions)):
                    warrior['warrior'].extra_functions[i](warrior['warrior'])
                    

        youwon=True
        for enemy in warrior['warrior'].enemies:
                    if not ((enemy.endGame==True  or enemy.isAlive==False) and warrior['warrior'].canClick!=3):
                        youwon=False
                        break
        if youwon:
                    warrior['warrior'].canClick=2
                    warrior['warrior'].messages[0]['a']=True
                    warrior['warrior'].messages[0]['l']='images//youwon.png'
                    warrior['warrior'].messages[1]['a']=True
                    warrior['warrior'].messages[2]['a']=True

        if warrior['warrior'].exitGame:
            #using_ports.discard(warrior['player']['connection'].laddr[1])###
            send=json.dumps({'c':"exit"})
            #warrior['player']['connection'].sendall(len(send).to_bytes(4,byteorder='big'))
            #warrior['player']['connection'].sendall(send.encode('utf-8'))
            #get=json.loads(str(warrior['player']['connection'].recv(1024),'utf-8')[2:])
            
            warrior['player']['get']=None
            warrior['player']['send']=[len(send.encode('utf-8')).to_bytes(4,byteorder='big'),send.encode('utf-8')]
            print('funnytime')
            
            get=warrior['player']['get']
            while get!='done':
                get=warrior['player']['get']
                warrior['player']['get']=None
                print(get)
            print(get)
            warrior['player']['connection'].close()

            del warrior['player']
            warriors.remove(warrior)
                    #send exit game


     for i in range(len(word['bullets'])-1,-1,-1):
                    word['bullets'][i].todo(word['bullets'][i])
                    if word['bullets'][i].isOverlap(word['bullets'][i],word):
                        word['bullets'].remove(word['bullets'][i])
     for i in range(len(word['peaces'])-1,-1,-1):
                    word['peaces'][i].todo(word['peaces'][i])
                    word['peaces'][i].isOverlap(word)
     word['map'][0].todo(word)



                #send positions for w1 and w2


def send_world(world,warrior):#later add sounds and voices
 player=warrior['warrior']
 #print(player)
 #if player.endGame:
 #       warrior['player']['send']=[json.dumps({'e':'f'}).encode('utf-8')]#send length?
 #       return
 if player.exitGame:
    return
 if not warrior['player']['send']:
    elements=[]
    #scale=player.total_height/450
    scale=player.client_height/1000
    dx=player.returnCameraX()
    dy=player.returnCameraY()
    
    if world['map'][0].background:
        elements.append({'p':world['map'][0].background,
                                         'c':{'x':player.client_side_w*2,
                                              'y':0,#player.client_height,
                                              'w':player.client_game_area_width,
                                              'h':player.client_height,
                                              'r':0}})
    
    for part in world['map'][0].extra_texture:
        elements.append({'p':part.look,
                                         'c':{'x':(int(part.coord[0])-dx)*scale+player.client_side_w*2,
                                              'y':player.client_height-(int(part.coord[1]-dy+part.height)*scale),
                                              'w':int(part.width)*scale,
                                              'h':int(part.height)*scale,
                                              'r':360-(part.rotation)}})
    
    for TYPE in world:
        #print(world[TYPE])
        for unit in world[TYPE]:
            #print(unit)
            for part in unit.pers:
              if part:
               try:
                append=False
                if part.face:
                    #for i in range(0,len(part.coord),2):
                        #if (part.coord[i]>player.pers[0].coord[0]-150 and part.coord[i]<player.pers[0].coord[0]+1350 and
                     #       part.coord[i+1]>player.pers[0].coord[1]-500 and part.coord[i+1]<player.pers[0].coord[1]+500):##возможно, поделить на масштаб
                     #       append=True
                     #       break
                    #if append:
                        elements.append({'p':part.look.replace('\\','//').replace('.png','R.png'),
                                         'c':{'x':(int(part.coord[0])-dx)*scale+player.client_side_w*2,
                                              'y':player.client_height-(int(part.coord[3])-dy+part.height)*scale,
                                              'w':int(part.width)*scale,
                                              'h':int(part.height)*scale,
                                              'r':360-(part.rotation)}})
                else:
                #    for i in range(0,len(part.coord),2):
                #        if (part.coord[i]>player.pers[0].coord[0]-1350 and part.coord[i]<player.pers[0].coord[0]+150 and
                #            part.coord[i+1]>player.pers[0].coord[1]-500 and part.coord[i+1]<player.pers[0].coord[1]+500):
                #            append=True
                #            break
                #    if append:
                       elements.append({'p':part.look.replace('\\','//').replace('R.png','.png'),
                                         'c':{'x':(int(part.coord[2])-dx)*scale+player.client_side_w*2,
                                              'y':player.client_height-(int(part.coord[3])-dy+part.height)*scale,
                                              'w':int(part.width)*scale,'h':int(part.height)*scale,
                                              'r':360-(part.rotation)}})
               except:
                print(part.look)
    darkness=[]
    for part in player.darkness:
        darkness.append({'x':(int(part.coord[0])-dx)*scale+player.client_side_w*2,
                         'y':player.client_height-(int(part.coord[1]-dy)*scale),
                         'x1':(int(part.coord[2])-dx)*scale+player.client_side_w*2,
                         'y1':player.client_height-(int(part.coord[3]-dy)*scale),
                         'x2':(int(part.coord[4])-dx)*scale+player.client_side_w*2,
                         'y2':player.client_height-(int(part.coord[5]-dy)*scale),
                         'x3':(int(part.coord[6])-dx)*scale+player.client_side_w*2,
                         'y3':player.client_height-(int(part.coord[7]-dy)*scale)})
    health_elements=[]
    for i in range(len(player.health)):
        if player.pers[i]:
                health_elements.append({'p':player.health[i].look.replace('\\','//'),
                                        'x':int(player.health[i].coord[0]),
                                        'y':int(player.health[i].coord[1]-player.health[i].height),
                                        'w':int(player.health[i].width),
                                        'h':int(player.health[i].height),
                                        'r':360-(player.health[i].rotation),
                                        'v':player.pers[i].health/player.pers[i].max_health})
    health={'l':health_elements}
    icons=player.icons+player.extra_icons
    messages=[]
    for msg in player.messages:
        if(msg['a']):
            #messages.append({'x':msg['x'],'y':player.client_height-msg['y']-msg['h'],'w':msg['w'],'h':msg['h'],'l':msg['l']})
            messages.append({'x':msg['x'],'y':msg['y'],'w':msg['w'],'h':msg['h'],'l':msg['l']})
    sending_world=json.dumps({'w':elements,'i':icons,'h':health,'m':messages,'d':darkness,'x':int(player.pers[0].coord[0]),'y':int(player.pers[0].coord[1]),'f':player.face}).encode('utf-8')
    warrior['player']['send']=[(len(sending_world)).to_bytes(4,byteorder='big'),sending_world]

    #return sending_world

def send_warrior(files,path,client):
    for file in files:
        #print(file)
        if '.' not in file:
            client['connection'].sendall(len((path+'/'+file).replace('\\','/').encode('utf-8')).to_bytes(4,byteorder='big'))
            client['connection'].sendall((path+'/'+file).replace('\\','/').encode('utf-8'))
            send_warrior(os.listdir(path+'\\'+file),path+'\\'+file,client)
        else:
            f=open(path+'\\'+file,'rb')##
            data=f.read()
            print((path+'/'+file).replace('\\','/').encode('utf-8'))
            print(data)
            f.close()
            client['connection'].sendall(len((path+'/'+file).replace('\\','/').encode('utf-8')).to_bytes(4,byteorder='big'))
            client['connection'].sendall((path+'/'+file).replace('\\','/').encode('utf-8'))
            #print(client[0].recv(1024))
            client['connection'].sendall(len(data).to_bytes(4,byteorder='big'))
            client['connection'].sendall(data)

warriors=os.listdir('sources\\images\\minions')
print(warriors)
maps=os.listdir('sources\\maps')[:-1]
print(maps)


if __name__ == '__main__':
 sock=socket.socket(socket.AF_INET,      # задамем семейство протоколов 'Интернет' (INET)
                          socket.SOCK_STREAM  # задаем тип передачи данных 'потоковый' (TCP)
                          )#proto=0)
 sock.bind(('',8081))
 print(sock)
 sock.listen(1000)
 print(sock)
 i=0

 threading.Thread(target=QUERY).start()

 while True:
     conn,addr=sock.accept()
     print(conn,addr)
     threading.Thread(target=with_client,args=[{'connection':conn,'address':addr,'get':None,'send':[(4).to_bytes(4,byteorder='big'),'wait'.encode('utf-8')],'ee':None},i]).start()#['wait'.encode('utf-8')]
     i+=1

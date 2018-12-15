#!/usr/bin/python3
import numpy as np
import re
import copy

map=list();
car=list();

roadmap={'^':'|', '>':'-', 'v':'|', '<':'-'}
choices = ['left','straight','right']

incmap={'^' : {'mX':-1, 'mY': 0},
        '>' : {'mX': 0, 'mY': 1},
        'v' : {'mX': 1, 'mY': 0},
        '<' : {'mX': 0, 'mY':-1}}

dirmap={ '^|'  :  '^' ,
         '^/'  :  '>' ,
         '^\\' :  '<' ,
         
         '>-'  :  '>' ,
         '>/'  :  '^' ,
         '>\\' :  'v' ,
         
         'v|'  :  'v' ,
         'v/'  :  '<' ,
         'v\\' :  '>' ,
         
         '<-'  :  '<' ,
         '</'  :  'v' ,
         '<\\' :  '^' 
         }

turnmap={'^left'     :  '<' ,
         '^straight' :  '^' ,
         '^right'    :  '>' ,
         
         '>left'     :  '^' ,
         '>straight' :  '>' ,
         '>right'    :  'v' ,

         'vleft'     :  '>' ,
         'vstraight' :  'v' ,
         'vright'    :  '<' ,
         
         '<left'     :  'v' ,
         '<straight' :  '<' ,
         '<right'    :  '^' 
         }
         
def printMap(map,car):
    mcopy=copy.deepcopy(map)
    for c in car:
        mcopy[c['posX']][c['posY']] = c['dir']

    for m in mcopy:
        print("".join(m))

        
def moveTick(car):
    done=False
    crash=set();
    for c in car:
        c['posX'] += incmap[c['dir']]['mX'];
        c['posY'] += incmap[c['dir']]['mY'];
        if map[c['posX']][c['posY']] == '+' :
            combo="".join([ c['dir'], choices[c['turnCnt']%3] ]);
            c['dir']=turnmap[combo]
            c['turnCnt']+=1
        else:
            combo = "".join([c['dir'],map[c['posX']][c['posY']]])
            c['dir'] = dirmap[combo]
        # This is the key... have to check for collisions after each car moves
        # The moves are sequenced, not simultaneous
        # That's dumb... but that is how the problem is stated.
        ret=checkCollision(car)
        for r in ret:
            crash.add(r)

    #delete from the end, so as not to mess up index of identified cars
    for ci in sorted(crash,reverse=True):
        del car[ci]

    if (len(car)==1):
        done=True
        
    return(done)



            
def checkCollision(car):
    allPos=list()
    crashNdx=list();
    for c in car:
        allPos.append((c['posX'],c['posY']))
        
    for pi in range(0,len(allPos)):
        if allPos.count(allPos[pi])>1:
            crashNdx.append(pi)
#            print("crashed car {} at {},{}".format(pi,car[pi]['posY'],car[pi]['posX']))
    return crashNdx



##################################################################            
cnt=0;
with open('input.txt') as f:
#with open('exampleB.txt') as f:
    for line in f:
        map.append([c for c in line.strip('\n')])
        for d in roadmap.keys():
            ndx=[ ndx for ndx,char in enumerate(line.strip('\n')) if char==d]
            for i in ndx:
                car.append({'posX':cnt, 'posY':i,  'dir':d, 'turnCnt':0})
        cnt+=1
for c in car:
    map[c['posX']][c['posY']]=roadmap[c['dir']]

done=False
while (not done):
#    printMap(map,car)
    done=moveTick(car)

print("Final Car remains at {},{}".format(car[0]['posY'],car[0]['posX']))
    
        
    

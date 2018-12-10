#!/usr/bin/python3

import numpy as np
import random
#Input data
#lastMarble=70953*100;
#Nplayers = 405;
lastMarble=1618;
Nplayers = 10;
remaining = [int(x) for x in range(lastMarble,1,-1)];
score=[int(0) for x in range(0,Nplayers)];

circle=[int(0),int(1)];
current = 1;
player=0;

while (len(remaining)>0):
    player=(player+1)%Nplayers
    marble=remaining.pop();
    
    if (marble%23)==0:
        score[player]+=marble;
        ndx=current-7;
        if ndx<0:
            ndx+=len(circle);
        score[player]+=circle.pop(ndx);
        current=ndx;
    else:
        current+=2;
        if current>(len(circle)):
            current-=len(circle);
        circle.insert(current,marble);

    #Printing
    #print("{} {} || ".format(player+1,score[player]),end='');
    #for ndx in range(0,len(circle)):
    #    if ndx==current:
    #        print("({}) ".format(circle[ndx]),end='');
    #    else:
    #        print(" {}  ".format(circle[ndx]),end='');
    #print("");       
    if len(remaining)%10000==0:
        print("Remaining: {}".format(len(remaining)))

# Print solution
print("The solution is {}".format(max(score)));
 







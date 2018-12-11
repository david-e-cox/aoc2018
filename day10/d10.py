#!/usr/bin/python3
import numpy as np
import re

def printMatrix(grid):
    Nx,Ny=np.shape(grid)
    for y in range(Ny):
        for x in range(Nx):
            if grid[x,y]>0:
                print("#",end='');
            else:
                print('.',end='');
        print("");
        
def pos2grid(posX,mX,sX, posY,mY,sY):
    grid=np.zeros([121,31])
    for i in range(len(posX)):
        ndxX=np.round((posX[i]-mX)*sX+60);
        ndxY=np.round((posY[i]-mY)*sY+15);
        grid[ndxX,ndxY]=1
    return grid

posX=list();
posY=list();
vel=list();
with open('input.txt') as f:
    for line in f:
        lineArray = re.split('<|,|>',line);
        posX.append( float(lineArray[1]) )
        posY.append( float(lineArray[2]) )
        vel.append( (float(lineArray[4]),float(lineArray[5])) )

# Hindsight....
preCalc=10350;

done=False
longCnt=0;
while(not done):
    if longCnt>preCalc:
        # Calcualte scaling
        mX=(max(posX)+min(posX))/2
        sX=110/(max(posX)-min(posX))
        mY=(max(posY)+min(posY))/2
        sY=6/(max(posY)-min(posY))
        # print with scaling
        printMatrix(pos2grid(posX,mX,sX, posY,mY,sY))
        print("Time required is {} secs".format(longCnt));
        # allow frame stepping with keyboard
        input()
    #Increment time counter
    longCnt+=1

    # Apply velocities
    cnt=0;
    for vx,vy in vel:
        posX[cnt] = posX[cnt]+vx
        posY[cnt] = posY[cnt]+vy
        cnt+=1;







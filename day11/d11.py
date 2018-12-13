#!/usr/bin/python3
import numpy as np
input=4455

powerLvl=np.zeros([300,300])
sumGrid=list()
ndxGrid=list()
for xi in range(1,301):
    for yi in range(1,301):
        rackId=xi+10
        tmp=rackId*(rackId*yi+input)
        powerLvl[xi-1,yi-1]=( np.floor(tmp/100)- 10*np.floor(tmp/1000))-5

for i in range(0,298):
    for j in range(0,298):
        sumGrid.append(np.sum(powerLvl[i:i+3,j:j+3]))
        ndxGrid.append((i+1,j+1))
print('Part A: Solution is {}'.format(ndxGrid[np.argmax(sumGrid)]))            

runningMax=0
bestAns=0,0,0
for gridSize in range(1,301):
    print("   Grid Check {}/300  Best:{}".format(gridSize,bestAns))
    sumGrid.clear()
    ndxGrid.clear()
    for i in range(0,301-gridSize):
        for j in range(0,301-gridSize):
            sumGrid.append(np.sum(powerLvl[i:i+gridSize,j:j+gridSize]))
            ndxGrid.append((i+1,j+1))
    tmp=max(sumGrid)
    if tmp>runningMax:
        runningMax=tmp
        bestAns=ndxGrid[np.argmax(sumGrid)],gridSize

print('Part B: Solution is {}'.format(bestAns))
            



                       

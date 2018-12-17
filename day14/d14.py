#!/usr/bin/python3
from blist import *

def printScores(scores,elfNDx):
    for i in range(0,len(scores)):
        if i==elfNdx[0]:
            delim=[' (',') ']
        elif i==elfNdx[1]:
            delim=[' [','] ']
        else:
            delim=['  ','  ']
        print("{}{}{}".format(delim[0],scores[i],delim[1]),end='')
    print("")
    
scores=blist();
scores.append(3)
scores.append(7)
elfNdx=[0,1]

nRounds=147061
nPattern =blist([1,4,7,0,6,1])
#nPattern =blist([5,9,4,1,4])

doneA=doneB=False
cnt=0
while ( (not doneA) or (not doneB)):
#    printScores(scores,elfNdx)
    cnt+=1
    total = scores[elfNdx[0]] + scores[elfNdx[1]]
    if (total>9):
        scores.append(int(total/10))
        scores.append(total-10*scores[-1])
        addTwo=True
    else:
        scores.append(total)
        addTwo=False
    elfNdx[0]=(elfNdx[0]+scores[elfNdx[0]]+1)%len(scores)
    elfNdx[1]=(elfNdx[1]+scores[elfNdx[1]]+1)%len(scores)
    #Part A
    if (len(scores)>nRounds+10) and (not doneA):
        strScore = "".join([str(i) for i in scores[nRounds:nRounds+10] ])
        print("Part A: Solution is {}".format(strScore))
        doneA=True

    if (not doneB):
        if cnt%1000000==0:
            print(" Iteration {}".format(cnt))
            
        if scores[-len(nPattern):]==nPattern:
                strScore = "".join([str(i) for i in scores[-len(nPattern):]])
                print("Part B: Solution is {}  {}".format(len(scores)-len(nPattern),strScore))
                doneB=True

        if (addTwo):
            if scores[-len(nPattern)-1:-1]==nPattern:
                strScore = "".join([str(i) for i in scores[-len(nPattern)-1:-1]])
                print("Part B: Solution is {}  {}".format(len(scores)-len(nPattern)-1,strScore))
                doneB=True

    
                  

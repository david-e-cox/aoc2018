#!/usr/bin/python3
import numpy as np

rules=dict()

# get input
#with open('example.txt') as f:
with open('input.txt') as f:
    line = f.readline().rstrip().split(': ')
    # start with 4 pot buffer
    potString="...."+line[1]+"...."
    offset=4;
    potState = [ c for c in potString]
    f.readline()
    for line in f:
        stateAction = line.rstrip().split('=>');
        rules[stateAction[0].strip()]=stateAction[1].strip()

done=False
generation=0
firstPlant = next(i for i in range(len(potState)) if potState[i]=='#')
lastPlant  = next(i for i in range(len(potState)-1,-1,-1) if potState[i]=='#')

potNext=[c for c in potState]
while (not done):
    prevPattern= "".join(potState[firstPlant-1:lastPlant])
    generation+=1
    potState=[c for c in potNext]
    potNext =['.' for c in potNext]
    # Print
    #print("{:>2}: {}".format(generation,"".join(potState[offset-4:])))
    # Evolve
    for i in range(0,len(potState)-5):
        for item in rules.keys():
            if "".join(potState[i:i+5])==item:
                potNext[i+2]=rules[item]


    firstPlant = next(i for i in range(len(potNext)) if potNext[i]=='#')
    lastPlant  = next(i for i in range(len(potNext)-1,-1,-1) if potNext[i]=='#')
    if prevPattern=="".join(potNext[firstPlant:lastPlant+1]):
        print("Stable at generation {}".format(generation))
        activePotList=[ i-offset for i in range(0,len(potNext)) if potNext[i]=='#']
        print("ActivePotList:",end='')
        print(activePotList)
        print('Part B: Solution maybe is {}'.format(sum(activePotList)))
        input()
        # okay... no clean end here.
        # I thought I had an off-by-one in my first/last selection
        # But really the pattern moves.
        # Found the delta per iteration (23) and came up with
        # Solution = 3056 + (50e9 -113)*23 = 1150000000457
        # Got a star....

    # Increase garden size, if nearing endpoints        
    if (len(potNext)-lastPlant)<5:
        for _ in range(0,4):
            potNext.append('.')
        
    if (firstPlant<5):
        for _ in range(0,4):
            potNext.insert(0,'.')
        offset+=4

    #Determine active pots at gen20
    if (generation==19):
        activePotList=[ i-offset for i in range(0,len(potNext)) if potNext[i]=='#']
        print('Part A: Solution is {}'.format(sum(activePotList)))


#Print last iteration
#print("{:>2}: {}".format(generation,"".join(potNext[offset-4:])))


            



                       

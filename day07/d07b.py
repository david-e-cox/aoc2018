#!/usr/bin/python3

import numpy as np

#Input data
preReq = dict();
#EXAMPLE
#preReq['C']=['A','F'];
#preReq['A']=['B','D'];
#preReq['B']=['E'];
#preReq['D']=['E'];
#preReq['F']=['E'];
with open('input.txt') as f:
    for line in f:
        l=line.split();
        if l[1] in preReq.keys():
            preReq[l[1]].append(l[7]);
        else:
            preReq[l[1]] = list(l[7]);

timeSpent=dict();
# Create time map for each step
for ascii in range(65,65+26):
    #EXAMPLE    timeSpent[chr(ascii)] = ascii-64;
    timeSpent[chr(ascii)] = 60+ascii-64;


allSteps=set(preReq.keys())
for key in preReq.keys():
    for step in preReq[key]:
        allSteps.add(step);

#EXAMPLE workerTime=np.array([0,0]);
workerTime=np.array([0,0,0,0]);
workerTask=[".",".",".","."];

time=0;
instructions=list();
dependsOn=set();
done=False;
while(not done):
    #Create list of steps which depend on something unfinished
    dependsOn.clear();
    for key in preReq.keys():
        for step in preReq[key]:
            dependsOn.add(step);
    # Find steps with no dependency, pull first one
    nextSteps = sorted(set(preReq.keys()).difference(dependsOn));
    # If we are out of steps with no dependency, instead use all unfinished steps
    if len(nextSteps)==0:
        nextSteps = sorted(allSteps.difference(instructions));

    # Assign steps to available workers, set busy time
    for step in nextSteps:
        if step not in workerTask:
            for worker in np.where(workerTime==0)[0]:
                workerTime[worker]=timeSpent[step];
                workerTask[worker]=step;
                break;

    #EXAMPLE print("{}\t{}\t{}\t{}".format(time,workerTask[0],workerTask[1],"".join(instructions)));

    # exit condition, everyone is idle
    if np.all(workerTime==0):
        done=True;

    # Passage of time, for busy workers
    workerTime[np.where(workerTime>0)] -= 1;
    
    # For idle workers check task and remove from preReq set
    for ndx in np.where(workerTime==0)[0]:
        if (workerTask[ndx]!='.'):
            instructions.append(workerTask[ndx]);
            if workerTask[ndx] in preReq.keys():
                del preReq[workerTask[ndx]] 
            workerTask[ndx]=".";
    # Increment clock        
    time+=1;

# Print solution
print("Part B: Solution is {}".format(time-1));







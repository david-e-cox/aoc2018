#!/usr/bin/python3

import numpy as np

#Input data
preReq = dict();
preReq['C']=['A','F'];
preReq['A']=['B','D'];
preReq['B']=['E'];
preReq['D']=['E'];
preReq['F']=['E'];
with open('input.txt') as f:
    for line in f:
        l=line.split();
        if l[1] in preReq.keys():
            preReq[l[1]].append(l[7]);
        else:
            preReq[l[1]] = list(l[7]);

# Find all steps, the comprehensive list
allSteps=set(preReq.keys())
for key in preReq.keys():
    for step in preReq[key]:
        allSteps.add(step);

#Building instructions, the order list of steps
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
    if len(nextSteps)==0:
        remaining = sorted(allSteps.difference(instructions));
        for r in remaining:
            instructions.append(r);
        done=True;
    else:
        instructions.append(nextSteps[0]);
        # nextStep executed, it is no longer a preReq
        del preReq[nextSteps[0]];


# Print solution
print("Part A: Solution is {}".format("".join(instructions)));
 







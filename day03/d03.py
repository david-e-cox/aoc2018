#!/usr/bin/python3

import numpy as np
import re

index=list();
X0=list();
Y0=list();
Xd=list();
Yd=list();

Grid=np.zeros([1000,1000],np.int16);

# Input data
with open('input.txt') as f:
    for line in f:
        lineArray = re.split('#|,|@|x|:| ',line);
        index.append(int(lineArray[1]));
        X0.append(int(lineArray[4]));
        Y0.append(int(lineArray[5]));
        Xd.append(int(lineArray[7]));
        Yd.append(int(lineArray[8]));
f.close()
           
for i in range(0,len(index)):
    # Compute cumlative overlap grid for used patch calc (PartA)
    Grid[X0[i]:X0[i]+Xd[i],Y0[i]:Y0[i]+Yd[i]] += np.ones((Xd[i],Yd[i]),np.int16);

overlap=np.where(Grid>1);
print("Part A: Solution is {0:d}\n".format(len(overlap[0])));

# Find areas, potential speed up in conflict detection
areaInv = [1/(Xd[i]*Yd[i]) for i in range(0,len(index))];
# Inital list of unconflicted patches, includes all.
cleanList=[x for x in range(0,len(index))];

dirtySet=set();
cnt=0
# Start with comparison to largest elements first
for i in np.argsort(areaInv):
    dirtySet.clear();
    # Check all previously unconflicted patches against current patch
    for j in cleanList:
        # This is lazy... should be a convex hull kind of way to do this...
           PatchMap=np.zeros([1000,1000],np.int8);
           if (i!=j):
               PatchMap[X0[j]:X0[j]+Xd[j],Y0[j]:Y0[j]+Yd[j]]  = np.ones((Xd[j],Yd[j]),np.int8);
               PatchMap[X0[i]:X0[i]+Xd[i],Y0[i]:Y0[i]+Yd[i]] += np.ones((Xd[i],Yd[i]),np.int8);
           if (np.any(PatchMap>1)):
               dirtySet.add(j);
    #Remove those which had conflicts, shorten's next iteration
    for k in dirtySet:
        cleanList.remove(k);
    # Progress...
    if (cnt%25==0):
        print("  Progress {0:d}/{1:d} cleanList Size:{2:d}".format(cnt,len(index),len(cleanList)));
    cnt+=1;

print("\nPart B: Solution is {0:d}".format(index[cleanList[0]]));


    

            


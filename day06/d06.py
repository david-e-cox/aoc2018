#!/usr/bin/python3

import numpy as np

#Input data
#Pos = [(1, 1),(1, 6),(8, 3),(3, 4),(5, 5),(8, 9)];
with open('input.txt') as f:
    Pos=[tuple(map(int, xy.split(','))) for xy in f];

Npts=len(Pos);

# Pick a grid size, outsize all the points
Ngrid = 512;

# Create 3 Dim array of distances from each point to all coordinates
distMap  = np.zeros([Ngrid,Ngrid,Npts]);
coorMapX = np.tile(range(0,Ngrid),[Ngrid,1]);
coorMapY = coorMapX.T

cnt=0
# For every point calcuate distance-to over grid, and store everything
for (x,y) in Pos:
    distMap[:,:,cnt] = np.abs(coorMapX-x) + np.abs(coorMapY-y);
    cnt=cnt+1;

# find minimum distance to a point over grid
minDist  = np.min(distMap,axis=2);
# find coordinates (index) of closest point, over grid
closeNdx = np.argmin(distMap,axis=2);

# Check for duplicate distances, one point at a time
for i in range(0,Npts):
    # Close coordiantes for this point
    (x,y)=np.where(closeNdx==i);
    for xi,yi in zip(x,y):
        # If another point has the same distance, mark with -1 in closeNdx
        if len(np.where(minDist[xi,yi]==distMap[xi,yi,:])[0]) > 1:
            closeNdx[xi,yi]=-1;

# Determine infinites, here just taking boundary points
# This should work if grid is sufficently large
isInfinite=set();
# Check Boundaries
for yi in [0,Ngrid-1]:
    for xi in range(0,Ngrid):
        isInfinite.add(closeNdx[xi,yi]);

for xi in [0,Ngrid-1]:
    for yi in range(0,Ngrid):
        isInfinite.add(closeNdx[xi,yi]);

# Calcuate size of non-infinite        
spaceCnt=set();
for i in range(0,Npts):
    if i not in isInfinite:
        spaceCnt.add(len(np.where(closeNdx==i)[0]));
    
# Print solution
print("Part A: Solution is {0:d}".format(max(spaceCnt)));
# Yea, part A's structure paid off!
print("Part B: Solution is {0:d}".format(len(np.where(np.sum(distMap,axis=2)<10000)[0])));


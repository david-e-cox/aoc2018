#!/usr/bin/python3

import numpy as np
# Example problems
#inval=[-6, +3, +8, +5, -6];
#inval=[+3, +3, +4, -2, -4]
inval=[+7, +7, -2, -7, -4];

# Input data
f=open('input.txt');
inval =[int(val) for val in f.read().split()];
f.close()

# Initialize sets
seenSet=set();
dupSet =set();

out = np.cumsum(inval);
print (" Part A: Solution is {0:d}".format(out[-1]));

# Create a set of previously seen values
for val in out:
    seenSet.add(val);

done=False;
while (not done):    
    newlist = out[-1]+np.cumsum(inval);
    out = np.append(out,newlist);
    # Check new list for duplicates with seenSet, if so add to dupSet
    for val in newlist:
        if (val in seenSet):
            dupSet.add(val);
            break;
        else:  # add this unique value to the seenSet 
            seenSet.add(val);

    # check to duplist to find the first occurance in the ordered list
    for val in out:  
        if (val in dupSet):
            print(" Part B: Solution is {0:d}".format(val));
            done=True;
            break;
            

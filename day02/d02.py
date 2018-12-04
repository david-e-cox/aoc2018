#!/usr/bin/python3

import numpy as np
inval=["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"];

# Input data
f=open('input.txt');
inval =f.read().split();
f.close()

# Initialize sets
d=dict();
twoCount=0;
threeCount=0;
for i in range(len(inval)):
    d.clear();
    for let in inval[i]:
        d[let] = d.get(let,0)+1

    for let in d:
        if d[let]==2:
            twoCount+=1;
            break;
        
    for let in d:
        if d[let]==3:
            threeCount+=1;
            break;
        
print (" Part A: Solution is {}".format(twoCount*threeCount));

for i in range(len(inval)):
    for j in range(i+1,len(inval)):
        errorCount=0;
        for k in range(len(inval[i])):
            if (inval[i][k] != inval[j][k]):
                errorCount+=1;
                if (errorCount>1):
                    break;
                krm=k;

        if (errorCount==1):
            print (" Part B: Solution is {}".format(inval[i][0:krm-1]+inval[i][krm+1:]));
            break;

            
            


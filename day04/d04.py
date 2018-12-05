#!/usr/bin/python3

import numpy as np
import re

year  =list();
month =list();
day   =list();
hour  =list();
minute=list();
idnum =list();
action=list();

# Input data
with open('input.txt') as f:
    for line in f:
        lineArray=re.split("-|:| ",re.sub("\[|\]|#","",line));
        year.append(  int(lineArray[0]));
        month.append( int(lineArray[1]));
        day.append(   int(lineArray[2]));
        hour.append(  int(lineArray[3]));
        minute.append(int(lineArray[4]));
        if lineArray[5]=="Guard":
            idnum.append(int(lineArray[6]));
            action.append(0);
        else:
            idnum.append(-1);
            if lineArray[5]=="wakes":
                action.append(+1);
            else:
                action.append(-1);
f.close()

# Sort data, store in np arrays
sortMetric = np.array(year)*372+np.array(month)*31+np.array(day)+np.array(hour)/24+np.array(minute)/24/60;
ndx=np.argsort(sortMetric);
h=np.array(hour);  h=h[ndx];
m=np.array(minute);m=m[ndx];
id=np.array(idnum);id=id[ndx];
a=np.array(action);a=a[ndx];

# populate guard id vector with repeated entries
gid=list();
guards=set();
for i in range(0,len(id)):
    if id[i]>0:
        gid.append(id[i]);
        gidLast=id[i];
        guards.add(id[i]);
    else:
        gid.append(gidLast);
gid=np.array(gid);

# create unique ordered list of guards
gunique = np.array([x for x in guards]);

# Find guard who has slept the most
sleepDuration=np.zeros([len(gunique),1]);
minBymin=np.zeros([len(gunique),60]);
for i in range(0,len(gunique)):
    guardNdx=np.where(gid==gunique[i])[0];
    for j in range(0,len(guardNdx)):
        if (guardNdx[j]+1<len(a) and a[guardNdx[j]]<0):
            sleepDuration[i] += m[guardNdx[j]+1] - m[guardNdx[j]];
            for t in range(0,59):
                if (t<m[guardNdx[j]+1] and t>=m[guardNdx[j]]):
                    minBymin[i,t]+=1;                


# Find the sleepy guard
sleepyGuard=gunique[np.argmax(sleepDuration)];
# Find that guards most inactive minute
bestMinute =np.argmax(minBymin[np.argmax(sleepDuration),:]);
print("Part A: Solution is {0:d}*{1:d} = {2:d}".format(sleepyGuard,bestMinute,sleepyGuard*bestMinute));

# Find consistent guard
max2d=np.unravel_index(np.argmax(minBymin,axis=None),minBymin.shape);
print("Part B: Solution is {0:d}*{1:d} = {2:d}".format(gunique[max2d[0]],max2d[1],gunique[max2d[0]]*max2d[1]));
      

#!/usr/bin/python3

#Ngrid=10  # for example  
Ngrid=50

def printMap(map):
    for i in range(0,Ngrid):
        print("")
        for j in range(0,Ngrid):
            print(map[i*Ngrid+j],end='')
    print("")


# Function to return linear indices of eight neighboors, if they are within map
def nearEight(ndx):
    if ndx%Ngrid==0:  # Left Edge
        nEight = [ndx+1,
                  ndx+Ngrid,ndx+Ngrid+1,
                  ndx-Ngrid,ndx-Ngrid+1]
    elif (ndx+1)%Ngrid==0:  # Right Edge
        nEight = [ndx-1,
                  ndx+Ngrid,ndx+Ngrid-1,
                  ndx-Ngrid,ndx-Ngrid-1]
    else:  #interior to map
        nEight = [ndx-1,ndx+1,
                  ndx+Ngrid,ndx+Ngrid-1,ndx+Ngrid+1,
                  ndx-Ngrid,ndx-Ngrid-1,ndx-Ngrid+1]
    # top/bottom edge have neighboors that are outside of bounds
    within = [x for x in nEight if x>0 and x<Ngrid*Ngrid]
    # Return list of objects from map at neighboor locations
    return list(map[i] for i in within);

# Read input
map=[]
with open('input.txt') as f:
    for line in f:
        for c in line.strip():
            map.append(c)


# Initialize
cnt=0
endNdx=1000
seen=[]
firstRepeat=-1

done=False
while (not done):
#    printMap(map)
    newMap=['-' for c in map];

    for ndx in range(0,len(map)):
        if map[ndx]=='.':
            if sum([1 for c in nearEight(ndx) if c=='|']) >= 3:
                newMap[ndx]='|'
            else:
                newMap[ndx]=map[ndx]
            continue

        if map[ndx]=='|':
            if sum([1 for c in nearEight(ndx) if c=='#']) >= 3:
                newMap[ndx]='#'
            else:
                newMap[ndx]=map[ndx]
            continue

        if map[ndx]=='#':
            if ( sum([1 for c in nearEight(ndx) if c=='#']) >=1 and sum([1 for c in nearEight(ndx)if c=='|']) >= 1 ):
                newMap[ndx]='#'
            else:
                newMap[ndx]='.'

    map=[c for c in newMap]            

    if "".join(map) in seen and firstRepeat<0:
        firstRepeat=seen.index("".join(map))
        period=cnt-firstRepeat
        endNdx=((1000000000-firstRepeat)%period+firstRepeat)-1
        print("  Repeated pattern at iterations {} and {}, period={}".format(firstRepeat,cnt,period))
        print("  Solution occurs at {}".format(endNdx))
        print("Part B: Solution is {}".format(sum([1 for c in seen[endNdx] if c=='|'])*sum([1 for c in seen[endNdx] if c=='#'])))
        done=True

    seen.append("".join(map))
    cnt+=1

    if cnt==10:
        print("Part A: Solution is {}".format(sum([1 for c in map if c=='|'])*sum([1 for c in map if c=='#'])))
        
        

        
    



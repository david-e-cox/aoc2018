#!/usr/bin/python3

# Input data
#input="dabAcCaCBAcCcaDA"
with open('input.txt') as f:
    input=f.read().rstrip('\n');
f.close()

# Initiaze exit criteria
oldLen=-1;
done=False;

# Create set of unique elements in polymer
unique=set([c.lower() for c in input]);

# replace aA,Aa, bB etc combos
while(not done):
    for U in unique:
        input=input.replace("".join( [ U, U.upper() ]),"");
        input=input.replace("".join( [ U.upper(), U ]),"");
    # Check length, if stable exit reaction loop
    if len(input)==oldLen:
        done=True;
    else:
        oldLen=len(input);
# print length of fully reacted polymer        
print("Part A: Solution is {0:d}".format(len(input)));


# repeat process with pre-processing which removes one element
# track length to find shortest
lenList=list();
for poly in unique:
    # remove one element
    inmod=input.replace(poly,"").replace(poly.upper(),"");

    oldLen=-1;
    done=False;
    while(not done):
        for U in unique:
            inmod=inmod.replace("".join( [ U, U.upper() ]),"");
            inmod=inmod.replace("".join( [ U.upper(), U ]),"");
        if len(inmod)==oldLen:
            done=True;
        else:
            oldLen=len(inmod);
    lenList.append(oldLen);
    #print("  Removing {} yields {} length polymer".format(poly,oldLen));
print("Part B: Solution is {0:d}".format(min(lenList)));
	


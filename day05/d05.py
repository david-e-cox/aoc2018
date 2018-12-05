#!/usr/bin/python3

def react(polymer,elements):
    # Exit criteria
    oldLen=-1;
    done=False;
    # Eliminate aA,Aa,bB,Bb, etc until no further reductions exist
    while(not done):
        for E in elements:
            polymer=polymer.replace("".join( [ E, E.upper() ]),"");
            polymer=polymer.replace("".join( [ E.upper(), E ]),"");
        if len(polymer)==oldLen:
            done=True;
        else:
            oldLen=len(polymer);
    return oldLen;

# Input data
#input="dabAcCaCBAcCcaDA"
with open('input.txt') as f:
    input=f.read().rstrip('\n');

# Create set of unique elements in polymer
elements=set([c.lower() for c in input]);

# Print solution
print("Part A: Solution is {0:d}".format(react(input,elements)));


# repeat process with pre-processing which removes one element
# track length to find shortest resulting polymer
with open('input.txt') as f:
    input=f.read().rstrip('\n');

lenList=list();
for E in elements:
    # remove one element
    inmod=input.replace(E,"").replace(E.upper(),"");
    # react and store length
    lenList.append(react(inmod,elements));
    # progress print...
    print("  Removing {} yields {} length polymer".format(E,lenList[-1]));

#Print solution
print("Part B: Solution is {0:d}".format(min(lenList)));
	


#!/usr/bin/python3

# Create instruction set as dictionary of exec statements
opcode=dict();
opcode['addr'] = 'reg[A] + reg[B]'
opcode['addi'] = 'reg[A] + B'
opcode['mulr'] = 'reg[A] * reg[B]'
opcode['muli'] = 'reg[A] * B'
opcode['banr'] = 'reg[A] & reg[B]'
opcode['bani'] = 'reg[A] & B'
opcode['borr'] = 'reg[A] | reg[B]'
opcode['bori'] = 'reg[A] | B'
opcode['setr'] = 'reg[A]'
opcode['seti'] = 'A'
opcode['gtir'] = '1 if (A > reg[B])      else 0'
opcode['gtri'] = '1 if (reg[A] > B)      else 0'
opcode['gtrr'] = '1 if (reg[A] > reg[B]) else 0'
opcode['etir'] = '1 if (A == reg[B])      else 0'
opcode['etri'] = '1 if (reg[A] == B)      else 0'
opcode['etrr'] = '1 if (reg[A] == reg[B]) else 0'

# Function to find uniquely-mapped correct actions
def matchOp(works):
    dist=dict()
    for op in works.keys():
        dist[op]=sum([1 for i in works[op] if i>0])
        if dist[op]==1:
            nOp = works[op].index(max(works[op]))
            sOp = op;
            return sOp,nOp

        
# Read input file 1a
insList  =list();
regBefore=list();
regAfter =list();
    
with open('inputa.txt') as f:
    while(True):
        before=eval(f.readline().strip('\n').split(':')[1])
        insList.append(eval('['+f.readline().strip('\n').replace(' ',',')+']'))
        after=eval(f.readline().strip('\n').split(':')[1])
        regBefore.append(before)
        regAfter.append(after)
        if (not f.readline()):
            break

#Example        
#insList  =[[9,2,1,2]]
#regBefore=[[3,2,1,1]]
#regAfter= [[3,2,2,1]]

# Tally up total number of working codes for each I/O case
works=dict()
for op in opcode.keys():
    works[op]=[0]*16

worksCount=0
sampleCount=0
for i in range(0,len(insList)):
    # Create variables for eval()
    opN =insList[i][0];
    A =insList[i][1];
    B =insList[i][2];
    C =insList[i][3];
    for op in opcode.keys():
        # Set register to 'before' values
        reg=[r for r in regBefore[i]]
        # Run instruction
        reg[C]=eval(opcode[op])
        # Comare to 'after' values
        if reg == regAfter[i]:
            worksCount+=1
            works[op][opN]+=1;
            
    # if 3 or more opcodes could produce this sample I/O, increase sample count
    if worksCount>=3:
        sampleCount+=1

    # reset works counter to zero
    worksCount=0

print("Part A: Solution is {}".format(sampleCount))


map=['.']*16
for _ in range(0,len(opcode)):
    sOp,nOp=matchOp(works)
    # Assign string opcode into map at appropriate index
    map[nOp]=sOp
    # set works tally to zero in all op code cases, allows for
    # discovery of next unique mapping
    for op in works.keys():
        works[op][nOp]=0

# Read in part b        
insList.clear()
with open('inputb.txt') as f:
    for line in f:
        insList.append(eval('['+line.strip('\n').replace(' ',',')+']'))

# start with empty registers        
reg=[0]*4

for i in range(0,len(insList)):
    # Set registers
    opN =insList[i][0];
    A =insList[i][1];
    B =insList[i][2];
    C =insList[i][3];
    # Evaluate
    reg[C]=eval(opcode[map[opN]])

print("Part B: Solution is {}".format(reg[0]))







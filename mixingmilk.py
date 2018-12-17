inFile = open('mixmilk.in', 'r')
outFile = open('mixmilk.out', 'w')

cows = inFile.readlines()
purifiedcows = []

for cow in cows:
    cow = cow.strip('\n')
    purifiedcows.append(cow)

cowList1 = [cow.split(' ') for cow in purifiedcows]
cowList = []

for cow in cowList1:
    cow = [int(i) for i in cow]
    cowList.append(cow)

caps = [cowList[0][0], cowList[1][0], cowList[2][0]]

state = [cowList[0][1], cowList[1][1], cowList[2][1]]

allstates = []

FROM = 0
TO = 0

for i in range(100):
    FROM = i % 3
    TO = (FROM + 1) % 3
    
    if state[FROM] + state[TO] <= caps[TO]:
        state[TO] += state [FROM]
        state[FROM] = 0
        
    elif state[FROM] + state[TO] > caps[TO]:
        state[FROM] = state[FROM] - (caps[TO] - state[TO])
        state[TO] = caps[TO]
    
    print(state)
    allstates.append(state)
    

finalstate = allstates[99]

finalstate = [str(i) for i in finalstate]
for c in finalstate:
    outFile.write(c)
    outFile.write('\n')

outFile.close()

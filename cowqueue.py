inFile = open('cowqueue.in', 'r')
outFile = open('cowqueue.out', 'w')
info = inFile.readlines()
cows = [[int(c) for c in s.split()] for s in info[1::]]
cows = sorted(cows)

nexttime = 0
for cow in cows:
    nextentry = -1
    if cow[0] > nexttime:
        nexttime = cow[0] + cow[1]
    else:
        nexttime += cow[1]

outFile.write(str(nexttime))
outFile.write('\n')
outFile.close()

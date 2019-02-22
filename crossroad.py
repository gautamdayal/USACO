inFile = open('crossroad.in', 'r')
outFile = open('crossroad.out', 'w')
info = inFile.readlines()[1::]
crossings = [[int(c) for c in s.split()] for s in info]
cows = []
for x in crossings:
    if x[0] not in cows:
        cows.append(x[0])

crosscount = 0
for cow in cows:
    prevstate = None
    time = 0
    for crossing in crossings:
        ID = crossing[0]
        pos = crossing[1]
        if cow == ID:
            time += 1
            if time == 1:
                prevstate = pos
            else:
                if pos ^ prevstate:
                    crosscount += 1
                prevstate = pos

outFile.write(str(crosscount))
outFile.write('\n')
outFile.close()


inFile = open('square.in', 'r')
outFile = open('square.out', 'w')

sqs = inFile.readlines()

sq1 = [int(c) for c in sqs[0].split()]
sq2 = [int(c) for c in sqs[1].split()]

xvals = [sq1[0], sq1[2], sq2[0], sq2[2]]
yvals = [sq1[1], sq1[3], sq2[1], sq2[3]]
x = max(xvals)-min(xvals)
y = max(yvals)-min(yvals)


print(max([x, y]) ** 2)
outFile.write(str(max([x, y]) ** 2))
outFile.write('\n')
outFile.close()

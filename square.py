# All test cases correct.

# Have written functions for min and max instead of using builtin.
def maximum(L):
    currentmax = 0
    for n in L:
        if n > currentmax:
            currentmax = n
    return currentmax

def minimum(L):
    currentmin = 11
    for n in L:
        if n < currentmin:
            currentmin = n
    return currentmin

inFile = open('square.in', 'r')
outFile = open('square.out', 'w')

sqs = inFile.readlines()

sq1 = [int(c) for c in sqs[0].split()]
sq2 = [int(c) for c in sqs[1].split()]

xvals = [sq1[0], sq1[2], sq2[0], sq2[2]]
yvals = [sq1[1], sq1[3], sq2[1], sq2[3]]

x = maximum(xvals)-minimum(xvals)
y = maximum(yvals)-minimum(yvals)

outFile.write(str(maximum([x, y]) ** 2))
outFile.write('\n')
outFile.close()

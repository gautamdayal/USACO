# All test cases correct.

"""
PROB: sleepy
LANG: PYTHON3
ID: gautam.8
"""
inFile = open('sleepy.in', 'r')
outFile = open('sleepy.out', 'w')

clist = inFile.readlines()[1]
cows = [int(i) for i in clist.split()]

def rightMostSort(line):
    i = len(line) - 1
    suffLength = 1
    while 1:
        
        if line[i] < line[i - 1]:
            break
        elif i == 0:
            break
        else:
            suffLength += 1
        i -= 1
    return len(line) - suffLength

outFile.write(str(rightMostSort(cows)))
outFile.write('\n')

outFile.close()

inFile = open('billboard.in', 'r')
outFile = open('billboard.out', 'w')
info = inFile.readlines()
mowin = info[0]
cowin = info[1]

mower = [int(c) for c in mowin.split()]
cow = [int(c) for c in cowin.split()]

x1, y1, x2, y2 = mower[0], mower[1], mower[2], mower[3]
x3, y3, x4, y4 = cow[0], cow[1], cow[2], cow[3]

def isHidden(point):
    x = point[0]
    y = point[1]
    x1, y1 = cow[0], cow[1]
    x2, y2 = cow[2], cow[3]
    
    if y >= y1 and y <= y2 and x >= x1 and x <= x2:
        return True
    else:
        return False

hiddenCount = 0
if isHidden([x1, y1]):
    hiddenCount += 1
    
if isHidden([x1, y2]):
    hiddenCount += 1
    
if isHidden([x2, y1]):
    hiddenCount += 1
    
if isHidden([x2, y2]):
    hiddenCount += 1
    
output = None
if hiddenCount == 4:
    output = 0

elif hiddenCount == 1 or hiddenCount == 0:
    output = (x2 - x1) * (y2 - y1)

else:
    xb = max([x1, x3])
    yb = max([y1, y3])
    xt = min([x2, x4])
    yt = min([y2, y4])
    
    output = (x2-x1) * (y2-y1) - (xt-xb) * (yt-yb)

outFile.write(str(output))
outFile.write('\n')

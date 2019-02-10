# All test cases correct.

inFile = open('notlast.in', 'r')
outFile = open('notlast.out', 'w')

cows = [s.split() for s in inFile.readlines()[1::]]
for l in cows:
    l[1] = int(l[1])

totalmilk = {}

for cow in cows:
    name = cow[0]
    amount = cow[1]
    if name not in totalmilk:
        totalmilk[name] = 0
        
    totalmilk[name] += amount
    
amounts = list(totalmilk.values())
sortedamounts = []
while len(amounts) > 0:
    sortedamounts.append(min(amounts))
    amounts.remove(min(amounts))

second = 0
secondname = ''
minimum = sortedamounts[0]
for n in sortedamounts[1::]:
    if n > minimum:
        second = n
        break

count = 0
for n in sortedamounts[1::]:
    if n == second:
        count += 1

for cow in totalmilk:
    if totalmilk[cow] == second:
        secondname = cow

if len(cows) == 1:
    outFile.write(cows[0][0])
else:
    
    if count == 1:
        outFile.write(secondname)
    else:
        outFile.write('Tie')
outFile.write('\n')
outFile.close()

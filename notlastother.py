inFile = open('notlast.in', 'r')
outFile = open('notlast.out', 'w')

cows = [s.split() for s in inFile.readlines()[1::]]
print(cows)
for l in cows:
    l[1] = int(l[1])

totalmilk = {}

for cow in cows:
    name = cow[0]
    amount = cow[1]
    if name not in totalmilk:
        totalmilk[name] = 0
        
    totalmilk[name] += amount

done = False
if len(totalmilk) == 1:
    done = True
    outFile.write(list(totalmilk.keys())[0])
    print(list(totalmilk.keys())[0])
    outFile.write('\n')
    outFile.close()

if not done:
    amounts = list(totalmilk.values())
    if len(totalmilk) < 7:
        lowest = 0
    else:
        lowest = amounts[0]
    second = 10000
    
    for amount in amounts[1::]:
    
        if amount == lowest:
            continue
            
        elif amount < lowest:
            second = lowest
            lowest = amount  
        
        elif amount < second:
            second = amount
        
    secondCow = ''
    count = 0
    for cow in totalmilk:
        if totalmilk[cow] == second:
            secondCow = cow
            count += 1
    
    if count > 1 or second == 10000:
        print('Tie')
        outFile.write('Tie')
    else:
        print(secondCow)
        outFile.write(secondCow)
    
    outFile.write('\n')
    outFile.close()

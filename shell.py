# All test cases correct.

"""
PROB: shell
LANG: PYTHON3
ID: gautamdayal
"""

inFile = open('shell.in', 'r')
outFile = open('shell.out', 'w')
inList = inFile.readlines()[1::]

moves = [[int(c) for c in string.split()] for string in inList]
scores = []

for position in range(3):
    shells = ['O', 'O', 'O']
    shells[position] = 'X'
    score = 0
    
    for move in moves:
        a = move[0]
        b = move[1]
        guess = move[2]
        tempA = shells[a-1]
        shells[a-1] = shells[b-1]
        shells[b-1] = tempA
        
        if shells[guess-1] == 'X':
            score += 1
            
    scores.append(score)

outFile.write(str(max(scores)))
outFile.write('\n')
outFile.close()

import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
Given a sequence, calculate the point of it
points = # of continuous 'O' in a sequence


'''

def calcPointOfSeq(seq): # seq: a string input
    point = 0
    combo = 0
    for answer in seq:
        if answer=='O':
            combo += 1
            point += combo
        elif answer == 'X':
            combo = 0 # reset
        else:
            print("ERROR: Invalid input!\n")
    return point

# get the sequences
numberOfSeq = int(input().replace('\n', ''))
listOfSeq = []
pointsOfSeq = []
for i in range(numberOfSeq):
    seq = input().replace('\n', '')
    listOfSeq.append(seq)

# analyze each sequence & append final score
for seq in listOfSeq:
    point = calcPointOfSeq(seq)
    pointsOfSeq.append(point)

# print points
for i in range(len(pointsOfSeq)):
    print("%d\n"%pointsOfSeq[i]) # print int with newline












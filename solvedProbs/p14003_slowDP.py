import sys
input = sys.stdin.readline

'''
longest increasing partial sequence

print length of partial seq
and a candidate of such sequence

Using DP
keep track of: the last element index of max length partial sequence
DP[i] = [max length upto ith partial sequence including itself, previous index of such partial sequence]
if there is no prior one, put -1 instead

'''

n = int(input())
sequence = list(map(int, input().split(' ')))

DP = []
maxIdx = 0

# first element
DP = [(1,-1)]

def printDP():
    for i in range(len(DP)):
        maxlenForIdx, prev = DP[i]
        if prev == -1:
            print(i, 'th: ',sequence[i],' len', maxlenForIdx, 'prev num None')
        else:
            print(i,'th: ',sequence[i],' len', maxlenForIdx,'prev num ', sequence[prev])

curIdx = 1
while curIdx < len(sequence):
    # append curIdx th element into DP table
    maxlen = 0
    maxPrevIdx = -1
    for i in range(len(DP)): # 이게 O(n)
        dpLen, prevIdx = DP[i]
        if sequence[i] < sequence[curIdx]: # current num is larger => can be added to
            if (dpLen > maxlen): # if it becomes larger
                maxlen = dpLen
                maxPrevIdx = i
    newDPLen = maxlen + 1
    DP.append((newDPLen, maxPrevIdx))
    if newDPLen > DP[maxIdx][0]:
        maxIdx = curIdx
    curIdx += 1

# print max length
# partial sequence
maxLength, prevIdx = DP[maxIdx]
pSeq = [sequence[maxIdx]]
while prevIdx >= 0:
    pSeq.append(sequence[prevIdx])
    _, prevIdx = DP[prevIdx]

# printDP()

pSeq.reverse()
print(maxLength)
print(' '.join(map(str, pSeq)) )












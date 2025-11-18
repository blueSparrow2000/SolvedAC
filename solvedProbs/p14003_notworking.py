import sys
input = sys.stdin.readline

'''
longest increasing partial sequence

print length of partial seq
and a candidate of such sequence
'''

n = int(input())
sequence = list(map(int, input().split(' ')))

partialSeq = []
curIdx = 0

while curIdx < len(sequence):
    curNum = sequence[curIdx]
    incrementablePSeq = [] # curNum을 맨 끝에 추가할 수 있는 녀석들 index

    for p in range(len(partialSeq)):
        pSeq = partialSeq[p]
        if pSeq[-1] < curNum:
            incrementablePSeq.append(p)

    if len(incrementablePSeq) == 1: # 한 곳에만 추가 가능할때
        partialSeq[incrementablePSeq[0]].append(curNum)
    elif len(incrementablePSeq) >= 2: # 여러개
        maxLen = max([len(partialSeq[l]) for l in incrementablePSeq])
        maxFound = False

        for j in range(len(incrementablePSeq)-1,-1,-1): # range(len(incrementablePSeq) ,-1,-1)
            if not maxFound and len(partialSeq[incrementablePSeq[j]]) == maxLen: # first max encountered
                maxFound = True
                partialSeq[incrementablePSeq[j]].append(curNum)
            else:
                del partialSeq[incrementablePSeq[j]]
    elif len(incrementablePSeq) == 0:
        if len(partialSeq) == 0: # 처음일때
            partialSeq.append([curNum])
        else: # 기존 pseq중 제일 길이가 긴 놈에게 붙임
            maxSubSeq = []
            maxSubLen = 0

            for pseq in partialSeq:
                subLen = 0
                subSeq = []
                for k in range(len(pseq)):
                    if pseq[k] < curNum:
                        subLen += 1
                    else:
                        break
                subSeq = pseq[:subLen]
                if maxSubLen < subLen:
                    maxSubLen = subLen
                    maxSubSeq = subSeq
            partialSeq.append(maxSubSeq + [curNum])

    curIdx += 1

maxLen = max(list(map(len, partialSeq)))
print(maxLen)

for pseq in partialSeq:
    if len(pseq) == maxLen:
        print(' '.join(map(str, pseq)))
        break














import sys
input = sys.stdin.readline

'''
longest increasing partial sequence

print length of partial seq
and a candidate of such sequence

# replace를 생각못했네

lis = [ (number, sequence에서 해당 숫자가 있는 index)  ... ] 
tracker의 index == sequence의 index
tracker = [ partial sequence에서 해당 index에 위치한 sequence[index] 숫자의 previous number가 있는 index ... ] 
back tracking할때 tracker에서 partial sequence의 앞 숫자들을 구할것

6
10 20 10 30 20 50
>>
4
10 20 30 50


9
3 9 3 9 12 3 9 17 9
>>
4
3 9 12 17

7
-38 -86 8 8 -86 -38 1
>>
3
-86 -38 1 

9
24 41 58 2 40 25 24 30 34


'''

n = int(input())
sequence = list(map(int, input().split(' ')))

lis = []
tracker = []

def binarySearch(low, high, target):
    global lis
    if low > high:
        return low
    mid = low + (high - low) // 2
    if lis[mid][0] == target:
        return mid
    elif lis[mid][0] < target:
        return binarySearch(mid +1,high, target)
    else:
        return binarySearch(low,mid-1, target)


# 처음 꺼 미리 tracker랑 lis에 넣고 시작하자
lis.append((sequence[0], 0))
tracker.append(-1)

for i in range(1,len(sequence)):
    curNum =  sequence[i]
    # print(lis)
    if lis[-1][0] < curNum: # higher => add to lis
        tracker.append(lis[-1][1])
        lis.append((curNum, i))  # number랑 해당 숫자가 있는 idx
    else: # replace
        replaceIdx = binarySearch(0,len(lis)-1, curNum)
        # print(replaceIdx)
        if replaceIdx == 0:
            tracker.append(-1)
        else:
            tracker.append(lis[replaceIdx-1][1]) #lis[-1][1]
        lis[replaceIdx] = (curNum, i)

# print(tracker)

# print max length & partial sequence
print(len(lis))

pSeq = []
num, prevIdx = lis.pop()
while prevIdx >= 0:
    pSeq.append(sequence[prevIdx])
    prevIdx = tracker[prevIdx]

pSeq.reverse()
print(' '.join(map(str, pSeq)) )












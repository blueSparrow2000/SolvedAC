import sys
input = sys.stdin.readline

'''
break n place
3 1 10
194
5
26

>> 357 78
level 78에 357시간 소요

1 3 1
0 2 5

>> 8 2
'''

n,m,availableBlocks = map(int, input().split(' '))
ground = [] # we only need height information, since we don't use 2D spacial information

for i in range(n):
    ground += list(map(int, input().split(' ')))

ground.sort()
# print(ground)

def equiHeightLeftIndex(start, height):
    global ground
    while start < m*n and ground[start] <= height: # input is given so that this is always true for at least once
        start += 1
    if start < m*n and ground[start] > height: # if the next block is higher than the current filled height (from the left side)
        return start - 1
    return start

def equiHeightRightIndex(start, height):
    global ground
    while start >= 0 and ground[start] >= height: # input is given so that this is always true for at least once
        start -= 1
    if start >= 0 and ground[start] < height: # if the next block is higher than the current filled height (from the left side)
        return start + 1
    return start

# index where flattening is complete
minHeight = ground[0]
minIdx = equiHeightLeftIndex(0,minHeight)
maxHeight = ground[m*n-1]
maxIdx = equiHeightRightIndex(m*n-1, maxHeight)

totalCost = 0
while minHeight != maxHeight and minIdx < maxIdx: # until they meet
    # print("Before: minH %d / maxH %d"%(minHeight, maxHeight))
    placeCost = minIdx + 1
    breakCost = m*n - maxIdx
    if placeCost > 2*breakCost or availableBlocks < placeCost: # if breaking takes less time OR not enough blocks in inventory
        # break
        # print('breaked ', breakCost)
        totalCost += 2*breakCost
        maxHeight -= 1
        maxIdx = equiHeightRightIndex(maxIdx, maxHeight)
        availableBlocks += breakCost # blocks removed
        # print('maxIdx ', maxIdx)
    else:
        # place
        # print('placed ', placeCost)
        totalCost += placeCost
        minHeight += 1
        minIdx = equiHeightLeftIndex(minIdx, minHeight)
        availableBlocks -= placeCost
        # print('minIdx ', minIdx)

print("%d %d"%(totalCost, maxHeight ))

















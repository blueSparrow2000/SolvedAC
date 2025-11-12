import sys
input = sys.stdin.readline

'''
Histogram area

number of histograms
1 <= n
histogram height
0 <= h_i

heights: (height, first index where such height starts)
it contains limsup-like height list (max heights upto index)

test case:
3 1 3 2 
0
>> 4

11 0 1 7 2 0 3 6 3 3 1 0
0
>> 12
'''
debug = False


# each test case is a line
while True:
    data = input().split(' ')
    n = int(data[0])
    if n == 0: # end
        break
    histograms = list(map(int, data[1:]))
    heights = []

    maxArea = 0
    curhistIdx = 0
    while curhistIdx < len(histograms):
        if not heights: # if height list is empty (in increasing order)
            if histograms[curhistIdx] > 0:
                heights.append((histograms[curhistIdx],curhistIdx))
                if debug: print('filled heights')
            curhistIdx += 1
            continue
        if debug: print("heights: ", heights)

        currentHeight = histograms[curhistIdx]
        prevMax = heights[-1][0]
        if prevMax < currentHeight: # if higher histogram encountered
            heights.append((currentHeight, curhistIdx))
            if debug: print('higher encountered: prev ', prevMax, ' / current ',currentHeight)
        elif prevMax == currentHeight: # if same to prev height => skip
            if debug: print('same level')
            pass
        else:
            firstLevelLayerIdx = curhistIdx
            while heights and (heights[-1][0] > currentHeight): # while current height is strictly smaller
                h,idx = heights.pop()
                firstLevelLayerIdx = idx
                if debug: print('popped ', h, 'on',idx)
                area = h*( (curhistIdx - 1) - idx + 1)
                if area > maxArea: maxArea = area
                if debug: print('max updated: ', maxArea)
            heights.append((currentHeight, firstLevelLayerIdx))
        curhistIdx += 1

    # if we have seen all histograms, do a final pass with current height 0, index is n-1 where n is initial height number
    if debug: print('final heights: ', heights)
    while heights and heights[-1][0] > 0:
        h, idx = heights.pop()
        if debug: print('popped ', h,'on', idx)
        area = h * ((n - 1) - idx + 1)
        if area > maxArea: maxArea = area
        if debug: print('max updated: ', maxArea)

    print(maxArea)


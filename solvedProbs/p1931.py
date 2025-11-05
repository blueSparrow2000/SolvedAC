import sys
input = sys.stdin.readline

'''
# scheduling
'''
# get number of intervals
n = int(input().strip())

intervals = [] # list of [start, end]
# get intervals
for i in range(n):
    intervals.append(list(map(int, input().strip().split(' '))))

# sort by starting time
intervals.sort() # key = lambda x:(x[0],x[1])

totalNumber = 0
cur = 0
while cur < n: # until it reaches end of the list of intervals
    totalNumber += 1
    currentInterval = intervals[cur]
    next = cur + 1
    while next < n:
        nextInterval = intervals[next]
        # if next interval has no common piece, break the loop (we saw all that is needed)
        if nextInterval[0] >= currentInterval[1]: # next interval's start is passed current interval's end
            break
        # change the current interval if it is inside current one
        if nextInterval[1] <= currentInterval[1]:
            cur = next # skip to next one
            currentInterval = intervals[cur] # update current interval
        next += 1

    # if next one exists, use it as current one on the next loop
    if next < n:
        cur = next
    else:
        break
print(totalNumber)

# for debugging
'''
import sys
input = sys.stdin.readline

DEBUG = False

# get number of intervals
n = int(input().strip())

intervals = [] # list of [start, end]
# get intervals
for i in range(n):
    intervals.append(list(map(int, input().strip().split(' '))))

# sort by starting time
intervals.sort() # key = lambda x:(x[0],x[1])

totalNumber = 0
cur = 0
while cur < n: # until it reaches end of the list of intervals
    totalNumber += 1
    currentInterval = intervals[cur]
    next = cur + 1
    if DEBUG: print("Added 1 | cur: [{},{}]".format(currentInterval[0],currentInterval[1]))

    while next < n:
        nextInterval = intervals[next]
        if DEBUG: print("next: [{},{}]".format(nextInterval[0],nextInterval[1]))

        # if next interval has no common piece, break the loop (we saw all that is needed)
        if nextInterval[0] >= currentInterval[1]: # next interval's start is passed current interval's end
            break
        # change the current interval if it is inside current one
        if nextInterval[1] <= currentInterval[1]:
            cur = next # skip to next one
            currentInterval = intervals[cur] # update current interval
            if DEBUG: print("Changed | cur: [{},{}]".format(currentInterval[0], currentInterval[1]))
        next += 1

    # if next one exists, use it as current one on the next loop
    if next < n:
        cur = next
        if DEBUG: print("Done | cur: [{},{}]".format(intervals[cur][0], intervals[cur][1]))
    else:
        break


print(totalNumber)

'''
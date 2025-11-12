import sys
from queue import PriorityQueue
# 되는 코드. 구현은 비슷한데 뭐가 차이인지 모르겠다

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    Q = int(input())

    min_pq = PriorityQueue()
    max_pq = PriorityQueue()
    count = {}

    for _ in range(Q):
        t, v = input().split()
        v = int(v)

        if t == 'I':
            min_pq.put(v)
            max_pq.put(-v)
            if v not in count:
                count[v] = 0
            count[v] += 1
        if t == 'D':
            if v == 1:
                while max_pq.qsize() != 0:
                    x = -max_pq.get()
                    if count[x] != 0:
                        count[x] -= 1
                        break
            if v == -1:
                while min_pq.qsize() != 0:
                    x = min_pq.get()
                    if count[x] != 0:
                        count[x] -= 1
                        break
    max_val = -1e12
    min_val = 1e12

    while max_pq.qsize() != 0:
        x = -max_pq.get()
        if count[x] != 0:
            max_val = x
            break

    while min_pq.qsize() != 0:
        x = min_pq.get()
        if count[x] != 0:
            min_val = x
            break

    if max_val == -1e12:
        print("EMPTY")
    else:
        print(max_val, min_val)


############# TIMEOUT ###################

# import sys
# import heapq
# input = sys.stdin.readline
#
# '''
# priority queue
#
# keep track of deleted numbers
# and do garbage collection-like operation when popping maxima & minima
#
# for duplicate numbers, it is only stored once in the heap
# '''
#
# num_tracker = dict() # tracts number of given numbers
# minHeap, maxHeap = [], []
# # use 'not minHeap' to check empty (safe)
#
# def isEmpty(tracker):
#     # check whether tracker is empty or not
#     isEmpty = True
#     for k in tracker.keys():
#         if tracker[k] >0 :
#             isEmpty = False
#             break
#     return isEmpty
#
# def safePush(item):
#     if item in num_tracker: # item already inside -> only increment tracker
#         num_tracker[item] += 1
#     else: # first time insert
#         num_tracker[item] = 1
#         heapq.heappush(minHeap, item)
#         heapq.heappush(maxHeap, -item)
#
# def popMax():
#     if isEmpty(num_tracker): # when tracker is empty, it means no data
#         return
#     # do garbage collection - remove deleted values now
#     while (-maxHeap[0] not in num_tracker) or num_tracker[-maxHeap[0]] <= 0:
#         poppedMax = -heapq.heappop(maxHeap)
#         if poppedMax in num_tracker:
#             del num_tracker[poppedMax]
#     # after garbage collection
#     poppedMax = -maxHeap[0]
#     num_tracker[poppedMax] -= 1
#
#     # print("popmax: ", poppedMax)
#     #
#     # minHeap.remove(poppedMax) # O(n)
#     # heapq.heapify(minHeap) # O(n) but faster since it is already ordered
#     return
#
# def popMin():
#     if isEmpty(num_tracker): # when tracker is empty, it means no data
#         return
#     while (minHeap[0] not in num_tracker) or num_tracker[minHeap[0]] <= 0:
#         poppedMin = heapq.heappop(minHeap)
#         if poppedMin in num_tracker:
#             del num_tracker[poppedMin]
#     # after garbage collection
#     poppedMin = minHeap[0]
#     num_tracker[poppedMin] -= 1
#
#     # print("popmin: ", poppedMin)
#     # maxHeap.remove(-poppedMin)
#     # heapq.heapify(maxHeap)
#     return
#
# def printMaxMin():
#     if isEmpty(num_tracker): # empty
#         print('EMPTY')
#         return
#
#     while (-maxHeap[0] not in num_tracker) or num_tracker[-maxHeap[0]] <= 0:
#         poppedMax = -heapq.heappop(maxHeap)
#         if poppedMax in num_tracker:
#             del num_tracker[poppedMax]
#     maxVal =  -maxHeap[0]
#
#     while (minHeap[0] not in num_tracker) or num_tracker[minHeap[0]] <= 0:
#         poppedMin = heapq.heappop(minHeap)
#         if poppedMin in num_tracker:
#             del num_tracker[poppedMin]
#     minVal = minHeap[0]
#
#     print("%d %d"%(maxVal, minVal))
#
# # 'EMPTY'
# T = int(input())
# for t in range(T):
#     num_tracker = dict()
#     minHeap, maxHeap = [], [] # reset heap
#     n = int(input())
#     for k in range(n):
#         op, num = input().strip().split(' ')
#
#         num = int(num)
#         if op == 'I':
#             safePush(num)
#         else: # op is 'D'
#             if num == 1: # delete max
#                 popMax()
#             else: # delete min
#                 popMin()
#         # print('%s %d'%(op, num))
#         # print(num_tracker)
#         # print(maxHeap)
#         # print(minHeap)
#
#     printMaxMin()
#
#
#
#
#
#

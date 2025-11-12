import sys
input = sys.stdin.readline

'''
abs heap
empty => return 0 / no 0 value
root: smallest abs value
tie break: - value (smaller one)

heap start with index 1
parent of ith node) i//2
child of ith node) left: 2i, right: 2i+1
'''

# abs heap - start with index 0
heap = [0]

def shiftUp(i):

    # get parent
    parent = i//2
    # print('current: ', i, '| parent: ', parent)
    if parent ==0: return # no parent => reached root

    # checks
    if abs(heap[i]) < abs(heap[parent]) or (abs(heap[i]) == abs(heap[parent]) and (heap[i] < heap[parent])):
        # change
        # print('change!')
        heap[i], heap[parent] = heap[parent], heap[i]
        return shiftUp(parent)

    return

# insert
def insert(node):
    heap.append(node) # append at last pos
    idx = len(heap) - 1
    shiftUp(idx)


# current parent node index i
def shiftDown(i):
    # among childs, find smaller one
    # print(i)
    # # if i> 100:
    # #     return
    leftChild = 2 * i
    rightChild = 2 * i + 1
    smallerChild = leftChild
    if leftChild < len(heap): # left child exist
        if rightChild >= len(heap):  # right child do not exist
            smallerChild = leftChild
        # compare left and right childs and get smaller one
        elif abs(heap[rightChild]) < abs(heap[smallerChild]) or (abs(heap[rightChild]) == abs(heap[smallerChild]) and ( heap[rightChild] < heap[smallerChild] ) ):
            smallerChild = rightChild

        # if current ith node is larger than the child, swap and shift down
        if abs(heap[i]) > abs(heap[smallerChild]) or (abs(heap[i]) == abs(heap[smallerChild]) and ( heap[i] > heap[smallerChild] ) ):
            heap[i], heap[smallerChild] = heap[smallerChild], heap[i]
            return shiftDown(smallerChild)
    return

# remove root and return
# if empty, return 0
def remove():
    if len(heap) == 1: # empty check
        return 0
    if len(heap) == 2:  # only root exists
        return heap.pop()

    # shift down operation
    root = heap[1]
    heap[1] = heap.pop()  # get the last elem to root
    shiftDown(1)
    return root

N = int(input())
for n in range(N):
    op = int(input())

    if op == 0: # pop the root (print and remove) - consider tie breaking - whether there is same abs value => choose the smallest
        # print the result right away
        # print("Before: ", heap)
        print(remove())
        # print("Removed: ",heap)

    else: # push
        # print("Before: ", heap)
        insert(op)
        # print("After: ",heap)





















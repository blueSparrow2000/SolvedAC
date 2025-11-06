import sys
from collections import deque
input = sys.stdin.readline

'''
Riping tomato in a box

queue: separator( | ) separates riped tomatoes of today and next day
day 0 tomato
0 0 | 
day 1 tomato
0 | 1 1 
| 1 1 1 1 
day 2 tomato
1 1 1 1 |
1 1 1 | 2 2 2
...
'''

ylen, xlen = map(int, input().split(' '))
board = [] # 2D list
nearBy = ((1,0),(-1,0),(0,1),(0,-1))

# fill the board
for i in range(xlen):
    board.append(list(map(int, input().split(' '))))

def simulate():
    global xlen, ylen, board
    queue = deque([])  # we will use (-1,-1) as a separator
    dayCount = 0

    # enqueue the already riped tomato
    for x in range(xlen):
        for y in range(ylen):
            if board[x][y] == 1:
                queue.append((x,y))
    queue.append((-1, -1))  # add the initial separator

    separatorReached = False
    while True: # while not empty
        x,y = queue.popleft()
        if x==-1 and y== -1: # if separator encountered
            if separatorReached: # the separator was already encountered in the previous loop
                break # get out of the loop
            dayCount += 1
            queue.append((-1, -1)) # append another separator on the back
            separatorReached = True
            continue
        elif separatorReached: # if it is not separator and previous queue was separator, reset separator counter
            separatorReached = False

        # investigate nearby up, down, left, right nodes
        for dx,dy in nearBy:
            xNear, yNear = x+dx, y+dy
            if (0 <= xNear<xlen) and (0 <= yNear<ylen) and (board[xNear][yNear]==0): # propagate only if it is immature tomato
                queue.append((xNear, yNear))
                board[xNear][yNear] = 1 # change to riped

    # check unreachable node
    for row in board:
        if 0 in row:
            return -1 # if there is a tomato that cannot be riped,
    return dayCount - 1 # we always count one more day because we check separator once more right before queue is empty(all riping done)

ripeResult = simulate()
print("%d"%(ripeResult))





















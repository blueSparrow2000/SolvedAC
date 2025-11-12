import sys
from collections import deque
input = sys.stdin.readline

'''
shortest path (bfs?)
2 <= n,m <= 1000
2: target (only one!)
1: available
0: non available
-1: unreachable
    
use BFS propagation like 'tomato(p7576)' problem

# -1 : not visited / wall: 0 /
# -1일때만 좌표에 방문하고, 거리 +1을 해서 저장한다
# 시작점과 벽만 0으로 초기화하고 시작노드를 넣는다
'''

def printMat(mat, n):
    for i in range(n):
        print(' '.join(map(str, mat[i])))

n,m = map(int, input().split(' '))
board = [] # we only need height information, since we don't use 2D spacial information
nearBy = ((1,0),(-1,0),(0,1),(0,-1))

# fill the board
for i in range(n):
    board.append(list(map(int, input().split(' '))))
result = [[-1] * m for i in range(n)]

queue = deque([])  # we will use (-2,-2) as a separator
distance = 1 # bfs depth

for x in range(n):
    for y in range(m):
        if board[x][y] == 2: # target
            queue.append((x,y))
            result[x][y] = 0
        elif board[x][y] == 0: # wall
            result[x][y] = 0
queue.append((-2, -2)) # add the initial separator

separatorReached = False
while True: # while not empty
    x,y = queue.popleft()
    if x==-2 or y== -2: # if separator encountered
        if separatorReached: # the separator encountered second consecutive time => END
            break
        # separator encountered for the first time => bfs depth += 1
        distance += 1
        queue.append((-2, -2)) # append another separator on the back
        separatorReached = True
        continue
    elif separatorReached: # if it is not separator and previous queue was separator, reset separator counter (there is more element in queue)
        separatorReached = False

    # investigate nearby up, down, left, right nodes
    for dx,dy in nearBy:
        xNear, yNear = x+dx, y+dy
        if (0 <= xNear<n) and (0 <= yNear<m) and (board[xNear][yNear]==1) and result[xNear][yNear]==-1: # propagate only if it is visitable and unvisited node
            queue.append((xNear, yNear))
            result[xNear][yNear] = distance # update distance

printMat(result, n)











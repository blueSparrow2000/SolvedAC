import sys
from collections import deque
input = sys.stdin.readline

'''
Maze routing
n by m grid
both at least 2
start from 0,0 to n-1,m-1
find least cost path length

=> BFS

1: can be visited => count # of 1's in the way
0: blocked
'''

nearBy = ((1,0),(-1,0),(0,1),(0,-1))

n,m = map(int, input().split(' '))
maze = []
visited = [[-1]*m for i in range(n)]

for i in range(n):
    row = list(map(lambda x: int(x), input().strip()))
    maze.append(row)

# print(maze)

queue = deque([(0,0,1)])
while queue:
    x,y,distance = queue.popleft()
    nextDistance = distance+1
    # investigate nearby up, down, left, right nodes
    for dx,dy in nearBy:
        xNear, yNear = x+dx, y+dy
        # print(xNear, yNear)
        if (xNear == n-1 and yNear == m-1): # arrived on destination
            print(nextDistance)
            queue = deque([]) # emptify
            break
        elif (0 <= xNear<n) and (0 <= yNear<m) and (maze[xNear][yNear]==1) and visited[xNear][yNear]==-1: # propagate only if it is visitable and unvisited node
            queue.append((xNear, yNear,nextDistance))
            visited[xNear][yNear] = nextDistance # update distance

import sys
input = sys.stdin.readline

'''
color blind
- 2d array에서 connect된 덩어리의 개수를 세기
'''
# debug = False

length = int(input())
board = [] # 2D list

# fill the board
for i in range(length):
    board.append(list(input().strip()))


# def printMat(mat):
#     for row in mat:
#         row = ['o' if x else 'x' for x in row]
#         print(''.join(row))

def countMass():
    global length, board
    visited = [[False] * length for i in range(length)]
    queue = []  #
    connectedMassCount = 0
    visitX = 0
    visitY = 0

    while visitX < length: # we see untill board runs out spaces
        if visited[visitX][visitY]: # already visited
            visitY += 1 # search next one
            if visitY == length:
                visitY = 0
                visitX += 1
            continue
        # do until we find unvisited
        pattern = board[visitX][visitY] # get pattern to search for connectivity: R,G,B
        # if debug: print("Pivot: ",visitX, visitY)

        # put the seed to the queue
        queue.append((visitX,visitY))
        visited[visitX][visitY] = True
        connectedMassCount += 1
        while queue: # while not empty
            # dfs (if used queue.pop(0) => bfs)
            x,y = queue.pop()

            # investigate nearby up, down, left, right nodes
            # if there is unvisited connected pattern, append to queue
            if (x > 0) and (not visited[x-1][y]) and (board[x-1][y] == pattern):
                visited[x - 1][y] = True
                queue.append((x-1,y))
            if (x < length - 1) and (not visited[x+1][y]) and (board[x+1][y] == pattern):
                visited[x+1][y] = True
                queue.append((x+1,y))
            if (y > 0) and (not visited[x][y-1]) and (board[x][y-1] == pattern):
                visited[x][y-1] = True
                queue.append((x,y-1))
            if (y < length - 1) and (not visited[x][y + 1]) and (board[x][y + 1] == pattern):
                visited[x][y + 1] = True
                queue.append((x, y + 1))

        # if debug: printMat(visited)
    return connectedMassCount


withoutColorBlind = countMass()
# make board colorblind
board = [ ['R' if e=='G' else e for e in row] for row in board]

# for row in board:
#     print(''.join(row))

withColorBlind = countMass()
print("%d %d"%(withoutColorBlind,withColorBlind))








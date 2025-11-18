import sys
input = sys.stdin.readline

'''
Housing complex
'''

length = int(input())
board = []

for i in range(length):
    row = list(map(lambda x: int(x), input().strip()))
    board.append(row)

# def printMat(mat):
#     for row in mat:
#         row = ['o' if x else 'x' for x in row]
#         print(''.join(row))

def countMass():
    global length, board
    # mark already visited if it is a wall
    visited = [[False if board[i][j] else True for j in range(length)] for i in range(length)]
    # printMat(visited)
    queue = []  #
    connectedMassCount = 0
    massWeights = []
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

        # put the seed to the queue
        queue.append((visitX,visitY))
        visited[visitX][visitY] = True
        connectedMassCount += 1
        weight = 0
        while queue: # while not empty
            # dfs (if used queue.pop(0) => bfs)
            x,y = queue.pop()
            weight += 1

            # investigate nearby up, down, left, right nodes
            # if there is unvisited connected pattern, append to queue
            if (x > 0) and (not visited[x-1][y]) and (board[x-1][y]):
                visited[x - 1][y] = True
                queue.append((x-1,y))
            if (x < length - 1) and (not visited[x+1][y]) and (board[x+1][y]):
                visited[x+1][y] = True
                queue.append((x+1,y))
            if (y > 0) and (not visited[x][y-1]) and (board[x][y-1]):
                visited[x][y-1] = True
                queue.append((x,y-1))
            if (y < length - 1) and (not visited[x][y + 1]) and (board[x][y + 1]):
                visited[x][y + 1] = True
                queue.append((x, y + 1))

        massWeights.append(weight)
        # if debug: printMat(visited)
    return connectedMassCount, massWeights

numOfEstates, housesPerEstate = countMass()
print(numOfEstates)
housesPerEstate.sort()
for houses in housesPerEstate:
    print(houses)






















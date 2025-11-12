import sys
input = sys.stdin.readline

'''
# find max sum of tetromino positions
4 4
5 5 2 3
1 6 9 7
6 1 8 6
8 7 8 8

>> 33
'''

m,n = map(int, input().split(' '))
board = []
for i in range(m):
    row = list(map(int, input().split(' ')))
    board.append(row)

# tetroRectDict = {
#     '2b2': (2,2),
#     'hori': (1,4),
#     'verti': (4,1),
#     'capHori': (2,3),
#     'capVerti': (3,2),
#     'LHori': (2,3),
#     'LVerti': (3,2),
#     'zigHori': (2,3),
#     'zigVerti': (3,2),
# }

maxVal = 0
def updateMax(newVal):
    global maxVal
    if newVal > maxVal:
        maxVal = newVal

# borderX = tetroRectDict['2b2'][0]
# borderY = tetroRectDict['2b2'][1]
for i in range(m):
    for j in range(n):
        # 2 by 2
        if i < m - 2 + 1 and j < n - 2 + 1:
            val = board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1]
            updateMax(val)
        # verti
        if i < m - 4 + 1 and j < n - 1 + 1:
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            updateMax(val)
        # hori
        if i < m - 1 + 1 and j < n - 4 + 1:
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            updateMax(val)

        if i < m - 2 + 1 and j < n - 3 + 1:
            # capHori - two cases
            val = board[i+1][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            updateMax(val)
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j + 1]
            updateMax(val)

            # LHori
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
            updateMax(val)
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]
            updateMax(val)
            val = board[i][j]+ board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            updateMax(val)
            val = board[i][j+2]+ board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            updateMax(val)

            # zigHori
            val = board[i][j+1] + board[i][j+2] + board[i+1][j] + board[i+1][j+1]
            updateMax(val)
            val = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            updateMax(val)


        if i < m - 3 + 1 and j < n - 2 + 1:
            # capVerti
            val = board[i+1][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            updateMax(val)
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+1][j + 1]
            updateMax(val)

            # LVerti
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i][j + 1]
            updateMax(val)
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j + 1]
            updateMax(val)
            val = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            updateMax(val)
            val = board[i+2][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            updateMax(val)

            # zigVerti
            val = board[i+1][j] + board[i+2][j] + board[i][j+1] + board[i+1][j+1]
            updateMax(val)
            val = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
            updateMax(val)

            # print('verti loop', i , j )


print(maxVal)





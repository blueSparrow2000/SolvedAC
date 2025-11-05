import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
invert type1 chessboard == type2 chessboard
=> we only have to check for pattern of type 1 (black first)
for other pattern's minimal painting number = 8^2 - (type 1 minimal painting num)
'''

chessBoardX = 8
chessBoardY = 8
totalBoardSize = chessBoardX*chessBoardY

def getColorOfTypeOnePatternAtIdx(i,j):
    return 'B' if (i+j)%2==0 else 'W'

# n row, m col
n,m = map(int,input().replace('\n', '').split(' '))
board = [] # 2D matrix
for i in range(n): # get a row
    rowPatternString = input().replace('\n', '')
    # calculate difference with type 1
    rowpatternDiff = [rowPatternString[j]==getColorOfTypeOnePatternAtIdx(i,j) for j in range(len(rowPatternString))] # true = 1 / false = 0
    board.append(rowpatternDiff)

minimumPaintingNumber = totalBoardSize # initially, make it 64 (any sub board's minimal painting number must be smaller than this number)
# for each sub boards - get 8 by 8 portions
for i in range(n-chessBoardX+1):
    for j in range(m-chessBoardY+1):
        # calculate the sub board sum
        subBoardPaintingNumber = 0
        for bi in range(i, i+chessBoardX):
            subBoardPaintingNumber += sum(board[bi][j:j+chessBoardY])
        # compare the smallest number considering type 2
        subBoardPaintingNumber = min(subBoardPaintingNumber, totalBoardSize - subBoardPaintingNumber)

        if subBoardPaintingNumber < minimumPaintingNumber: # update global minima
            minimumPaintingNumber = subBoardPaintingNumber


print("%d"%minimumPaintingNumber)






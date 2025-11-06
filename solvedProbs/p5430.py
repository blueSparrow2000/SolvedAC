import sys
input = sys.stdin.readline

''' 
# 5430 
solved.ac에서 성공한거: 하나씩 빼도 된당
'''

# number of test case
T = int(input()) # <= 100

for t in range(T): # for each test case, do
    operations = input().strip() # operation string
    input() # python dont need number of array elem
    listGiven = input().replace('\n', '').replace('[', '').replace(']', '')
    if listGiven:
        array = list(map(int, listGiven.split(',')))
    else:
        array = []

    # virtually flip
    flipped = False # final state to reverse the list or not
     # this is either -1(flipped) or 0

    errorFlag = False
    for op in operations:
        if op == 'R':
            flipped = not flipped # invert
        else: # op == 'D'
            if len(array) == 0: # don't have to do remaining op
                errorFlag = True
                continue
            else:
                if flipped: # remove last elem - it is the real first elem
                    array.pop()
                else: # remove first elem
                    array.pop(0)

    if errorFlag:
        print('error')
    else:
        if flipped:
            array.reverse()
        print("[%s]"%','.join(list(map(str, array))))
        # result is [] final array or 'error'
''' 
# test.ac 에서 시간초과 해결한거: 여러개 한꺼번에 빼야 한다

import sys
input = sys.stdin.readline

def deleteMutiple(givenList, delCount, flipped):
    result = []
    curLength = len(givenList)
    if curLength < delCount:  # list smaller than number of element to remove
        return False, result
    # elif curLength == delCount:
    #     return True, []

    # safe
    if flipped:  # remove last elem - it is the real first elem
        result = givenList[0:curLength-delCount]
    else:  # remove first elem
        result = givenList[delCount:curLength]
    return True, result

# number of test case
T = int(input()) # <= 100

for t in range(T): # for each test case, do
    operations = input().strip() # operation string
    input() # python dont need number of array elem
    listGiven = input().replace('\n', '').replace('[', '').replace(']', '')
    if listGiven:
        array = list(map(int, listGiven.split(',')))
    else:
        array = []

    # virtually flip
    flipped = False # final state to reverse the list or not
    delCount = 0

    errorFlag = False
    for op in operations:
        if op == 'D':
            delCount += 1
        else: # op == 'R'
            # efficient deletion
            if delCount > 0: # need deletion
                success, array = deleteMutiple(array, delCount, flipped)
                delCount = 0  # reset
                if not success: # an error occurred
                    errorFlag = True
                    break # no need to check remaining op

            # reverse the list
            flipped = not flipped  # invert

    # check del count, if it exists, remove accordingly
    if delCount > 0:
        success, array = deleteMutiple(array, delCount, flipped)
        delCount = 0  # reset
        if not success:  # an error occurred
            errorFlag = True

    if errorFlag:
        print('error')
    else:
        if flipped:
            array.reverse()
        print("[%s]"%','.join(list(map(str, array))))
        # result is [] final array or 'error'
'''

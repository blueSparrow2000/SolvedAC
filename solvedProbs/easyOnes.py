import sys
input = sys.stdin.readline
print = sys.stdout.write


''' 
# 11720 sum numbers

numberOfNums = int(input().replace('\n', ''))
allNums = input().replace('\n', '')

result = 0
for i in range(numberOfNums):
    num = int(allNums[i])
    result += num

print("%d"%result)
'''

''' 
# 10818 min max
num range from -1,000,000 to 1,000,000

numberOfNums = int(input().replace('\n', ''))
# length must be equal to numberOfNums
allNumString = input().replace('\n', '').split(' ')

numList = [int(x) for x in allNumString] # save as int

# at least there is one number given
# or set min max to the first number at the start?
minNum = 1000000
maxNum = -1000000
for num in numList:
    if num > maxNum:
        maxNum = num
    if num < minNum:
        minNum = num

print("%d %d"%(minNum, maxNum))
'''

'''
# 2562 find max among 9 nums

numList = []
# get 9 nums
for i in range(9):
    num = int(input().replace('\n', ''))
    numList.append(num)

# get max
maxNum = numList[0]
maxNumOrder = 1
for i in range(len(numList)):
    num = numList[i]
    if num > maxNum:
        maxNum = num
        maxNumOrder = i+1

# print
print("%d\n%d"%(maxNum,maxNumOrder))
'''


'''
# 11650 plane

# get number of integers to sort
N = int(input().replace('\n', ''))
coordList = []

for i in range(N):
    data = list(map(int, input().replace('\n', '').split(' ')))
    coordList.append(data)

coordList.sort(key = lambda x:(x[0], x[1]))
coordList = ['%d %d'%(data[0], data[1]) for data in coordList]
print("\n".join(coordList))
'''

'''
# 1920 find elem

# get int list
N = int(input())
intList = set(map(int, input().split(' ')))

# get list of int to find
M = int(input())
findInList = list(map(int, input().split(' ')))

result = ['1' if (item in intList) else '0' for item in findInList]

print('\n'.join(result))
'''

'''
# 2164 

import math

N = int(input())
k = math.floor(math.log2(N))
power2 = 2**k
delta = N-power2
if (delta==0):
    print("%d" %N)
else:
    print("%d"%(2*delta))
'''

'''
# 10816 count occurence in num list

from collections import Counter

# get int list
N = int(input())
intList = list(map(int, input().split(' ')))

intDict = dict(Counter(intList))

# get list of int to find
M = int(input())    
findInList = list(map(int, input().split(' ')))

result = [str(intDict[item]) if item in intDict else '0' for item in findInList]

print(' '.join(result))
'''

'''
# 9012 VPS

# number of checking
N = int(input())
PSList = []
result = []

# get inputs
for i in range(N):
    ps = input().replace('\n', '')
    PSList.append(ps)

def checkVPS(ps):
    height = 0
    for c in ps:
        if c =='(': # climb up
            height += 1
        else: # climb down
            height -= 1
        # check non negative height
        if height < 0: # failed
            return 'NO'

    # check height becomes 0 at the final
    if height != 0:
        return 'NO'
    return 'YES'

# calc output
for ps in PSList:
    result.append(checkVPS(ps))

print('\n'.join(result))
'''

'''
# 1929 prime

import math
from itertools import compress

lower, upper = map(int,input().replace('\n', '').split(' '))
sieve = [True] * (upper+1)
sieve[0] = False
sieve[1] = False

for p in range(2, math.floor(math.sqrt(upper))+1):
    if sieve[p]:
        sieve[p**2::p] = [False]*((upper-p**2)//p+1)

result = list(map(str, list(compress(range(lower, (upper+1)), sieve[lower:]))))
print('\n'.join(result))
'''

'''
# 2108 statistics

from collections import Counter

# number of checking
N = int(input())
numberList = []

# get inputs
for i in range(N):
    numberList.append( int(input()) )

# arithmetic avg
print("%d\n"%round(sum(numberList)/N))

# center value of odd numbers
numberList.sort()
print("%d\n"%numberList[N//2])

# most frequent
numberDict = Counter(numberList) # O(n) / if you called list.count n times, it is O(n^2)

topOne = numberDict.most_common(1)[0]
frequentNum = topOne[0]
topFrequency = topOne[1]
if N > 1:  # can be multiple element with multiple occurence
    top_freq = list(filter(lambda x: x[1] == topFrequency ,numberDict.most_common()))
    if len(top_freq) > 1: # if there are more than one top frequency numbers
        top_freq.sort(key=lambda x: x[1])
        frequentNum = top_freq[1][0]  #get the second smallest


print("%d\n"%frequentNum)

# range
print("%d\n"%(numberList[-1] - numberList[0]) )

'''

'''
# 10773

# import sys
# input = sys.stdin.readline
# 
# # number of checking
# N = int(input())
# 
# # get inputs
# numStack = []
# for i in range(N):
#     num = int(input())
#     if num==0:
#         numStack.pop() # remove latest added element
#     else:
#         numStack.append(num)
# 
# print(sum(numStack))
# 
# # input_data = sys.stdin.read().split()
# # for num in map(int, input_data[1:]):
'''


''' 
# 18110

# import sys
# import math
# input = sys.stdin.readline
# # Take care of python's banker's rounding policy
# def roundStrict(realNum):
#     return math.floor(realNum + 0.5)
#
# rate = 0.3
# halfRate = rate/2
# # get ratings data
# N = int(input())
# if N==0:
#     print('0')
# else:
#     points = []
#     for i in range(N):
#         points.append(int(input()))
#
#     points.sort()
#
#     quantile = roundStrict(halfRate*N)
#     if quantile > 0:
#         print( "%d"%roundStrict(sum(points[quantile: -quantile])/(N - 2*quantile)) )
#     else: # 0 quantile (too small data)
#         print("%d" % roundStrict(sum(points) / N))

'''

'''
# 17626 Four squares

import sys
import math
input = sys.stdin.readline

def getFourSquares():
    min_sum_count = 4 # decide 3 or 4
    n = int(input())
    sqrtN1 = math.sqrt(n)
    n1 = math.floor(sqrtN1)
    # print('n1', n1)
    if sqrtN1.is_integer(): return 1  # only need one -> no need to see deeper
    # if given number is not a square
    for k1 in range(n1, n1//2, -1):
        r1 = n - k1**2
        sqrtN2 = math.sqrt(r1)
        n2 = math.floor(sqrtN2)
        # print('n2', n2)
        if sqrtN2.is_integer(): return 2  # 2 is the minimal needed if num is not a square
        for k2 in range(n2, 0, -1):
            r2 = r1 - k2**2
            sqrtN3 = math.sqrt(r2)
            n3 = math.floor(sqrtN3)
            # print('n3',n3)
            if sqrtN3.is_integer(): min_sum_count = 3  # only need three num - but not certain. there may be two num case
            for k3 in range(n3, 0, -1):
                r3 = r2 - k3**2
                n4 = math.sqrt(r3)
                # print('n4',n4)
                if n4.is_integer(): min_sum_count = min(min_sum_count, 4) # non zero int => need 4 int
                else: # Failed: try other case
                    pass
    return min_sum_count
print(getFourSquares())

'''



import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
Sorting
'''

# get number of integers to sort
N = int(input().replace('\n', ''))
dataList = []

for i in range(N):
    data = input().replace('\n', '').split(' ')
    dataList.append([int(data[0]), data[1]])

dataList.sort(key = lambda x:x[0])
dataList = ['%d %s'%(data[0], data[1]) for data in dataList]
print("\n".join(dataList))










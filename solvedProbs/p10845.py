import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
Queue
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

# number of operations
nOps = int(input())
queue = []

for i in range(nOps): # for each operations, parse
    op = input().replace('\n', '').split(' ')
    parsedOp = op[0]
    # print('parsed op: %s'%parsedOp)

    if len(op) == 1: # length 1 operations
        if parsedOp == 'pop':
            if not queue:
                print('-1\n')
            else:
                print("%d\n"%queue[0]) # print first element
                queue.remove(queue[0]) # remove first occurence
        elif parsedOp == 'size':
            print("%d\n"%len(queue))
        elif parsedOp == 'empty':
            if not queue:
                print('1\n')
            else:
                print('0\n')
        elif parsedOp == 'front':
            if not queue:
                print("-1\n")
            else:
                print("%d\n"%queue[0])
        elif parsedOp =='back':
            if not queue:
                print("-1\n")
            else:
                print("%d\n"%queue[-1])

    else: # length 2 operations == push operation
        enqueueInt = int(op[1])
        queue.append(enqueueInt)













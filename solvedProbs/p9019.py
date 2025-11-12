import sys
from collections import deque
input = sys.stdin.readline

'''
DSLR
동일한 숫자가 다시 나온 경우 (재도달), queue에 넣을 필요가 없다
=> table 에 숫자 저장해 두기
'''

def DSLR_BFS(a,b):
    queue = deque([(a,'')])
    generatedNum = [False] * 10000 # 0 부터 9999까지 만개 방문여부

    generatedNum[a] = True
    if a==b:
        return ''

    while True:
        num, seq = queue.popleft()
        # D
        opD = (2 * num) % 10000
        if opD == b:
            return seq + 'D'
        if not generatedNum[opD]: # 이전에 만든적 없을때만 추가한다
            generatedNum[opD] = True
            queue.append((opD,seq + 'D'))
        # S
        opS = (num -1) % 10000
        if opS == b:
            return seq + 'S'
        if not generatedNum[opS]: # 이전에 만든적 없을때만 추가한다
            generatedNum[opS] = True
            queue.append((opS, seq + 'S'))

        # L
        d1 = num // 1000
        opL = (num%1000)*10 + d1
        if opL == b:
            return seq + 'L'
        if not generatedNum[opL]: # 이전에 만든적 없을때만 추가한다
            generatedNum[opL] = True
            queue.append((opL, seq + 'L'))
        # R
        d4 = num % 10
        opR = num//10 + d4*1000
        if opR == b:
            return seq + 'R'
        if not generatedNum[opR]: # 이전에 만든적 없을때만 추가한다
            generatedNum[opR] = True
            queue.append((opR, seq + 'R'))

        # print(queue)
    return ''

T = int(input())

for t in range(T):
    a,b = map(int, input().split(' '))
    print(DSLR_BFS(a,b))









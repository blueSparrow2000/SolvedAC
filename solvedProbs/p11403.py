import sys
input = sys.stdin.readline

'''
graph connectivity

directional graph 임 => 연결 방향이 중요하다! 그 방향을 따라서만 도달할 수 있음
print reachability graph
'''

def printMat(mat, rowlen):
    for i in range(rowlen):
        print(' '.join(map(str, mat[i])))

n = int(input())
adj = [] # adjacency matrix

for i in range(n):
    row = list(map(int, input().split(' ')))
    adj.append(row)

for c in range(n): # column check
    for r in range(n):
        if adj[r][c]: # if non zero => update row!
            adj[r] = [1 if adj[c][i] else adj[r][i] for i in range(n)]

printMat(adj,n)










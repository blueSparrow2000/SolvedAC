import sys
input = sys.stdin.readline

'''
# ring world
'''


T = int(input()) # number of test cases 1~20

points = []
for i in range(T):
    Ncity,Nzone = map(int, input().split(' '))
    # Nzone restrictions
    zones = []
    for z in range(Nzone):
        startZone, endZone = map(int, input().split(' ')) # 한 zone의 시작 index와 끝 index(모두 포함임!)
        


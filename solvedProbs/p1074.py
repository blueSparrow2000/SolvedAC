import sys
input = sys.stdin.readline

'''
# Z
2^n by 2^n matrix
find the order of visit of (r,c) element
'''

n,r,c = map(int, input().strip().split(' ')) # number of test cases 1~20

order = 0
sb = 2**(n-1) # sub block length
while sb > 0:
    sbArea = sb ** 2
    if sb <= r:
        order += 2*sbArea
        r -= sb
    if sb <= c:
        order += sbArea
        c -= sb
    # print("%d: %d"%(sb, order))
    sb //= 2

print(order)









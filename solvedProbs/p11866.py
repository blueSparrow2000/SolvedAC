import sys
input = sys.stdin.readline
print = sys.stdout.write

# list deletion at index
# del list[index]

n,k = map(int, input().split(' '))
table = [i for i in range(1, n+1)]

sequence = []
alive = len(table)
removeAt = 0
while alive>0:
    # calculate index
    removeAt = (removeAt+k -1)%alive

    sequence.append(str(table[removeAt]))
    del table[removeAt]
    alive =  len(table)

print("<" +', '.join(sequence) + ">")







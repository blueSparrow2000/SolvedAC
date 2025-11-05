import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().replace('\n', ''))
words = []
for i in range(N): # get list of words
    words.append(input().replace('\n', ''))

# remove duplicates
words = list(set(words))

words.sort() # lexicographically first
words.sort(key = len ) # then sort by length

print('\n'.join(words))
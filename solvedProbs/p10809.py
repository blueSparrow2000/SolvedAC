import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
For each alphabets, find index of the first appearance of it in the given word
'''

alphabetVec = [-1 for i in range(26)] # 26 alphabets

def printListWithSpace(listToPrint):
    for elem in listToPrint:
        print("%d "%elem)
    # print characters
    # print("\n")
    # for i in range(len(listToPrint)):
    #     if listToPrint[i] == -1:
    #         print(" ")
    #     print("%s " % chr(i + 97))

def identifyCharAtIndex(idx): # idx is an index of the current character in the word we are identifying
    global word
    # code number of a character (relative to a, since it is all lowercase letters)
    charCode = ord(word[idx]) - ord("a")

    # we have to check whether each alphabet appears only for the first time
    if (alphabetVec[charCode]==-1): # if only for the first time
        alphabetVec[charCode] = idx # assign

word = input().replace('\n', '')

for i in range(len(word)):
    identifyCharAtIndex(i)

printListWithSpace(alphabetVec)

























import sys
input = sys.stdin.readline
print = sys.stdout.write

'''
word duplication
'''
testCaseNum = int(input().replace('\n', ''))

testCaseList = []
resultList = []
for i in range(testCaseNum): # get test cases
    testCase = input().replace('\n', '').split(' ')
    testCaseList.append(testCase)

for testCase in testCaseList:
    repeatNum = int(testCase[0])
    repeatString = testCase[1]
    resultOneList = []
    for st in repeatString:
        resultOneList.append(st*repeatNum)
    result = ''.join(resultOneList)+"\n"
    resultList.append(result)

resultString = ''.join(resultList)
print(resultString)




















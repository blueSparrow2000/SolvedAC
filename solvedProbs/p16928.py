import sys
input = sys.stdin.readline

'''
ladder and snake
'''
rules = dict()
ladder, snake = map(int, input().split(' '))
for i in range(ladder + snake):
    start, end = map(int, input().split(' '))
    # assign rules
    rules[start] = end
ruleKey = list(rules.keys())

def applyRule(x):
    global rules, ruleKey
    if x in ruleKey:
        return rules[x]
    return x

def play():
    parentNodes = [1]
    childNodes = set()

    depth = 0
    reached100 = False
    while not reached100:
        depth += 1
        # print(parentNodes)
        while parentNodes:
            p = parentNodes.pop()
            rollout = [applyRule(x) for x in range(p+1, p+7)]
            if 100 in rollout:
                reached100 = True
                return depth
            childNodes.update(rollout)

        parentNodes = list(childNodes)
        childNodes = set() # reset


print(play())
























import sys
from collections import deque
# from bisect import bisect_left
input = sys.stdin.readline

'''
Graph traversal: DFS, BFS
edges: bidirectional

Duplicate visits not allowed => check for visited nodes
If many neighbors => visit smaller node number first

'''

class Node():
    def __init__(self, num):
        self.myNum = num
        self.neighbors = []
        self.visitedDFS = False
        self.visitedBFS = False

    def addEdge(self, node):
        # insertIdx = bisect_left(self.neighbors,nodeNum)
        # self.neighbors.insert(insertIdx, nodeNum)
        if not (node in self.neighbors):
            self.neighbors.append(node)

    def getNeighbors(self):
        return self.neighbors

    def sortNeighbors(self):
        self.neighbors.sort(key = lambda x: x.myNum)

    def visitDFS(self):
        self.visitedDFS = True
        self.printMyNum()
        for nbh in self.neighbors:
            if not nbh.visitedDFS:
                nbh.visitDFS()

    def printMyNum(self):
        print(self.myNum, end=' ')


nodes, edges, startNode = map(int, input().split(' '))
nodeList = [Node(i) for i in range(1,nodes+1)]

for i in range(edges):
    edgeStart, edgeEnd = map(int, input().split(' '))
    nodeList[edgeStart-1].addEdge(nodeList[edgeEnd-1])
    nodeList[edgeEnd-1].addEdge(nodeList[edgeStart-1])

# sort neighbors prior
for node in nodeList:
    node.sortNeighbors()

# traverse DFS
StartingNode = nodeList[startNode-1]
StartingNode.visitDFS()

print()
# traverse BFS - destructive way (node neighbor list will be destroyed after BFS traversal)
queue = deque(StartingNode.getNeighbors())
StartingNode.visitedBFS = True
StartingNode.printMyNum()
while queue:
    node = queue.popleft()
    node.visitedBFS = True
    node.printMyNum()
    nbd = [n for n in node.getNeighbors() if (not n.visitedBFS) and (not n in queue)]
    queue.extend(nbd)















class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode
linkedList = [Node() for _ in range(10)]
linkedList[0] = Node(1, 1)
linkedList[1] = Node(5, 4)
linkedList[2] = Node(6, 7)
linkedList[3] = Node(7, -1)
linkedList[4] = Node(2, 2)
linkedList[5] = Node(0, 6)
linkedList[6] = Node(0, 8)
linkedList[7] = Node(56, 3)
linkedList[8] = Node(0, 9)
linkedList[9] = Node(0, -1)
startPointer = 0
emptyList = 5
def outputNodes(linkedList, startPointer):
    while startPointer != -1:
        print(linkedList[startPointer].data)
        startPointer = linkedList[startPointer].nextNode
def addNode(linkedList, startPointer, emptyList):
    data = int(input('Enter anything'))
    if emptyList == -1:
        return False
    newNodeIndex = emptyList
    linkedList[newNodeIndex].data = data
    emptyList = linkedList[newNodeIndex].nextNode
    linkedList[newNodeIndex].nextNode = -1
    if startPointer == -1:  #if no initial value in linked list
        startPointer = newNodeIndex
    else:
        while linkedList[startPointer].nextNode != -1:
            startPointer = linkedList[startPointer].nextNode
        linkedList[startPointer].nextNode = newNodeIndex
    return True
outputNodes(linkedList, startPointer)
print("Adding new node with provided data.")
result= addNode(linkedList, startPointer, emptyList)
if result:
    print("Node added.")
else:
    print("Failed to add node.")
outputNodes(linkedList, startPointer)

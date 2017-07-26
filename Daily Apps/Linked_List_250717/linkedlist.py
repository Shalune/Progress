class LinkedList:

    head = None

    def __init__(self, head):
        self.head = head

    def GetElement(self, elementNum):
        currentNode = self.head
        index = 0
        while(True):
            if(currentNode == None):
                return None
            if(index == elementNum):
                return currentNode
            currentNode = currentNode.next
            index += 1
        return None

class Node:
    value = 0
    next = None

    def __init__(self, value, next = None):
        self.value = value
        self.next = next
from Linked_List_250717 import linkedlist
import random



def runTests():
    nodeTests()
    llTests()



def nodeTests():
    createNodeTest()
    nextNodeLoopTest()

def createNodeTest():
    testDesctiption = "node creation with random value = "
    for i in range(1,30):
        val = random.randint(0,999)
        newNode = linkedlist.Node(val)
        myTest(testDesctiption + str(val), newNode.value == val)


def nextNodeLoopTest():
    testDescription = "node link loop, at index "
    size = 5
    currentNode = testableListHead(size)

    index = 0
    while(index < size):
        myTest(testDescription + str(index), currentNode.value == index)
        currentNode = currentNode.next
        index+=1


def llTests():
    getElementTest()
    appendTest()


def getElementTest():
    testDescription = "from linked list get element numnber "
    size = 5
    head = testableListHead(size)
    list = linkedlist.LinkedList(head)
    for i in range(1,10):
        val = random.randint(0,size-1)
        myTest(testDescription + str(val), list.getElement(val).value == val)


def appendTest():
    testDescription = "append new node test "
    size = 5

    for i in range(1,10):
        head = testableListHead(size)
        list = linkedlist.LinkedList(head)
        val = random.randint(50,999)
        newTail = linkedlist.Node(val)
        list.append(newTail)
        myTest(testDescription, list.getElement(size) == newTail)


def testableListHead(size):
    index = 0
    head = prevNode = linkedlist.Node(index)
    index = 1
    while (index < size):
        prevNode.next = linkedlist.Node(index)
        index += 1
        prevNode = prevNode.next
    return head


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    runTests()
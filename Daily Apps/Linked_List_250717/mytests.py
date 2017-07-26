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
    return


def getElementTest():
    return


def testableListHead(size):
    index = 0
    head = prevNode = linkedlist.Node(index)
    while (index < size):
        index += 1
        prevNode.next = linkedlist.Node(index)
        prevNode = prevNode.next
    return head


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    runTests()
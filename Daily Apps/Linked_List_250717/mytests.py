from Linked_List_250717 import linkedlist
import random



def runTests():
    nodeTests()
    #llTests()


def nodeTests():
    createNodeTest()
    nextNodeLoopTest()

def createNodeTest():
    for i in range(1,30):
        val = random.randint(0,999)
        newNode = linkedlist.Node(val)
        myTest("node creation with random value = " + str(val), newNode.value == val)


def nextNodeLoopTest():
    index = 0
    currentNode = prevNode = linkedlist.Node(index)
    while(index<5):
        index += 1
        prevNode.next = linkedlist.Node(index)
        prevNode = prevNode.next

    index = 0
    while(index<5):
        myTest("node link loop test, at index " + str(index), currentNode.value == index)
        currentNode = currentNode.next
        index+=1


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    runTests()
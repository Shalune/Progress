from Linked_List_250717 import linkedlist
import random



def runTests():
    nodeTest()


def nodeTest():
    for i in range(1,30):
        val = random.randint(0,999)
        newNode = linkedlist.Node(val)
        myTest("node creation with random value = " + str(val), newNode.value == val)


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    runTests()
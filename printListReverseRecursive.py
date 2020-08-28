from list import Node
from list import LinkedList

def printReverse(node):
    if node:
        printReverse(node.next)
        print node.data,

a = LinkedList()
for i in range(8):
    a.append(i)
a.printList()
printReverse(a.head)

from list import LinkedList
from list import Node

def decimalEquivalent(node):
    a = 0 
    while node:
        a = a * 2 + node.data
        node = node.next
    return a

l  = LinkedList()
l.append(0)
l.append(1)
l.append(0)
l.append(0)
l.append(1)
l.append(1)
l.append(0)

l.printList()
print decimalEquivalent(l.head)

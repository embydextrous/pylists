from list import LinkedList
from list import Node

def isIdentical(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.data == b.data and isIdentical(a.next, b.next)

a = LinkedList()
a.append(1)
b = LinkedList()
b.append(1)
b.append(2)

print isIdentical(a.head, b.head)
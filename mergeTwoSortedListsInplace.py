from list import LinkedList
from list import Node

def mergeRecursive(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        a.next = mergeRecursive(a.next, b)
        return a
    else:
        b.next = mergeRecursive(a, b.next)
        return b 

l = LinkedList()
l.append(1)
l.append(2)
l.append(4)
l.printList()
s = LinkedList()
s.append(3)
s.append(4)
s.append(5)
s.printList()

m = LinkedList()
m.head = mergeRecursive(l.head, s.head)
m.printList()


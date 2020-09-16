from list import LinkedList
from list import Node

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    head = a if a.data < b.data else b
    prevA = None
    while a and b:
        if a.data <= b.data:
            prevA, a = a, a.next
        else:
            nextA, nextB = a.next, b.next
            prevA.next = b
            b.next = a
            prevA = b
            b = nextB
    if a is None:
        prevA.next = b
    return head

def mergeRecursive(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data < b.data:
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


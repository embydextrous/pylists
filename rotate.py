from list import LinkedList
from list import Node

def leftRotate(l, k):
    if k == 0 or l.head is None:
        print "b"
        return
    size = 1
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
        size += 1
    k = k % size
    if k == 0:
        return
    lastNode.next = l.head
    current = l.head
    while k != 1:
        k -= 1
        current = current.next
    l.head = current.next
    current.next = None

def rightRotate(l, k):
    if k == 0 or l.head is None:
        print "b"
        return
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
    a, b, x = l.head, l.head, k
    while b and x > 0:
        b = b.next
        x -= 1
    if b is None:
        return
    else:
        while b.next:
            a, b = a.next, b.next
        lastNode.next = l.head
        l.head = a.next
        a.next = None
    
a = LinkedList()
for i in range(1, 9):
    a.append(i)
a.printList()
leftRotate(a, 6)
a.printList()
rightRotate(a, 9)
a.printList()
    
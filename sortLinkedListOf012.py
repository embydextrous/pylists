from list import LinkedList
from list import Node

def sort(l):
    if l.head is None:
        return
    for i in range(3):
        sortUtil(l, i)

def sortUtil(l, i):
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
    firstInode = None
    prev, current = None, l.head
    while current and firstInode != current:
        if current.data == i:
            if firstInode is None:
                firstInode = current
            if prev is None:
                l.head = current.next
                lastNode.next = current
                lastNode = lastNode.next
                current.next = None
                current = l.head
            else:
                prev.next = current.next
                lastNode.next = current
                lastNode = lastNode.next
                current.next = None
                current = prev.next
        else:
            prev, current = current, current.next

a = LinkedList()
a.append(1)
a.append(1)
a.append(0)
a.append(2)
a.append(0)
a.append(0)
a.append(1)
a.append(2)
a.append(0)
a.append(1)
a.append(2)
a.append(2)
a.append(1)
a.append(1)
a.append(2)
a.printList()
sort(a)
a.printList()


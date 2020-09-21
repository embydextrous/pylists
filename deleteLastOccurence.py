from list import LinkedList
from list import Node

def deleteLast(l, key):
    prev, current = None, l.head
    prevLastOcc, lastOcc = None, None
    while current:
        if current.data == key:
            prevLastOcc, lastOcc = prev, current
        prev, current = current, current.next
    if lastOcc is None:
        return
    if prevLastOcc is None:
        l.head = l.head.next
    else:
        prevLastOcc.next = lastOcc.next
    lastOcc.next = None
    lastOcc = None

l = LinkedList()
for i in range(8):
    l.append(i)
l.printList()
deleteLast(l, 6)
l.printList()
deleteLast(l, 7)
l.printList()
deleteLast(l, 7)
l.printList()
deleteLast(l, 1)
l.printList()
deleteLast(l, 2)
deleteLast(l, 3)
deleteLast(l, 4)
deleteLast(l, 0)
deleteLast(l, 5)
l.printList()
deleteLast(l, 1)
l.append(1)
l.append(2)
l.append(1)
l.append(2)
l.append(1)
l.printList()
deleteLast(l, 1)
l.printList()
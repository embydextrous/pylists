from list import LinkedList
from list import Node

def moveAllOccurencesToEnd(l, x):
    if l.head is None:
        return
    prev, current = None, l.head
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
    firstKeyNode = None
    while current and lastNode != firstKeyNode:
        if current.data == x:
            if current == l.head:
                l.head = current.next
                lastNode.next = current
                current.next = None
                current = l.head
                lastNode = lastNode.next
            else:
                prev.next = current.next
                lastNode.next = current
                current.next = None
                current = prev.next
                lastNode = lastNode.next
            if firstKeyNode is None:
                firstKeyNode = lastNode
        else:
            prev, current = current, current.next

a = LinkedList()
a.append(1)
a.append(0)
a.append(0)

a.printList()
moveAllOccurencesToEnd(a, 1)
a.printList()



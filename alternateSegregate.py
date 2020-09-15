from list import LinkedList
from list import Node

def alternateSegregate(l):
    if l.head is None:
        return
    first, second = LinkedList(), LinkedList()
    lastNode = l.head
    while lastNode.next:
        lastNode = lastNode.next
    current = l.head
    lNode = lastNode
    prev = None
    while current != lastNode:
        next = current.next
        current.next = next.next
        lNode.next = next
        next.next = None
        lNode = lNode.next
        prev = current
        current = current.next
        if lNode == lastNode:
            break
    first.head = l.head
    second.head = current if lastNode == lNode else current.next
    if lastNode != lNode:
        current.next = None
    else:
        print current.data
        prev.next = None
    return [first, second]
    
    

l = LinkedList()
for i in range(1, 9):
    l.append(i)
l.printList()
a = alternateSegregate(l)
a[0].printList()
a[1].printList()



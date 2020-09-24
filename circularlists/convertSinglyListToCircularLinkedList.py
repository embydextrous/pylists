from list import LinkedList
from circularlist import CircularLinkedList
from list import Node
from circularlist import Node as CircularNode

def toCircular(head):
    c = CircularLinkedList()
    if head is None:
        return c
    lastNode = head
    while lastNode.next:
        lastNode = lastNode.next
    c.tail = lastNode
    lastNode.next = head
    return c

l = LinkedList()
for i in range(1):
    l.append(i)
l.printList()
toCircular(l.head).printList()

from list import LinkedList
from list import Node

def merge(a, b):
    if a.head is None or b.head is None:
        return
    head = tail = a.head
    aNode, bNode = a.head.next, b.head
    while aNode and bNode:
        tail.next = bNode
        tail = tail.next
        bNode = bNode.next
        tail.next = aNode
        tail = tail.next
        aNode = aNode.next
    if aNode:
        tail.next = aNode
    if bNode:
        tail.next = bNode
    b.head = None
    a.head = head

a = LinkedList()
for i in range(6):
    a.append(i)
a.printList()
b = LinkedList()
for i in range(6, 12):
    b.append(i)
b.printList()
merge(a, b)
a.printList()
b.printList()

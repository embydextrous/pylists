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
    if bNode:
        tail.next = bNode
        bNode = bNode.next
        tail.next.next = None
    b.head = bNode
    a.head = head

def merge2(a, b):
    if a.head is None or b.head is None:
        return
    aNode = a.head
    bNode = b.head
    while aNode and bNode:
        next = bNode.next
        bNode.next = aNode.next
        aNode.next = bNode
        b.head = next
        aNode = bNode.next
        bNode = next



a = LinkedList()
for i in range(3):
    a.append(i)
a.printList()
b = LinkedList()
for i in range(6, 12):
    b.append(i)
b.printList()
merge2(a, b)
a.printList()
b.printList()

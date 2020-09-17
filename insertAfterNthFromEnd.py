from list import LinkedList
from list import Node

def insertAfterNthFromEnd(l, n, data):
    current = l.head
    for i in range(n):
        if current:
            current = current.next
    if current is None:
        return
    a = l.head
    while current.next:
        a = a.next
        current = current.next
    newNode = Node(data)
    newNode.next = a.next
    a.next = newNode

a = LinkedList()
for i in range(7):
    a.append(i)
a.printList()
insertAfterNthFromEnd(a, 6, 7)
a.printList()
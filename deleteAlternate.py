from list import LinkedList
from list import Node

def deleteAlternate(node):
    while node and node.next:
        next = node.next
        node.next = next.next
        next.next = None
        node = node.next

a = LinkedList()
for i in range(1, 8):
    a.append(i)
a.printList()
deleteAlternate(a.head)
a.printList()

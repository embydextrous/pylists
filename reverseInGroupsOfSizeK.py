from list import LinkedList
from list import Node

def reverse(l, node, k):
    current, next, prev, count = node, None, None, 0
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    if next:
        node.next = reverse(l, next, k)
    return prev


l = LinkedList()
for i in range(1, 9):
    l.append(i)

l.printList()
l.head = reverse(l, l.head, 3)
l.printList()
    
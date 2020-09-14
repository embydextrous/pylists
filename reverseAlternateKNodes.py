from list import LinkedList
from list import Node

def reverse(node, k, i):
    current, next, prev, count = node, None, None, 0
    if i == 0:
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
    else:
        while current and count < k:
            prev, current, next = current, current.next, current.next
            count += 1
    if next:
        if i == 0:
            node.next = reverse(next, k, 1)
        else:
            prev.next = reverse(next, k, 0)
    return prev if i == 0 else node

l = LinkedList()
for i in range(1, 9):
    l.append(i)

l.printList()
l.head = reverse(l.head, 3, 0)
l.printList()



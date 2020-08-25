from list import Node
from list import LinkedList

def getNth(node, n):
    while node and n > 0:
        node = node.next
        n -= 1
    if node:
        return node.data
    else:
        return -1

def getNthFromEnd(node, n):
    a, b = node, node
    for i in range(n):
        if a:
            a = a.next
        else:
            return -1
    if a is None:
        return -1
    while a.next:
        a, b = a.next, b.next
    return b.data

a = LinkedList()
for i in range(1, 8):
    a.append(i)
a.printList()

for i in range(0, 9):
    print getNth(a.head, i)

for i in range(0, 9):
    print getNthFromEnd(a.head, i)
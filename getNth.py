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

a = LinkedList()
for i in range(1, 8):
    a.append(i)
a.printList()

for i in range(0, 9):
    print getNth(a.head, i)
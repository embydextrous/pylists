from list import Node
from list import LinkedList

def search(node, key):
    position = 0
    while node and node.data != key:
        node = node.next
        position += 1
    if node:
        return position
    else:
        return -1

a = LinkedList()
for i in range (1, 8):
    a.append(i)

a.printList()
print search(a.head, 3)
print search(a.head, 8)
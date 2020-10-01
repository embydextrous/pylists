from dll import DLL
from dll import Node

# Just swap prev and next pointers
def reverse(node):
    while node:
        node.prev, node.next = node.next, node.prev
        if node.prev is None:
            break
        node = node.prev
    return node

dll = DLL()
for i in range(10):
    dll.append(i)
dll.printList()
dll.head = reverse(dll.head)
dll.printList()
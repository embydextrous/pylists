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

def reverseData(head, tail):
    if head is None:
        return
    while head != tail and head.prev != tail:
        head.data, tail.data = tail.data, head.data
        head, tail = head.next, tail.prev

dll = DLL()
for i in range(9):
    dll.append(i)
dll.printList()
reverseData(dll.head, dll.tail)
dll.printList()
from dll import DLL
from dll import Node

def removeDuplicates(node):
    while node and node.next:
        if node.data == node.next.data:
            next = node.next
            node.next = next.next
            next.next.prev = node
            next.next = None
            next.prev = None
        else:
            node = node.next

s = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
dll = DLL()
for i in s:
    dll.append(i)
dll.printList()
removeDuplicates(dll.head)
dll.printList()

from dll import DLL
from dll import Node

def removeDuplicates(node):
    s = set()
    while node:
        if node.data in s:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            next = node.next
            node.prev = None
            node.next = None
            node = next
        else:
            s.add(node.data)
            node = node.next

s = [2, 1, 4, 2, 3, 1, 4, 3, 6, 5]
dll = DLL()
for i in s:
    dll.append(i)
dll.printList()
removeDuplicates(dll.head)
dll.printList()

from dll import DLL
from dll import Node

# 1-based Index
def deleteAt(dll, k):
    if k <= 0:
        return
    if dll.head is None:
        return
    if k == 1 and dll.head.next is None:
        dll.head = None
        dll.tail = None
        return
    if k == 1:
        node = dll.head
        dll.head = node.next
        node.next = None
        dll.head.prev = None
    else:
        current = dll.head
        while current and k > 1:
            current = current.next
            k -= 1
        if current is None:
            return
        elif current.next is None:
            dll.tail = current
            current.prev.next = None
            current.prev = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
    
dll = DLL()
for i in range(8):
    dll.append(i)
dll.printList()
deleteAt(dll, 8)
print dll.tail
dll.printList()
from dll import DLL
from dll import Node

def deleteKey(dll, key):
    if dll.head is None:
        return
    current = dll.head
    while current:
        if current.data == key:
            if current == dll.head:
                if current.next is None:
                    dll.head = None
                    dll.tail = None
                    current = None
                else:
                    dll.head = current.next
                    dll.head.prev = None
                    current.next = None
                    current = dll.head
            elif current == dll.tail:
                dll.tail = current.prev
                current.prev.next = None
                current.prev = None
                current = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = current.next
        else:
            current = current.next

dll = DLL()
s = [1, 2, 2, 3, 1, 2, 3,2 ,1, 1,2, 3, 2,1 ]
for i in s:
    dll.append(i)
dll.printList()
deleteKey(dll, 1)
print dll.tail
dll.printList()
deleteKey(dll, 2)
dll.printList()


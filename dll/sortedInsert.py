from dll import DLL
from dll import Node

def sortedInsert(dll, data):
    newNode = Node(data)
    if dll.head and newNode.data < dll.head.data:
        newNode.next = dll.head
        newNode.next.prev = newNode
        dll.head = newNode
        return
    current = dll.head
    while current and current.next:
        if current.next.data > newNode.data:
            break
        current = current.next
    if current is None:
        dll.head = newNode
    elif current.next is None:
        current.next = newNode
        newNode.prev = current
        dll.tail = newNode
    else:
        newNode.next = current.next
        newNode.prev = current
        newNode.next.prev = newNode
        current.next = newNode

dll = DLL()
for i in range(7):
    dll.append(2*i+1)
dll.printList()
sortedInsert(dll, 0)
dll.printList()
sortedInsert(dll, 4)
dll.printList()
sortedInsert(dll, 16)
dll.printList()
sortedInsert(dll, 0)
dll.printList()
sortedInsert(dll, 7)
dll.printList()
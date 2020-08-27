from list import Node
from list import LinkedList

def removeDuplicates(node):
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
            continue
        node = node.next
        

a = LinkedList()
a.append(0)
a.append(0)
a.append(1)
a.append(1)
a.append(1)
a.append(2)
a.append(2)
a.append(2)
a.append(2)
a.append(3)
a.printList()
removeDuplicates(a.head)
a.printList()
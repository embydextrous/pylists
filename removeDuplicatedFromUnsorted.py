from list import Node
from list import LinkedList

def removeDuplicates(node):
    if node is None:
        return
    s = [node.data]
    while node.next:
        if node.next.data in s:
            node.next = node.next.next
            continue
        s.append(node.next.data)
        node = node.next
        

a = LinkedList()
a.append(0)
a.append(3)
a.append(1)
a.append(2)
a.append(1)
a.append(4)
a.append(3)
a.append(0)
a.append(2)
a.append(4)
a.printList()
removeDuplicates(a.head)
a.printList()
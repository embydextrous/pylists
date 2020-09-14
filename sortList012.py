from list import LinkedList
from list import Node

def sort(node):
    a = [0] * 3
    current = node
    while current:
        a[current.data] += 1
        current = current.next
    current = node
    i = 0
    while current and i < 3:
        current.data = i
        current = current.next
        a[i] -= 1
        if a[i] == 0:
            i += 1

l = LinkedList()
l.append(1)
l.append(0)
l.append(2)
l.append(2)
l.append(1)
l.append(1)
l.append(1)
l.append(0)
l.append(0)
l.append(0)
l.append(2)
l.append(1)
l.append(1)
l.append(2)
l.append(1)
l.append(0)

l.printList()
sort(l.head)
l.printList()

    

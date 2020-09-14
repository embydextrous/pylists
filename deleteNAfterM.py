from list import LinkedList
from list import Node

def delete(l, m, n):
    if m == 0:
        while n > 0:
            l.head = l.head.next
            n -= 1
    else:
        current, prev = l.head, None
        while current and m > 0:
            current, prev = current.next, current
            m -= 1
        while current and n > 0:
            next = current.next
            prev.next = next
            current = next
            n -= 1
    
l = LinkedList()
for i in range(1, 9):
    l.append(i)
delete(l, 3, 0)
l.printList()
        
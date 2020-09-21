from list import LinkedList
from list import Node

def swap(a):
    if a is None or a.next is None:
        return a
    temp = swap(a.next.next)
    nextA = a.next
    a.next = temp
    nextA.next = a
    return nextA

a = LinkedList()
for i in range(9):
    a.append(i)
a.printList()
a.head = swap(a.head)
a.printList()
    

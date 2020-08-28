from list import Node
from list import LinkedList

def intersectionOfSortedLists(a, b):
    result = LinkedList()
    while a and b:
        if a.data == b.data:
            result.append(a.data)
            a, b = a.next, b.next
        elif a.data > b.data:
            b = b.next
        else:
            a = a.next
    return result

a = LinkedList()
for i in range(8):
    a.append(i)
a.printList()

b = LinkedList()
for i in range(1, 6):
    b.append(i*2)
b.printList()

intersectionOfSortedLists(a.head, b.head).printList()

from list import LinkedList
from list import Node

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        mergedHead = a
        a = a.next
    else:
        mergedHead = b
        b = b.next
    mergedTail = mergedHead
    while a and b:
        if a.data <= b.data:
            mergedTail.next = a
            a = a.next
        else:
            mergedTail.next = b
            b = b.next
        mergedTail = mergedTail.next
    if a:
        mergedTail.next = a
    if b:
        mergedTail.next = b
    return mergedHead
        
a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
b = LinkedList()
b.append(4)
b.append(5)
b.append(6)
a.printList()
b.printList()
l = LinkedList()
l.head = merge(a.head, b.head)
a.printList()

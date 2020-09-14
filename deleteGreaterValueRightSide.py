from list import LinkedList
from list import Node

def delete(l):
    if l.head:
        reverse(l)
        maxRight = l.head.data
        prev, current = l.head, l.head.next
        while current:
            if current.data < maxRight:
                prev.next = current.next
                current = current.next
            else:
                maxRight = current.data
                prev = current
                current = current.next
            
        reverse(l)


def reverse(l):
    current, prev = l.head, None
    while current:
        next = current.next 
        current.next = prev
        prev, current = current, next
    l.head = prev

l = LinkedList()
l.append(12)
l.append(15)
l.append(10)
l.append(11)
l.append(5)
l.append(6)
l.append(2)
l.append(3)
l.printList()
delete(l)
l.printList()
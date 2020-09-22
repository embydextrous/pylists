from list import LinkedList
from list import Node

def addOne(a):
    head = tail = reverse(a)
    prevTail = None
    carry = 1
    while tail:
        sum = tail.data + carry
        tail.data = sum % 10
        carry = sum / 10
        prevTail, tail = tail, tail.next
    if carry == 1:
        prevTail.next = Node(1)
    return reverse(head)

def reverse(a):
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

a = LinkedList()
a.append(1)
a.append(1)
a.append(2)
a.append(4)
a.printList()
a.head = addOne(a.head)
a.printList()
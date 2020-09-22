from list import LinkedList
from list import Node

def sort(a):
    if a is None:
        return a
    first = a
    head = tail = Node('x')
    while a.next:
        tail.next = a.next
        a.next = a.next.next
        tail = tail.next
        tail.next = None
        a = a.next
    second = reverse(head.next)
    return merge(first, second)

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        head = a
        a = a.next
    else:
        head = b
        b = b.next
    tail = head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head


def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev
    
s = [10, 40, 53, 30, 67, 12, 89]
a = LinkedList()
for i in s:
    a.append(i)
a.printList()
a.head = sort(a.head)
a.printList()
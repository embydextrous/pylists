from list import LinkedList
from list import Node

def mergeKSortedLists(lists):
    while len(lists) > 1:
        p, q = lists.pop(0), lists.pop(0)
        lists.append(merge(p, q))
    l = LinkedList()
    l.head = lists[0]
    return l

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

a = LinkedList()
for i in range(6):
    a.append(2*i+1)
b = LinkedList()
for i in range(3):
    b.append(2*(i+1))
c = LinkedList()
c.append(0)
c.append(9)
c.append(10)
c.append(11)
a.printList()
b.printList()
c.printList()
lists = [a.head, b.head, c.head]
mergeKSortedLists(lists).printList()

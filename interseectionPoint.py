from list import Node
from list import LinkedList

def intersectionPoint(a, b):
    l1 = a.size()
    l2 = b.size()
    p, q = a.head, b.head
    if l1 > l2:
        d = l1 - l2
        while d > 0:
            p = p.next
            d -= 1
    elif l2 < l1:
        d = l1 - l2
        while d > 0:
            q = q.next
            d -= 1
    while p != q:
        p, q = p.next, q.next
    return p.data

a = LinkedList()
b = LinkedList()

for i in range(8):
    a.append(i)

for j in range(8, 10):
    b.append(j)

b.head.next.next = a.head.next.next.next.next.next

a.printList()
b.printList()

print intersectionPoint(a, b)

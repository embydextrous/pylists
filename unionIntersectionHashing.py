from list import LinkedList
from list import Node

def intersection(a, b):
    s = set()
    while a:
        s.add(a.data)
        a = a.next
    head = tail = Node('x')
    while b:
        if b.data in s:
            tail.next = Node(b.data)
            tail = tail.next
        b = b.next
    return head.next

def union(a, b):
    s = set()
    head = tail = Node('x')
    while a:
        if a.data not in s:
            s.add(a.data)
            tail.next = Node(a.data)
            tail = tail.next
        a = a.next
    while b:
        if b.data not in s:
            s.add(b.data)
            tail.next = Node(b.data)
            tail = tail.next
        b = b.next
    return head.next


a = LinkedList()
a.append(10)
a.append(15)
a.append(4)
a.append(20)    
a.printList()
b = LinkedList()
b.append(8)
b.append(4)
b.append(2)
b.append(10)
b.printList()

i = LinkedList()
i.head = intersection(a.head, b.head)
i.printList()

u = LinkedList()
u.head = union(a.head, b.head)
u.printList()
a.append(10)
a.printList()
b.printList()
u.head = union(a.head, b.head)
u.printList()

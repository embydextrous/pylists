from list import LinkedList
from list import Node

def merge(a, b):
    while a and b:
        if (a.data > b.data):
            a.data, b.data = b.data, a.data
            temp = b
            while b.next and b.data > b.next.data:
                b = b.next
                prev, ptr = None, b
                while ptr and ptr.data < temp.data:
                    prev, ptr = ptr, ptr.next
                prev.next = temp
                temp.next = ptr
        if a.next is None:
            break
        a = a.next
    while a.next:
        a = a.next
    a.next = b

a = LinkedList()
a.append(2)
a.append(4)
a.append(7)
a.append(8)
a.append(10)

b = LinkedList()
b.append(1)
b.append(3)
b.append(12)

merge(a.head, b.head)
a.printList()
from list import Node
from list import LinkedList

def multiply(a, b):
    n1 = n2 = 0
    while a:
        n1 = n1 * 10 + a.data
        a = a.next
    while b:
        n2 = n2 * 10 + b.data
        b = b.next
    return n1 * n2


a = LinkedList()
a.append(9)
a.append(4)
a.append(6)
a.printList()
b = LinkedList()
b.append(8)
b.append(4)
b.printList()
print multiply(a.head, b.head)
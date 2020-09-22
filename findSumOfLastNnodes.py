from list import LinkedList
from list import Node

def sumOfLastNNodes(a, n):
    b = a
    while a and n > 0:
        a = a.next
        n -= 1
    if not a:
        sum = 0
        while b:
            sum += b.data
            b = b.next
        return sum
    while a:
        a, b = a.next, b.next
    if b is None:
        return 0
    sum = 0
    while b:
        sum += b.data
        b = b.next
    return sum

a = LinkedList()
for i in range(12):
    a.append(i)
a.printList()
print sumOfLastNNodes(a.head, 13)
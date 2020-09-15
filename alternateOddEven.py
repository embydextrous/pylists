from list import LinkedList
from list import Node

def alternateOddEven(l):
    even = []
    odd = []
    i = 0
    current = l.head
    while current:
        if i % 2 == 0 and current.data % 2 == 1:
            odd.append(current)
        if i % 2 == 1 and current.data % 2 == 0:
            even.append(current)
        i += 1
        current = current.next
    while len(odd) > 0 and len(even) > 0:
        a, b = odd.pop(), even.pop()
        a.data, b.data = b.data, a.data
    
l = LinkedList()
l.append(10)
l.append(2)
l.append(1)
l.append(5)
l.append(3)
l.append(6)
l.append(7)
l.append(8)
l.printList()
alternateOddEven(l)
l.printList()

        

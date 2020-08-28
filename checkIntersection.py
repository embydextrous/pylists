from list import Node
from list import LinkedList

def checkIntersection(a, b):
    if not a or not b:
        return
    lastA = a
    while lastA.next:
        lastA = lastA.next
    lastB = b
    while lastB.next:
        lastB = lastB.next
    return lastA == lastB

a = LinkedList()
b = LinkedList()

for i in range(8):
    a.append(i)

for j in range(8, 10):
    b.append(j)

b.head.next.next = a.head.next.next.next.next.next

a.printList()
b.printList()

print checkIntersection(a.head, b.head)
    
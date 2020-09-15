from list import LinkedList
from list import Node

def rotate(l, k):
    if k == 0:
        return
    current, prev = l.head, None
    while current and k > 0:
        prev = current
        current = current.next
        k -= 1
    if current:
        temp = l.head
        l.head = current
        prev.next = None
        lastNode = current
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = temp

a = LinkedList()
for i in range(1, 9):
    a.append(i)
a.printList()
rotate(a, 1)
a.printList()
    
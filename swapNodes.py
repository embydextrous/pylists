from list import Node
from list import LinkedList

# assuming valid nodes
def swapNodes(l, a, b):
    prevA, current = None, l.head
    while current:
        if current == a:
            break
        prevA, current = current, current.next

    prevB, current = None, l.head
    while current:
        if current == b:
            break
        prevB, current = current, current.next

    if prevA and prevB:
        prevA.next, prevB.next, a.next, b.next = b, a, b.next, a.next
    elif not prevA:
        l.head, prevB.next, a.next, b.next = b, a, b.next, a.next
    else:
        l.head, prevA.next, a.next, b.next = a, b, b.next, a.next

a = LinkedList()
for i in range(8):
    a.append(i)

a.printList()
swapNodes(a, a.head, a.head.next.next.next.next)
a.printList()
swapNodes(a, a.head.next.next.next, a.head)
a.printList()
swapNodes(a, a.head.next, a.head.next.next.next.next.next.next)
a.printList()



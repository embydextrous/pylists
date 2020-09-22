from list import LinkedList
from list import Node

def sort(a):
    if a is None or a.next is None:
        return
    lastNode = a
    while lastNode.next:
        lastNode = lastNode.next
    firstNonNegNode = None
    firstNegNode = None
    prev, current = None, a
    while current and current != firstNonNegNode:
        if current.data >= 0:
            if not firstNonNegNode:
                firstNonNegNode = current
            lastNode.next = current
            lastNode = lastNode.next
            next = current.next
            current.next = None
            if prev:
                prev.next = next
            current = next
        else:
            if not firstNegNode:
                firstNegNode = current
            prev, current = current, current.next
    if not firstNegNode:
        return firstNonNegNode
    else:
        if not firstNonNegNode:
            return reverse(firstNegNode)
        else:
            prev.next = None
            s = reverse(firstNegNode)
            firstNegNode.next = firstNonNegNode
            return s


def reverse(a):
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

a = LinkedList()
a.append(0)
a.append(-2)
a.append(-3)
a.append(4)
a.append(-5)
a.append(-6)
a.append(-8)
a.printList()
a.head = sort(a.head)
a.printList()
    

            

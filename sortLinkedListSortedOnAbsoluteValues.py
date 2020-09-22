from list import LinkedList
from list import Node

def sort(a):
    if a is None or a.next is None:
        return
    head = tail = Node('x')
    firstNonNegativeNode = None
    prevA = None
    while a:
        if a.data >= 0:
            if firstNonNegativeNode is None:
                firstNonNegativeNode = a
            prevA, a = a, a.next
        else:
            nodeToRemove = a
            if prevA:
                prevA.next = a.next
            a = a.next
            nodeToRemove.next = None
            tail.next = nodeToRemove
            tail = tail.next
    s = reverse(head.next)
    if s is None:
        return firstNonNegativeNode
    else:
       lastNode = s
       while lastNode.next:
           lastNode = lastNode.next
       lastNode.next = firstNonNegativeNode
    return s

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

a = LinkedList()
a.append(-1)
a.append(-2)
a.append(-3)
a.append(-4)
a.append(-5)
a.append(-6)
a.append(-8)
a.printList()
a.head = sort(a.head)
a.printList()
    

            

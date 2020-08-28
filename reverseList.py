from list import Node
from list import LinkedList

def reverse(a):
    prev, current = None, a.head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    a.head = prev

def reverseRecursive(a):
    a.head = reverseRecursiveUtil(a.head, None)

def reverseRecursiveUtil(node, prev):
    if node:
        next = node.next
        node.next = prev
        return reverseRecursiveUtil(next, node)
    else:
        return prev
    
    

a = LinkedList()
for i in range(8):
    a.append(i)
a.printList()
reverseRecursive(a)
a.printList()
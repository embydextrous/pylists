from list import LinkedList
from list import Node

def lengthOddOrEven(node):
    while node and node.next:
        node = node.next.next
    if not node:
        return "even"
    else:
        return "odd"

a = LinkedList()
for i in range(9):
    a.append(i)
print "Length of the linked list is " + lengthOddOrEven(a.head)

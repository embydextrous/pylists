from list import Node
from list import LinkedList

def pairwiseSwap(node):
    while node and node.next:
        node.data, node.next.data = node.next.data, node.data
        node = node.next.next

def pairwiseSwapUsingPointers(a):
    a.head = pairwiseSwapUsingPointersUtil(a.head) 

def pairwiseSwapUsingPointersUtil(node):
    toReturn = node
    if node and node.next:
        temp = node.next
        node.next = node.next.next
        temp.next = node
        toReturn = temp
        node.next = pairwiseSwapUsingPointersUtil(node.next)
    return toReturn


a = LinkedList()
for i in range(6):
    a.append(i)
a.printList()
pairwiseSwapUsingPointers(a)
a.printList()

a = LinkedList()
for i in range(7):
    a.append(i)
a.printList()
pairwiseSwapUsingPointers(a)
a.printList()
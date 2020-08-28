from list import Node
from list import LinkedList

def segregateEvenAndOdd(node):
    if node is None:
        return
    isHeadEven = node.data % 2 == 0
    lastNode = node
    while lastNode.next:
        lastNode = lastNode.next
    prev, node = node, node.next
    firstMovedNode = None
    while node and node != firstMovedNode:
        if (node.data % 2 == 0 and isHeadEven) or (node.data % 2 != 0 and not isHeadEven):
            prev, node = node, node.next
        else:   
            if not firstMovedNode:
                firstMovedNode = node             
            prev.next = node.next
            lastNode.next = node
            node.next = None
            lastNode = lastNode.next
            node = prev.next

 
a = LinkedList()
a.append(17)
a.append(15)
a.append(8)
a.append(12)
a.append(10)
a.append(5)
a.append(4)
a.append(1)
a.append(7)
a.append(6)

a.printList()
segregateEvenAndOdd(a.head)
a.printList()
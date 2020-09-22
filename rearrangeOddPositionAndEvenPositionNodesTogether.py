'''
Rearrange a linked list in such a way that all odd position nodes are together and all even positions node are together.

Examples:

Input:   1->2->3->4
Output:  1->3->2->4

Input:   10->22->30->43->56->70
Output:  10->30->56->22->43->70
'''
from list import LinkedList
from list import Node

def rearrange(a):
    if a is None or a.next is None or a.next.next is None:
        return
    lastNode = a
    while lastNode.next:
        lastNode = lastNode.next
    firstNodeToMove = a.next
    while a != firstNodeToMove:
        nodeToMove = a.next
        a.next = a.next.next
        nodeToMove.next = None
        lastNode.next = nodeToMove
        lastNode = lastNode.next
        a = a.next
        if a.next == firstNodeToMove:
            break

a = LinkedList()
for i in range(1, 6):
    a.append(i)
a.printList()
rearrange(a.head)
a.printList()
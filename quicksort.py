from list import LinkedList
from list import Node

def quickSort(node, lastNode):
    if node and node != lastNode:
        p = partition(node, lastNode)
        if p[0] and p[0] != node:
            quickSort(node, p[0])
        if p[1] and p[1] != lastNode:
            quickSort(p[1], lastNode)


def partition(startNode, endNode):
    i = None
    j = startNode
    while j != endNode:
        if j.data <= endNode.data:
            if i is None:
                i = startNode
            else:
                i = i.next
            i.data, j.data = j.data, i.data
        j = j.next
    if i:
        i.next.data, endNode.data = endNode.data, i.next.data
    else:
        startNode.data, endNode.data = endNode.data, startNode.data
    if i:
        if i.next == endNode:
            return (i, None)
        else:
            return (i, i.next.next)
    else:
        return (None, startNode.next)

a = LinkedList()
s = [10, 8, 2, 1, 4, 7, 9, 8, 5, 6]
for i in s:
    a.append(i)
a.printList()
lastNode = a.head
while lastNode.next:
    lastNode = lastNode.next
quickSort(a.head, lastNode)
a.printList()
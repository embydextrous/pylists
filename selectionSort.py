from list import LinkedList
from list import Node


def selectionSort(l):
    node = l.head
    prev = None
    while node:
        x = findMinNode(node)
        minNode, prevMinNode = x[0], x[1]
        if node != minNode:
            if prev:
                prevMinNode.next = minNode.next
                prev.next = node.next
                node.next = prevMinNode.next
                minNode.next = prev.next
                prevMinNode.next = node
                prev.next = minNode
            else:
                prevMinNode.next = minNode.next
                l.head = node.next
                node.next = prevMinNode.next
                minNode.next = l.head
                prevMinNode.next = node
                l.head = minNode
        prev, node = minNode, minNode.next

def findMinNode(node):
    minNode, prevMinNode = node, None
    prev = None
    while node:
        if node.data < minNode.data:
            prevMinNode, minNode = prev, node
        prev, node = node, node.next
    return (minNode, prevMinNode)

l = LinkedList()
a = [10, 12, 8, 4, 6]
for i in a:
    l.append(i)
l.printList()
selectionSort(l)
l.printList()
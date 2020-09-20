from list import LinkedList
from list import Node

def sort(l):
    a = LinkedList()
    node = l.head
    while node:
        temp = node.next
        node.next = None
        sortedInsert(a, node)
        node = temp
    l.head = a.head

def sortedInsert(l, node):
    if l.head is None:
        l.head = node
        return
    prev, current = None, l.head
    while current:
        if current.data > node.data:
            break
        prev, current = current, current.next
    if prev is None:
        node.next = l.head
        l.head = node
    else:
        node.next = current
        prev.next = node

l = LinkedList()
a = [4, 1, 7, 6, 2, 3, 9, 8, 0]
for i in a:
    l.append(i)
l.printList()
sort(l)
l.printList()

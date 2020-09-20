from list import LinkedList
from list import Node

def mergeSort(l):
    if l is None or l.next is None:
        return l
    middle = findMiddle(l)
    nextToMiddle = middle.next
    middle.next = None
    left = mergeSort(l)
    right = mergeSort(nextToMiddle)
    return merge(left, right)

def findMiddle(node):
    fast, slow, slowPrev = node, node, None
    while fast and fast.next:
        fast, slow, slowPrev = fast.next.next, slow.next, slow
    return slowPrev

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        mergedHead = a
        a = a.next
    else:
        mergedHead = b
        b = b.next
    mergedTail = mergedHead
    while a and b:
        if a.data <= b.data:
            mergedTail.next = a
            a = a.next
        else:
            mergedTail.next = b
            b = b.next
        mergedTail = mergedTail.next
    if a:
        mergedTail.next = a
    if b:
        mergedTail.next = b
    return mergedHead

a = [4, 3, 1, 2, 8, 7, 6, 1, 4, 9, 3, 4, 5, 2, 1]
l = LinkedList()
for i in a:
    l.append(i)
l.head = mergeSort(l.head)
l.printList()

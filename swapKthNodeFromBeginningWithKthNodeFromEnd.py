from list import LinkedList
from list import Node

def swap(head, k):
    newHead = head
    if head is None or head.next is None or k <= 0:
        return newHead
    i, j = head, head
    prevI, prevJ = None, None
    while j and k > 1:
        prevJ, j = j, j.next
        k -= 1
    if j is None:
        return newHead
    kthFromBegin, kthFromEnd = j, i
    while j.next:
        prevI, kthFromEnd = kthFromEnd, kthFromEnd.next
        j = j.next
    if kthFromBegin == kthFromEnd:
        return newHead
    if prevI is None:
        newHead = kthFromBegin
        prevJ.next = kthFromEnd
    elif prevJ is None:
        newHead = kthFromEnd
        prevI.next = kthFromBegin
    else:
        prevI.next = kthFromBegin
        prevJ.next = kthFromEnd
    kthFromBegin.next, kthFromEnd.next = kthFromEnd.next, kthFromBegin.next
    return newHead

a = LinkedList()
for i in range(1, 9):
    a.append(i)
a.printList()
a.head = swap(a.head, 1)
a.printList()
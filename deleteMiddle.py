from list import LinkedList
from list import Node

def deleteMiddle(l):
    if l.head is None:
        return
    if l.head.next is None:
        l.head = None
        return
    fast = slow = l.head
    prev = None
    while fast and fast.next:
        fast, prev, slow = fast.next.next, slow, slow.next
    prev.next = slow.next
    slow.next = None
    slow = None

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.printList()
deleteMiddle(a)
a.printList()
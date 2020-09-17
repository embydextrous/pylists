from list import LinkedList
from list import Node

def makeMiddleHead(l):
    fast, slow, prev = l.head, l.head, None
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if prev:
        prev.next = slow.next
        slow.next = l.head
        l.head = slow

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.printList()
makeMiddleHead(a)
a.printList()

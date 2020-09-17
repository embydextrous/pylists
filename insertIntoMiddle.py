from list import LinkedList
from list import Node

def insertIntoMiddle(l, newNode):
    if l.head is None:
        l.head = newNode
        return
    fast, slow, prev = l.head, l.head, None
    while fast and fast.next:
        fast = fast.next.next
        prev, slow = slow, slow.next
    if fast is None:
        newNode.next = slow
        prev.next = newNode
    else:
        newNode.next = slow.next
        slow.next = newNode

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.printList()
insertIntoMiddle(a, Node(10))
a.printList()
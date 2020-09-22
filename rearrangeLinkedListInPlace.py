from list import LinkedList
from list import Node

def rearrange(a):
    if a is None or a.next is None:
        return a
    mid = findMid(a)
    nextMid = mid.next
    mid.next = None
    first = a
    second = reverse(nextMid)
    return merge(a, second)

def findMid(node):
    fast, prevSlow, slow = node, None, node
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    if fast:
        return slow
    return prevSlow

def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    head = tail = Node('*')
    while a and b:
        tail.next = a
        tail = tail.next
        a = a.next
        tail.next = b
        tail = tail.next
        b = b.next
    if a:
        tail.next = a
    return head.next

a = LinkedList()
for i in range(12):
    a.append(i)
a.printList()
a.head = rearrange(a.head)
a.printList()
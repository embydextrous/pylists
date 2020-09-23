from list import Node
from list import LinkedList

def rearrange(a):
    a = mergeSort(a)
    if a is None or a.next is None or a.next.next is None:
        return a
    mid = findMid(a)
    midNext = mid.next
    mid.next = None
    left = a
    right = reverse(midNext)
    return mergeAlternate(left, right)

def findMid(a):
    slow, fast = a, a
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def findPrevMid(a):
    slow, fast, prevSlow = a, a, None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    return prevSlow

def mergeSort(a):
    if a is None or a.next is None:
        return a
    prevMid = findPrevMid(a)
    mid = prevMid.next
    prevMid.next = None
    left = mergeSort(a)
    right = mergeSort(mid)
    return mergeSorted(left, right)

def mergeSorted(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        head = a
        a = a.next
    else:
        head = b
        b = b.next
    tail = head
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head

def reverse(a):
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def mergeAlternate(a, b):
    head = tail = Node('x')
    while a and b:
        tail.next = a
        tail = tail.next
        a = a.next
        tail.next = b
        tail = tail.next
        b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next

a = LinkedList()
s = [10, 4, 7, 1, 3, 8, 9, 2, 0, 5, 6]
for i in s:
    a.append(i)
a.printList()
a.head = rearrange(a.head)
a.printList()
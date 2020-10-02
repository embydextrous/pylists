from dll import DLL
from dll import Node

def mergeSort(a):
    if a is None or a.next is None:
        return a
    mid = findMid(a)
    mid.prev.next = None
    mid.prev = None
    left = mergeSort(a)
    right = mergeSort(mid)
    return merge(left, right)

def findMid(a):
    fast, slow = a, a
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def merge(a, b):
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
        tail.next.prev = tail
        tail = tail.next
    if a:
        tail.next = a
        tail.next.prev = tail
    if b:
        tail.next = b
        tail.next.prev = tail
    return head

a = DLL()
b = DLL()
s = [1, 3, 5, 7]
for i in s:
    a.append(i)
    b.append(i+1)
a.printList()
b.printList()
c = DLL()
c.head = merge(a.head, b.head)
c.printList()
current = c.head
while current:
    if current.prev:
        print current.prev.data,
    print current.data,
    if current.next:
        print current.next.data,
    print
    current = current.next

q = [2, 1, 5, 3, 8, 9, 7, 6, 4]
d = DLL()
for i in q:
    d.append(i)
d.printList()
d.head = mergeSort(d.head)
d.printList()
    

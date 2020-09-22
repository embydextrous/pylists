from list import LinkedList
from list import Node

def countPairsWithSumX(a, b, x):
    a = mergeSortAsc(a)
    b = mergeSortDesc(b)
    count = 0
    while a and b:
        if a.data + b.data == x:
            count += 1
            a, b = a.next, b.next
        elif a.data + b.data < x:
            a = a.next
        else:
            b = b.next
    return count

def mergeSortAsc(a):
    if a is None or a.next is None:
        return a
    mid = findMid(a)
    nextMid = mid.next
    mid.next = None
    left = mergeSortAsc(a)
    right = mergeSortAsc(nextMid)
    return mergeAsc(left, right)

def mergeAsc(a, b):
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

def mergeSortDesc(a):
    if a is None or a.next is None:
        return a
    mid = findMid(a)
    nextMid = mid.next
    mid.next = None
    left = mergeSortDesc(a)
    right = mergeSortDesc(nextMid)
    return mergeDesc(left, right)

def mergeDesc(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data >= b.data:
        head = a
        a = a.next
    else:
        head = b
        b = b.next
    tail = head
    while a and b:
        if a.data >= b.data:
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

def findMid(a):
    prevSlow, slow, fast = None, a, a
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    return prevSlow

a = [4, 3, 5, 7, 11, 2, 1]
l1 = LinkedList()
for i in a:
    l1.append(i)
l1.printList()

a = [2, 3, 4, 5, 6, 8, 12]
l2 = LinkedList()
for i in a:
    l2.append(i)
l2.printList()

print countPairsWithSumX(l1.head, l2.head, 9)
from list import LinkedList
from list import Node

def mergeSortAsc(a):
    if a is None or a.next is None:
        return a
    middle = findMiddle(a)
    nextToMiddle = middle.next
    middle.next = None
    left = mergeSortAsc(a)
    right = mergeSortAsc(nextToMiddle)
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
    else:
        tail.next = b
    return head

def mergeSortDesc(a):
    if a is None or a.next is None:
        return a
    middle = findMiddle(a)
    nextToMiddle = middle.next
    middle.next = None
    left = mergeSortDesc(a)
    right = mergeSortDesc(nextToMiddle)
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
    else:
        tail.next = b
    return head

def findMiddle(node):
    prevMiddle, slow, fast = None, node, node
    while fast and fast.next:
        fast = fast.next.next
        prevMiddle, slow = slow, slow.next
    return prevMiddle

def findTriplet(a, b, c, x):
    b.head = mergeSortAsc(b.head)
    c.head = mergeSortDesc(c.head)
    i = a.head
    while i:
        j, k = b.head, c.head
        while j and k:
            if i.data + j.data + k.data == x:
                return (i.data, j.data, k.data)
            elif i.data + j.data + k.data < x:
                j = j.next
            else:
                k = k.next
        i = i.next

a = LinkedList()
b = LinkedList()
c = LinkedList()
for i in range(1, 9):
    a.append(i)
s = [2, 4, 1, 7, 9, 1, 0, 6]
for i in s:
    b.append(i)
s = [8, 3, 12, 9, 11, 10, 1, 5]
for i in s:
    c.append(i)
print findTriplet(a, b, c, 29)




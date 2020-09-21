from list import LinkedList
from list import Node

def intersection(a, b):
    a = mergeSort(a)
    b = mergeSort(b)
    head = tail = Node('x')
    while a and b:
        if a.data == b.data:
            tail.next = Node(a.data)
            tail = tail.next
            a, b = a.next, b.next
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    return head.next

def union(a, b):
    a = mergeSort(a)
    b = mergeSort(b)
    head = tail = Node('x')
    while a and b:
        if a.data == b.data:
            tail.next = Node(a.data)
            tail = tail.next
            a, b = a.next, b.next
        elif a.data < b.data:
            tail.next = Node(a.data)
            tail = tail.next
            a = a.next
        else:
            tail.next = Node(b.data)
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next
           
def mergeSort(a):
    if a is None or a.next is None:
        return a
    mid = findMid(a)
    midNext = mid.next
    mid.next = None
    left = mergeSort(a)
    right = mergeSort(midNext)
    return merge(left, right)

def findMid(a):
    fast = slow = a
    prevSlow = None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    return prevSlow

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
        tail = tail.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head

a = LinkedList()
a.append(10)
a.append(15)
a.append(4)
a.append(20)    
a.printList()
b = LinkedList()
b.append(8)
b.append(4)
b.append(2)
b.append(10)
b.printList()
a.printList()
#intersect = LinkedList()
#intersect.head = intersection(a.head, b.head)
#intersect.printList()
un = LinkedList()
un.head = union(a.head, b.head)
un.printList()
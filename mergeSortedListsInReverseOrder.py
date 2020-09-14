'''
Given two linked lists sorted in increasing order. Merge them such a way that the result list 
is in decreasing order (reverse order).

Examples:

Input:  a: 5->10->15->40
        b: 2->3->20 
Output: res: 40->20->15->10->5->3->2

Input:  a: NULL
        b: 2->3->20 
Output: res: 20->3->2
'''

from list import LinkedList
from list import Node

def merge(a, b):
    l = LinkedList()
    while a and b:
        if a.data <= b.data:
            temp = a.next
            a.next = l.head
            l.head = a
            a = temp
        else:
            temp = b.next
            b.next = l.head
            l.head = b
            b = temp
    while a:
        temp = a.next
        a.next = l.head
        l.head = a
        a = temp
    while b:
        temp = b.next
        b.next = l.head
        l.head = b
        b = temp
    return l

a = LinkedList()
for i in range(8):
    a.append(i)
a.printList()

b = LinkedList()
for i in range(2, 7):
    b.append(i*2)
b.printList()

merge(a.head, b.head).printList()







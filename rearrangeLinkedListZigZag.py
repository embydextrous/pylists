'''
Given a linked list, rearrange it such that converted list should be of the form a < b > c < d > e < f ..
 where a, b, c.. are consecutive data node of the linked list.

Examples:

Input:  1->2->3->4
Output: 1->3->2->4 

Input:  11->15->20->5->10
Output: 11->20->5->15->10
'''
from list import LinkedList
from list import Node

def rearrange(a):
    asc = True
    while a and a.next:
        if (not asc and a.data < a.next.data) or (asc and a.data > a.next.data):
            a.data, a.next.data = a.next.data, a.data
        asc = not asc
        a = a.next
    

a = LinkedList()
for i in range(1, 5):
    a.append(i)
a.printList()
rearrange(a.head)
a.printList()

b = LinkedList()
s = [11, 15, 20, 5, 10]
for i in s:
    b.append(i)
b.printList()
rearrange(b.head)
b.printList()
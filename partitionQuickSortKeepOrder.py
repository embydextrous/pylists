'''
Given a linked list and a value x, partition it such that all nodes less than x come first, 
then all nodes with value equal to x and finally nodes with value greater than or equal to x. 
The original relative order of the nodes in each of the three partitions should be preserved. 
The partition must work in-place.

Examples:

Input : 1->4->3->2->5->2->3, 
        x = 3
Output: 1->2->2->3->3->4->5

Input : 1->4->2->10 
        x = 3
Output: 1->2->4->10

Input : 10->4->20->10->3 
        x = 3
Output: 3->10->4->20->10 
'''
from list import LinkedList
from list import Node

def partition(a, x):
    headl = taill = Node('x')
    heade = taile = Node('x')
    headg = tailg = Node('x')
    while a:
        nextA = a.next
        if a.data < x:
            taill.next = a
            taill = taill.next
        elif a.data == x:
            taile.next = a
            taile = taile.next
        else:
            tailg.next = a
            tailg = tailg.next
        a.next = None
        a = nextA
    headl = headl.next
    headg = headg.next
    heade = heade.next
    if headl:
        if heade:
            taill.next = heade
        else:
            taill.next = headg
    if heade:
        taile.next = headg
    head = headl if headl else heade if heade else headg
    return head

a = LinkedList()
s = [1, 4, 3, 2, 5, 2, 3]
for i in s:
    a.append(i)
a.printList()
a.head = partition(a.head, 3)
a.printList()
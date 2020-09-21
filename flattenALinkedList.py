'''
Given a linked list where every node represents a linked list and contains two pointers of its type:
(i) Pointer to next node in the main list (we call it 'right' pointer in below code)
(ii) Pointer to a linked list where this node is head (we call it 'down' pointer in below code).
All linked lists are sorted. See the following example

       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45

Write a function flatten() to flatten the lists into a single linked list. 
The flattened linked list should also be sorted. 
For example, for the above input list, output list should be 5->7->8->10->19->20->22->28->30->35->40->45->50.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None

def flatten(a):
    if a is None or a.next is None:
        return a
    while a.next:
        temp = a.next.next
        a = merge(a, a.next)
        a.next = temp
    return a

def merge(a, b):
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        head = a
        a = a.down
    else:
        head = b
        b = b.down
    tail = head
    while a and b:
        if a.data <= b.data:
            tail.down = a
            a = a.down
        else:
            tail.down = b
            b = b.down
        tail = tail.down
    if a:
        tail.down = a
    if b:
        tail.down = b
    return head

def printList(a):
    print "head ->",
    while a:
        print str(a.data),
        print "->",
        a = a.down
    print "null"

a = Node(5)
a.next = Node(10)
a.next.next = Node(19)
a.next.next.next = Node(28)
a.down = Node(7)
a.down.down = Node(8)
a.down.down.down = Node(30)
a.next.down = Node(20)
a.next.next.down = Node(22)
a.next.next.down.down = Node(50)
a.next.next.next.down = Node(35)
a.next.next.next.down.down = Node(40)
a.next.next.next.down.down.down = Node(45)

a = flatten(a)
printList(a)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def pointToNextGreater(node):
    d = {}
    origHead = node
    while node:
        d[node] = node.next
        node = node.next
    head = mergeSort(origHead)
    while head:
        head.next, head.random = d[head], head.next
        head = head.random
        

def mergeSort(node):
    if node is None or node.next is None:
        return node
    middle = findMiddle(node)
    nextToMiddle = middle.next
    middle.next = None
    left = mergeSort(node)
    right = mergeSort(nextToMiddle)
    return merge(left, right)

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

def findMiddle(node):
    slow, fast, prevSlow = node, node, None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    return prevSlow

def printList(node):
    print "head ->",
    while node:
        print str(node.data), "->",
        node = node.next
    print "null"

a = Node(5)
a.next = Node(10)
a.next.next = Node(2)
a.next.next.next = Node(3)

printList(a)
pointToNextGreater(a)
printList(a)
while a:
    print a.data,  "->",
    if a.random:
        print a.random.data
    else:
        print None
    a = a.next


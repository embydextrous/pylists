from list import LinkedList
from list import Node

def detectAndRemoveLoop(a):
    l = loopNode(a)
    if not l:
        print "Loop not found"
        return
    prevL = None
    while True:
        if a == l:
            break
        a, l , prevL = a.next, l.next, l
    print "Loop begins at:", l.data
    prevL.next = None

def loopNode(a):
    fast, slow = a, a
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return fast
    return None
    
a = LinkedList()
for i in range(10):
    a.append(i)
a.printList()   
detectAndRemoveLoop(a.head)
lastNode = a.head
while lastNode.next:
    lastNode = lastNode.next
lastNode.next = a.head.next.next.next.next.next
detectAndRemoveLoop(a.head)
a.printList()
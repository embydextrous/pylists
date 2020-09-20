from list import LinkedList
from list import Node

def removeAllOccurences(l):
    if l.head is None:
        return
    left, right, prevLeft, prevRight = l.head, l.head.next, None, l.head
    while left and right:
        while right and left.data == right.data:
            prevRight, right = right, right.next
        if right is None:
            if prevLeft is None:
                l.head = None
            else:
                prevLeft.next = None
            print "case1", 
            l.printList()
        elif left != prevRight and left.data == prevRight.data:
            if prevLeft is None:
                l.head = right
            else:
                prevLeft.next = right
            left, prevRight, right = right, right, right.next
            print "case2", 
            l.printList()
        else:
            prevLeft, left, prevRight, right = left, left.next, right, right.next
            print "case3", 
            l.printList()
        

l = LinkedList()
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(1)
l.append(2)
l.append(2)

l.printList()
removeAllOccurences(l)
l.printList()

    

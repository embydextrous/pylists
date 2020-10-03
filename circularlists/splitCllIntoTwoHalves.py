from circularlist import CircularLinkedList
from circularlist import Node

def split(cll):
    resultCll = CircularLinkedList()
    if cll.tail is None:
        return (cll, resultCll)
    if cll.tail == cll.tail.next:
        return (cll, resultCll)
    mid = findMid(cll.tail.next)
    midNext = mid.next
    mid.next = cll.tail.next
    cll.tail.next = midNext
    resultCll.tail = cll.tail
    cll.tail = mid
    return (cll, resultCll)


def findMid(node):
    fast, slow = node, node
    prevSlow = None
    while True:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
        if fast == node or fast.next == node:
            break
    if fast == node:
        return prevSlow
    return slow

cll = CircularLinkedList()
for i in range(11):
    cll.append(i)
cll.printList()
result = split(cll)
result[0].printList()
result[1].printList()

    
    
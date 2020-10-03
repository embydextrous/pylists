from list import LinkedList
from list import Node

def isCircular(head):
    if head is None:
        return True
    current = head
    loopNode = findLoopNode(head)
    if loopNode:
        while current:
            if current.next == head:
                return True
            if current.next == loopNode:
                return False
            current = current.next
    return False

def findLoopNode(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return slow
    return None

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.head.next.next.next.next.next = a.head
print isCircular(a.head)
from list import LinkedList
from list import Node

# Assuming linked list has loop
def checkIfPalindrome(a):
    if a is None:
        return True
    head = a
    loopNode = findLoopNode(a)
    lastNode = loopNode
    while lastNode.next != a.next:
        a = a.next
        lastNode = lastNode.next
    firstLoopNode = a.next
    lastNode.next = None
    if head.next is None:
        head.next = head
        return True
    mid = findMid(head)
    midNext = mid.next
    mid.next = None
    left = head
    headRight = right = reverse(midNext)
    result = True
    while left and right:
        if left.data != right.data:
            result = False
        if right.next is None:
            break
        left, right = left.next, right.next
    right = reverse(headRight)
    mid.next = right
    lastNode.next = firstLoopNode
    return result

def reverse(a):
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev

def findMid(a):
    fast, slow, prevSlow = a, a, None
    while fast and fast.next:
        fast = fast.next.next
        prevSlow, slow = slow, slow.next
    if fast:
        return slow
    return prevSlow

def findLoopNode(a):
    fast, slow = a, a
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return slow
    return None

def printList(a):
    fast, slow = a, a
    loopNode = None
    while fast and fast.next:
        print slow.data,
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            loopNode = slow
            break
    if not loopNode:
        while slow:
            print slow.data,
            slow = slow.next
    else:
        while a != loopNode:
            print loopNode.data,
            a, loopNode = a.next, loopNode.next

a = LinkedList()
a.head = Node(1)
a.head.next = Node(2)
a.head.next.next = Node(3)
a.head.next.next.next = Node(2)
a.head.next.next.next.next = Node(1)
a.head.next.next.next.next.next = a.head.next.next
printList(a.head)
print checkIfPalindrome(a.head)
printList(a.head)
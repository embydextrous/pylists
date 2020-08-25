from list import Node
from list import LinkedList

def findMiddle(node):
    fast, slow = node, node
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    if slow:
        return slow.data
    else:
        return -1

a = LinkedList()
for i in range(1, 8):
    a.append(i)
print findMiddle(a.head)
    
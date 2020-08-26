from list import Node
from list import LinkedList

def isLoop(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

a = LinkedList()
a.push(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.printList()
print isLoop(a.head)
a.head.next.next.next.next.next = a.head.next.next.next

print isLoop(a.head)


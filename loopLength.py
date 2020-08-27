from list import Node
from list import LinkedList

def loopLength(node):
    fast, slow = node, node
    isLoop = False
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            isLoop = True
            break
    count = 0
    if isLoop:
        while True:
            count += 1
            slow = slow.next
            if fast == slow:
                break
    return count

a = LinkedList()
a.push(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.printList()
print loopLength(a.head)
a.head.next.next.next.next.next = a.head.next.next.next

print loopLength(a.head)


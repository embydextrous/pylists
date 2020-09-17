from list import LinkedList
from list import Node

def countRotationInSortedList(node):
    count = 0
    while node.next:
        count += 1
        if node.data > node.next.data:
            break
        node = node.next
    if node.next is None:
        return 0
    return count

a = LinkedList()
for i in range(9):
    a.append((i+2) % 9)
a.printList()
print countRotationInSortedList(a.head)

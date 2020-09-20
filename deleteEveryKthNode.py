from list import LinkedList
from list import Node

def deleteKthNode(l, k):
    if k == 1:
        l.head = None
        return
    prev, current = None, l.head
    count = k
    while current and count > 0:
        count -= 1
        if count == 0:
            prev.next = current.next
            current.next = None
            current = prev.next
            count = k
        else:
            prev, current = current, current.next

a = LinkedList()
for i in range(1, 13):
    a.append(i)
a.printList()
deleteKthNode(a, 3)
a.printList()


    
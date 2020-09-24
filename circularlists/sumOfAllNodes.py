from circularlist import CircularLinkedList
from circularlist import Node

def sum(tail):
    if tail is None:
        return 0
    if tail.next == tail:
        return tail.data
    current = tail.next
    result = 0
    while current != tail:
        result += current.data
        current = current.next
    result += tail.data
    return result

c = CircularLinkedList()
c.push(4)
c.append(6)
c.push(1)
c.push(3)
c.push(5)
c.append(8)
c.printList()
print sum(c.tail)

from circularlist import CircularLinkedList
from circularlist import Node
import math

def josepheusCircle(c):
    if c.tail is None:
        return None
    if c.tail.next == c.tail:
        return c.tail.data
    current = c.tail.next
    while current != current.next:
        next = current.next
        current.next = next.next
        next.next = None
        if next == c.tail:
            c.tail = current
        current = current.next
    return current.data

def josepheusCircleDirect(n):
    if n <= 0:
        return None
    return 2 * (n - 2 ** int(math.log(n, 2))) + 1

def josepheusCircleBitwise(n):
    if n <= 0:
        return None
    i = 1
    while True:
        if i == n or i * 2 > n:
            break
        i *= 2
    return 2 * (n - i) + 1


c = CircularLinkedList()
for i in range(1, 101):
    c.append(i)
c.printList()
print josepheusCircle(c)
print josepheusCircleDirect(100)
print josepheusCircleBitwise(100)
from list import LinkedList
from list import Node

def add(a, b):
    l1 = a.size()
    l2 = b.size()
    p = a.head if l1 > l2 else b.head
    q = a.head if l1 <= l2 else b.head
    d = abs(l1 - l2)
    s = []
    while d > 0:
        s.append([p.data, 0])
        p = p.next
        d -= 1
    while p and q:
        s.append([(p.data + q.data) % 10, (p.data + q.data) / 10])
        p = p.next
        q = q.next
    l = LinkedList()
    carry = 0
    while len(s) > 0:
        node = s.pop()
        l.push((node[0] + carry) % 10)
        carry = node[1] + (node[0] + carry) / 10
    if carry > 0:
        l.push(carry)
    return l

n1 = LinkedList()
s1 = "1999"
s2 = "1001"
for i in s1:
    n1.append(int(i))
n1.printList()
n2 = LinkedList()
for i in s2:
    n2.append(int(i))
n2.printList()
add(n1, n2).printList()
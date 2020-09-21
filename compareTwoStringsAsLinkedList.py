from list import LinkedList
from list import Node

def strCompare(a, b):
    if not a and not b:
        return 0
    if not a:
        return -1
    if not b:
        return 1
    if a.data != b.data:
        return sgn(ord(a.data), ord(b.data))
    return strCompare(a.next, b.next)

def sgn(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    return 0

a = LinkedList()
b = LinkedList()
s1 = "Archit"
s2 = "Arpit"

for i in s1:
    a.append(i)
for i in s2:
    b.append(i)

print strCompare(a.head, b.head)
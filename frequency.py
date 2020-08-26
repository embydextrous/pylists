from list import Node
from list import LinkedList

def frequency(node, k):
    count = 0
    while node:
        if node.data == k:
            count += 1
        node = node.next
    return count

a = LinkedList()
a.append(0)
a.push(1)
a.append(1)
a.push(2)
a.append(3)
a.push(2)
a.append(4)
a.push(2)
a.append(2)
a.push(0)
a.printList()
for i in range(0, 6):
    print frequency(a.head, i)

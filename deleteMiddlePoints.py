from list import LinkedList
from list import Node

def deleteMiddlePoints(node):
    while node and node.next and node.next.next:
        if node.data[0] == node.next.data[0] and node.data[0] == node.next.next.data[0]:
            node.next = node.next.next
            continue
        if node.data[1] == node.next.data[1] and node.data[1] == node.next.next.data[1]:
            node.next = node.next.next
            continue
        node = node.next

a = LinkedList()
a.append([0, 10])
a.append([1, 10])
a.append([5, 10])
a.append([7, 10])
a.append([7, 5])
a.append([20, 5])
a.append([40, 5])
a.printList()
deleteMiddlePoints(a.head)
a.printList()

b = LinkedList()
b.append([2, 3])
b.append([5, 3])
b.append([7, 3])
b.append([10, 3])
b.append([12, 3])
b.printList()
deleteMiddlePoints(b.head)
b.printList()

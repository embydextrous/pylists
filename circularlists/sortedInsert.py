from circularlist import CircularLinkedList
from circularlist import Node

def insertSorted(cll, key):
    newNode = Node(key)
    if cll.tail is None:
        cll.tail = newNode
        return
    if cll.tail.data <= newNode.data:
        newNode.next = cll.tail.next
        cll.tail.next = newNode
        cll.tail = newNode
        return
    if cll.tail.next.data > newNode.data:
        newNode.next = cll.tail.next
        cll.tail.next = newNode
        return
    head = cll.tail.next
    while head != cll.tail:
        if head.next.data > newNode.data:
            break
        head = head.next
    newNode.next = head.next
    head.next = newNode

cll = CircularLinkedList()
s = [3, 6, 8, 10]
for i in s:
    cll.append(i)
cll.printList()
insertSorted(cll, 2)
cll.printList()
insertSorted(cll, 2)
cll.printList()
insertSorted(cll, 11)
cll.printList()
insertSorted(cll, 11)
cll.printList()
insertSorted(cll, 5)
cll.printList()
from list import Node
from list import LinkedList

def moveLastToFront(a):
    if a.head is None or a.head.next is None:
        return
    secondLast, last = None, a.head
    while last and last.next:
        secondLast, last = last, last.next
    secondLast.next = None
    last.next = a.head
    a.head = last

def moveFrontToLast(a):
    if a.head is None or a.head.next is None:
        return
    last = a.head
    while last and last.next:
        last = last.next
    last.next = a.head
    a.head = a.head.next
    last.next.next = None


a = LinkedList()
a.printList()
moveLastToFront(a)
a.printList()
a.append(1)
a.printList()
moveLastToFront(a)
a.printList()
a.append(2)
a.printList()
moveLastToFront(a)
a.printList()
a.append(3)
a.printList()
moveLastToFront(a)
a.printList()

a = LinkedList()
a.printList()
moveFrontToLast(a)
a.printList()
a.append(1)
a.printList()
moveFrontToLast(a)
a.printList()
a.append(2)
a.printList()
moveFrontToLast(a)
a.printList()
a.append(3)
a.printList()
moveFrontToLast(a)
a.printList()

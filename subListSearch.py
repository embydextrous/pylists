from list import LinkedList
from list import Node

def subListSearch(a, b):
    if b is None:
        return True
    while a:
        currentA, currentB = a, b
        while currentA and currentB:
            if currentA.data != currentB.data:
                break
            currentA, currentB = currentA.next, currentB.next
            if not currentB:
                return True
        if currentA is None:
            return False
        a = a.next
    return False

a = LinkedList()
for i in range(1, 9):
    a.append(i)
a.printList()

b = LinkedList()
b.append(4)
b.printList()

print subListSearch(a.head, b.head)




from list import Node
from list import LinkedList

def isPalindrome(node):
    s = []
    current = node
    while current:
        s.append(current.data)
        current = current.next
    current = node
    while current:
        if current.data != s.pop():
            return False
        current = current.next
    return True

a = LinkedList()
a.printList()
print isPalindrome(a.head)
a.append(1)
a.printList()
print isPalindrome(a.head)
a.append(2)
a.append(1)
a.printList()
print isPalindrome(a.head)
a.append(2)
a.append(1)
a.printList()
print isPalindrome(a.head)
a.append(5)
a.printList()
print isPalindrome(a.head)
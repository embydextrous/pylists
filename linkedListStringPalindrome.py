from list import LinkedList
from list import Node

def isPalindrome(node):
    s = ""
    while node:
        s += node.data
        node = node.next
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

a = LinkedList()
a.append("A")


a.printList()
print isPalindrome(a.head)

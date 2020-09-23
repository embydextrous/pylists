from list import LinkedList
from list import Node

def countCommon(a, b):
    count = 0
    while a and b:
        if a.data == b.data:
            count += 1
            a, b = a.next, b.next
        else:
            break
    return count

def longestPalindrome(a):
    result = 0
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        result = max(result, 2 * countCommon(next, prev) + 1)
        result = max(result, 2 * countCommon(current, prev))
        prev, current = current, next
    reverse(prev)
    return result

def reverse(a):
    prev, current = None, a
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next

s = [2, 3, 7, 3, 2, 12, 24]
a = LinkedList()
for i in s:
    a.append(i)
a.printList()
print longestPalindrome(a.head)
a.printList()
        
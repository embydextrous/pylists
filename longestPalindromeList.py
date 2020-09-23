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
        result = max(result, 2 * countCommon(prev, next) + 1)
        result = max(result, 2 * countCommon(current, next))
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

def countCommon(s, i, j, n):
    count = 0
    while i >= 0 and j < n:
        if s[i] == s[j]:
            count += 1
            j += 1
            i -= 1
        else:
            break
    return count

def longestPalindromeString(s):
    n = len(s)
    result = 0
    for i in range(n):
        result = max(result, 2 * countCommon(s, i - 1, i + 1, n) + 1)
        result = max(result, 2 * countCommon(s, i, i + 1, n))
    return result

s = "abcbade"
print longestPalindromeString(s)
        
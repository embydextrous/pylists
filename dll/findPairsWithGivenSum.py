from dll import DLL
from dll import Node

def findPairsWithSumX(head, tail, x):
    result = []
    if head is None or tail is None:
        return result
    while head != tail and tail.next != head:
        if head.data + tail.data == x:
            result.append((head.data, tail.data)
            head, tail = head.next, tail.prev
        elif head.data + tail.data < x:
            head = head.next
        else:
            tail = tail.prev
    return result

s = [1, 2, 4, 5, 6, 8, 9]
dll = DLL()
for i in s:
    dll.append(i)
dll.printList()
print findPairsWithSumX(dll.head, dll.tail, 7)
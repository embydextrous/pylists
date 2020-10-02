from dll import DLL
from dll import Node

def findTripletsWithSumX(head, tail, x):
    if head is None or head.next is None or head.next.next is None:
        return []
    result = []
    while head != tail:
        result += findPairsWithSumX(head.next, tail, x, head.data)
        head = head.next
    return result


def findPairsWithSumX(head, tail, x, key):
    if head == tail:
        return []
    result = []
    while head != tail and tail.next != head:
        if head.data + tail.data + key == x:
            result.append((key, head.data, tail.data))
            head, tail = head.next, tail.prev
        elif head.data + tail.data + key < x:
            head = head.next
        else:
            tail = tail.prev
    return result

s = [1, 2, 4, 5, 6, 8, 9]
dll = DLL()
for i in s:
    dll.append(i)
dll.printList()
print findTripletsWithSumX(dll.head, dll.tail, 15)
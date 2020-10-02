from dll import DLL
from dll import Node

def quickSort(dll, l, r):
    if not l or not r:
        return
    if l == r or r == l.prev:
        return
    p = lomutoPartition(dll, l, r)
    quickSort(dll, l, p.prev)
    quickSort(dll, p.next, r)

def hoarePartition(dll, l, r):
    i, j = l.next, r
    while i.next and j.prev and i != j and j != i.prev:
        while i.next and i.prev != j and i.data <= l.data:
            i = i.next
        while j.prev and i.prev != j and j.data >= l.data:
            j = j.prev
        if i !=j and j != i.prev:
            i.data, j.data = j.data, i.data
    if j.data < l.data:
        j.data, l.data = l.data, j.data
    return j

def lomutoPartition(dll, l, r):
    i = None
    pivot = r.data
    j = l
    while j != r:
        if j.data <= pivot:
            if i is None:
                i = l
            else:
                i = i.next
            i.data, j.data = j.data, i.data
        j = j.next
    if i is None:
        i = l
    else:
        i = i.next
    i.data, r.data = r.data, i.data
    return i

dll = DLL()
s = [3, 8, 6, 1, 7, 5, 2, 4]
for i in s:
    dll.append(i)
dll.printList()
quickSort(dll, dll.head, dll.tail)
dll.printList()
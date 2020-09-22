from list import LinkedList
from list import Node
import heapq

def mergeKSortedLists(lists):
    heap = [x for x in lists]
    k = len(lists)
    heapq.heapify(heap)
    head = tail = Node('x')
    while len(heap) > 0:
        tail.next = heap[0]
        tail = tail.next
        if heap[0].next:
            heapq.heappushpop(heap, heap[0].next)
        else:
            heapq.heappop(heap)
    return head.next

def mergeKSortedLists2(lists):
    heap = [x for x in lists]
    k = len(lists)
    buildHeap(heap)
    head = tail = Node('x')
    while len(heap) > 0:
        tail.next = heap[0]
        tail = tail.next
        if heap[0].next:
            heap[0] = heap[0].next
        else:
            heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
            heap.pop()
        heapify(heap, len(heap), 0)
    return head.next

def buildHeap(a):
    n = len(a)
    for i in range(n/2-1, -1, -1):
        heapify(a, n, i)

def heapify(a, n, i):
    smallest = i
    l = 2 * i + 1
    r = l + 1
    if l < n and a[l] < a[smallest]:
        smallest = l
    if r < n and a[r] < a[smallest]:
        smallest = r
    if i != smallest:
        a[smallest], a[i] = a[i], a[smallest]
        heapify(a, n, smallest)

a = LinkedList()
a.append(1)
a.append(4)
a.append(5)
b = LinkedList()
b.append(1)
b.append(3)
b.append(4)
c = LinkedList()
c.append(2)
c.append(6)
a.printList()
b.printList()
c.printList()
mergedList = LinkedList()
mergedList.head = mergeKSortedLists2([a.head, b.head, c.head])
mergedList.printList()

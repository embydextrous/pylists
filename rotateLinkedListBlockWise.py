from list import LinkedList
from list import Node

def rotateBlockWiseUtil(node, k, d):
    if abs(d) % k == 0 or node is None or node.next is None:
        return node
    d = ((-1 * d) % k) if d < 0 else ((k - d) % k) % k
    return rotateBlockWise(node, k, d)

def rotateBlockWise(node, k, d):
    if node is None or node.next is None:
        return node
    prev, current = None, node
    if current:
        x = k
        while current and x > 1:
            prev, current, next = current, current.next, current.next
            x -= 1
        if current:
            next = current.next
            current.next = None
        pair = leftRotate(node, d)
        last = pair[1]
        first = pair[0]
        if next:
            last.next = rotateBlockWise(next, k, d)
        return first
    
def leftRotate(node, k):
    if node is None or node.next is None:
        return node
    size = 1
    lastNode = node
    while lastNode.next:
        lastNode = lastNode.next
        size += 1
    k = k % size
    if k == 0:
        return node
    lastNode.next = node
    q = node
    while k > 1:
        q = q.next
        k -= 1
    node = q.next
    q.next = None
    return [node, q]

a = LinkedList()
for i in range(8):
    a.append(i)
a.printList()
a.head = rotateBlockWiseUtil(a.head, 4, 2)
a.printList()

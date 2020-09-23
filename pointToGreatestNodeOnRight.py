class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def pointRandomToGreatestNodeOnRight(node):
    if node is None or node.next is None:
        return
    reverseHead = lastNode = reverse(node)
    maxSoFar = lastNode
    lastNode = lastNode.next
    while lastNode:
        lastNode.random = maxSoFar
        if lastNode.data >= maxSoFar.data:
            maxSoFar = lastNode
        if lastNode.next is None:
            break
        lastNode = lastNode.next
    reverse(reverseHead)


def reverse(node):
    prev, current = None, node
    while current:
        next = current.next
        current.next = prev
        prev, current = current, next
    return prev


a = Node(5)
a.next = Node(10)
a.next.next = Node(2)
a.next.next.next = Node(3)
pointRandomToGreatestNodeOnRight(a)
while a:
    print a.data, a.next.data if a.next else None, a.random.data if a.random else None
    a = a.next
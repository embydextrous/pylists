class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def flatten(node):
    tail = node
    x = node
    while tail.next:
        tail = tail.next
    while node:
        if node.child:
            tail.next = node.child
            node.child = None
            while tail.next:
                tail = tail.next
        node = node.next
    return x
    
a = Node(10)
a.next = Node(5)
a.next.next = Node(12)
a.next.next.next = Node(7)
a.next.next.next.next = Node(11)
a.child = Node(4)
a.child.next = Node(20)
a.child.next.next = Node(13)
a.child.next.child = Node(2)
a.child.next.next.child = Node(16)
a.child.next.next.child.child = Node(3)
a.next.next.next.child = Node(17)
a.next.next.next.child.next = Node(6)
a.next.next.next.child.child = Node(9)
a.next.next.next.child.child.next = Node(8)
a.next.next.next.child.child.child = Node(19)
a.next.next.next.child.child.child.next = Node(15)

b = flatten(a)
while b:
    print b.data,
    b = b.next




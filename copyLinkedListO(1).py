class Node:
    def __init__(self, data):
        self.data = data
        self.random = None
        self.next = None

def clone(a):
    head = a
    while a:
        newNode = Node(a.data)
        newNode.next = a.next
        a.next = newNode
        a = a.next.next
    a = head
    while a:
        a.next.random = a.random.next
        a = a.next.next
    returnHead = None
    returnTail = None
    a = head
    while a:
        if returnHead is None:
            returnHead = a.next
            returnTail = a.next
            a.next = a.next.next
            a = a.next
        else:
            returnTail.next = a.next
            returnTail = returnTail.next
            a.next = a.next.next
            a = a.next
    returnTail.next = None
    return returnHead

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)
a.next.next.next.next = Node(5)
a.random = a.next.next
a.next.random = a
a.next.next.random = a.next.next.next.next
a.next.next.next.random = a.next.next
a.next.next.next.next.random = a.next

head = a
while head:
    print head.data,
    head = head.next
print
head = a
while head:
    print head.data, "->", head.random.data
    head = head.next

b = clone(a)

head = a
while head:
    print head.data,
    head = head.next
print
head = a
while head:
    print head.data, "->", head.random.data
    head = head.next

head = b
while head:
    print head.data,
    head = head.next
print
head = b
while head:
    print head.data, "->", head.random.data
    head = head.next


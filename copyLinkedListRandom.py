class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copy(a):
    if a is None:
        return None
    head = Node(a.data)
    tail = head
    d = {}
    d[a] = a.next
    a.next = tail
    tail.random = a
    a = d[a]
    while a:
        tail.next = Node(a.data)
        tail = tail.next
        tail.random = a
        d[a] = a.next
        a.next = tail
        a = d[a]
    tail = head
    while tail:
        tail.random = tail.random.random.next
        tail = tail.next
    for key in d.keys():
        key.next = d[key]
    return head

head = a = Node(1)
for i in range(2, 6):
    a.next = Node(i)
    a = a.next
head.random = head.next.next
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next

p = head
while p:
    print p.data,
    p = p.next
print

p = head
while p:
    print p.data, " -> ", p.random.data
    p = p.next

copyHead = copy(head)

p = copyHead
while p:
    print p.data,
    p = p.next
print

p = copyHead
while p:
    print p.data, " -> ", p.random.data
    p = p.next
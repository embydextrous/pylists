class Node:
    def __init__(self, coeff, deg):
        self.coeff = coeff
        self.deg = deg
        self.next = None
    
def add(a, b):
    if a is None:
        return b
    if b is None:
        return a
    head = tail = Node('x', 'x')
    while a and b:
        if a.deg == b.deg:
            a.coeff += b.coeff
            tail.next = a
            tail = tail.next
            a, b = a.next, b.next
        elif a.deg > b.deg:
            tail.next = a
            tail = tail.next
            a = a.next
        else:
            tail.next = b
            tail = tail.next
            b = b.next
    if a:
        tail.next = a
    if b:
        tail.next = b
    return head.next

def printList(a):
    if a is None:
        print None
    else:
        while a:
            strrep = ""
            if a.deg == 0:
                strrep += str(a.coeff)
            elif a.coeff != 1:
                strrep += str(a.coeff)
            if a.deg > 0:
                if a.deg == 1:
                    strrep += 'x'
                if a.deg > 1:
                    strrep += 'x^' + str(a.deg)
            if a.next:
                strrep += " +"
            print strrep,
            a = a.next
        print

a = Node(5, 2)
a.next = Node(4, 1)
a.next.next = Node(2, 0)

b = Node(5, 4)
b.next = Node(5, 0)

printList(a)
printList(b)
c = add(a, b)
printList(c)
            
            
    
            
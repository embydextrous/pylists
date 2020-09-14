from list import LinkedList
from list import Node

def add(a, b):
    result = LinkedList()
    lastNode = None
    carry = 0
    while a and b:
        sum = a.data + b.data + carry
        if lastNode:
            lastNode.next = Node(sum % 10)
            lastNode = lastNode.next
        else:
            result.head = Node(sum % 10)
            lastNode = result.head
        carry = sum / 10
        a, b = a.next, b.next
    while a:
        sum = a.data + carry
        if lastNode:
            lastNode.next = Node(sum % 10)
            lastNode = lastNode.next
        else:
            result.head = Node(sum % 10)
            lastNode = result.head
        carry = sum / 10
        a = a.next
    while b:
        sum = b.data + carry
        if lastNode:
            lastNode.next = Node(sum % 10)
            lastNode = lastNode.next
        else:
            result.head = Node(sum % 10)
            lastNode = result.head
        carry = sum / 10
        b = b.next
    if carry == 1:
        if lastNode:
            lastNode.next = Node(1)
        else:
            result.head = Node(1)
    return result

a = LinkedList()
a.append(6)
a.append(7)
a.append(5)
b = LinkedList()

add(a.head, b.head).printList()



    


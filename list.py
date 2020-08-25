class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insertion at head
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        if self.head is None:
            push(self, data)
        else:
            newNode = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def insertAfter(self, data, key):
        if self.head is None:
            return
        current = self.head
        while current and current.data != key:
            current = current.next
        if current:
            newNode = Node(data)
            newNode.next = current.next
            current.next = newNode

    def printList(self):
        print "head ->",
        current = self.head
        while current:
            print str(current.data) + " ->",
            current = current.next
        print "null"

a = LinkedList()
a.push(2)
a.push(1)
a.append(4)
a.insertAfter(3, 2)
a.printList()

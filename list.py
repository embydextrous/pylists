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

    def deleteKey(self, key):
        if self.head is None:
            return
        current, prev = self.head, None
        while current and current.data != key:
            current, prev = current.next, current
        if current is None:
            return
        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        current = None

    # position is 0-indexed
    def deleteAt(self, position):
        if position < 0:
            return
        current, prev = self.head, None
        while current and position != 0:
            current, prev = current.next, current
            position -= 1
        if current is None:
            return    
        if prev:
            prev.next = current.next
        else:
            self.head = current.next
        current = None

    def delete(self):
        while self.head:
            current = self.head
            self.head = current.next
            current = None

    def size(self):
        n = 0
        current = self.head
        while current:
            current = current.next
            n += 1
        return n

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
a.append(5)
a.append(6)
a.append(7)
a.printList()
print a.size()
a.delete()
a.printList()
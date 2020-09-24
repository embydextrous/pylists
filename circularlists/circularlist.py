class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def push(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.tail.next = self.tail
        else:
            newNode = Node(data)
            newNode.next = self.tail.next
            self.tail.next = newNode

    def append(self, data):
        if self.tail is None:
            self.push(data)
            return
        newNode = Node(data)
        newNode.next = self.tail.next
        self.tail.next = newNode
        self.tail = self.tail.next

    def insertAfter(self, node, data):
        if node is None:
            return
        if node == tail:
            self.append(data)
        else:
            newNode = Node(data)
            newNode.next = node.next
            node.next = newNode

    def popFirst(self):
        if self.tail is None:
            return
        if self.tail.next == self.tail:
            self.tail = None
        else:
            self.tail.next = self.tail.next.next 

    def popLast(self):
        if self.tail is None:
            return
        if self.tail.next == self.tail:
            self.tail = None
        else:
            current = self.tail.next
            while current.next != self.tail:
                current = current.next
            current.next = self.tail.next
            self.tail = current

    def delete(self, data):
        if self.tail is None:
            return
        if self.tail.data == data and self.tail.next == self.tail:
            self.tail = None
        else:
            prev, current = self.tail, self.tail.next
            while current.next != self.tail.next:
                if current.data == data:
                    prev.next = current.next
                    current.next = None
                    return
                prev, current = current, current.next  
            if self.tail.data == data:
                prev.next = self.tail.next
                self.tail = prev      

    def printList(self):
        print "head ->",
        if self.tail is None:
            print "null"
        else:
            current = self.tail.next
            while current.next != self.tail.next:
                print str(current.data) + " ->",
                current = current.next
            print str(self.tail.data) + " ->",
            print "head"

c = CircularLinkedList()
c.push(4)
c.append(6)
c.push(1)
c.push(3)
c.push(5)
c.append(8)
c.printList()
c.popFirst()
c.printList()
c.popLast()
c.printList()
c.popLast()
c.popLast()
c.popFirst()
c.popLast()
c.printList()
class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:
    def __init__(self, node = None):
        self.head = node

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def append(self, data):
        if self.head is None:
            self.push(data)
        else:
            newNode = Node(data)
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.prev = lastNode

    def insertAfter(self, node, data):
        if not node or not self.head:
            return
        if node.next:
            newNode = Node(data)
            newNode.next = node.next
            newNode.prev = node
            node.next.prev = newNode
            node.next = newNode
        else:
            self.append(data)

    def insertBefore(self, node, data):
        if not node or not self.head:
            return
        if node == self.head:
            self.push(data)
        else:
            newNode = Node(data)
            newNode.next = node
            newNode.prev = node.prev
            node.prev.next = newNode
            node.prev = newNode
        
    def delete(self, node):
        if node is None:
            return
        if node == self.head:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev.next = None
                self.head.prev = None
        else:
            if node.next is None:
                node.prev.next = None
                node.prev = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None

    def printList(self):
        print "head <->",
        current = self.head
        while current:
            print str(current.data), "<->",
            current = current.next
        print "null"

dll = DLL()
dll.push(1)
dll.push(2)
dll.push(3)
dll.push(4)
dll.append(5)
dll.insertAfter(dll.head.next.next.next.next, 6)
dll.insertAfter(dll.head, 7)
dll.insertAfter(dll.head.next.next, 8)
dll.insertBefore(dll.head, 9)
dll.insertBefore(dll.head.next.next.next.next.next.next.next.next, 10)
dll.insertBefore(dll.head.next.next, 11)
dll.printList()
dll.delete(dll.head)
dll.printList()
dll.delete(dll.head.next.next.next)
dll.printList()
dll.delete(dll.head.next.next.next.next.next.next.next.next)
dll.printList()

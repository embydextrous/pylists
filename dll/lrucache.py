from dll import DLL
from dll import Node

class CacheEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class LruCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dll = DLL()
        self.d = {}
        self.size = 0

    def put(self, key, value):
        if key in self.d:
            node = self.d[key]
            node.data.setValue(value)
            self.dll.delete(node)
            self.dll.pushNode(node)
        else:
            cacheEntry = CacheEntry(key, value)
            node = Node(cacheEntry)
            if not self.isFull():
                self.d[key] = node
                self.dll.pushNode(node)
                self.size += 1
            else:
                keyToDelete = self.dll.tail.data.key
                self.dll.delete(self.dll.tail)
                self.d.pop(keyToDelete)
                self.d[key] = node
                self.dll.pushNode(node)


    def isFull(self):
        return self.size == self.capacity

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.dll.delete(node)
            self.dll.pushNode(node)
            return node.data.value
        return None

    def delete(self, key):
        if key in self.d:
            node = self.d[key]
            self.dll.delete(node)
            self.d.pop(key)
            self.size -= 1

    def printCache(self):
        self.dll.printList()
        for value in self.d.values():
            print value
        print self.size

cache = LruCache(4)
cache.printCache()
cache.put(1, 3)
cache.printCache()
cache.put(2, 4)
cache.printCache()
cache.put(3, 5)
cache.printCache()
cache.put(1, 5)
cache.printCache()
cache.put(4, 6)
cache.printCache()
cache.put(5, 7)
cache.printCache()
class DlinkedNoed():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = DlinkedNoed()
        self.tail = DlinkedNoed()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.ha = dict()
    def moveToTail(self, node):
        # move
        self.deleteNode(node)
        self.addToTail(node)

    def deleteNode(self, node):
        # delete
        node.pre.next = node.next
        node.next.pre = node.pre

    def addToTail(self, node):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

    def get(self, key: int) -> int:
        if key not in self.ha:
            return -1
        else:
            node = self.ha[key]
            self.moveToTail(node)
            return  node.value

    def put(self, key: int, value: int) -> None:
        if key in self.ha:
            node = self.ha[key]
            node.value = value
            self.moveToTail(node)
        else:
            node = self.ha[key] = DlinkedNoed(key, value)
            if len(self.ha) <= self.cap:
                self.addToTail(node)
            else:
                delNode = self.head.next
                self.ha.pop(delNode.key)
                self.deleteNode(delNode)
                self.addToTail(node)

cache = LRUCache(1)
cache.put(2, 1)
cache.get(2)
cache.put(3,2)
cache.get(2)
cache.get(3)
# cache.put(4, 4)
# cache.get(1)
# cache.get(3)
# cache.get(4)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
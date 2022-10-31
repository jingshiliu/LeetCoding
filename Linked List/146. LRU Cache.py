class DoubleNode:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.storage = {} # Space:  O(capacity)
        self.cache = capacity
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.storage:
            self.removeNode(self.storage[key])
            self.addToTop(self.storage[key])
            return self.storage[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.storage:
            self.removeNode(self.storage[key])
        self.storage[key] = DoubleNode(key, value)
        self.addToTop(self.storage[key])
        if len(self.storage) > self.cache:
            node = self.tail.prev
            self.removeNode(node)
            self.storage.pop(node.key)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev, node.next = None, None

    def addToTop(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def printList(self):
        count = 0
        ptr = self.head
        string = ''
        while ptr:
            string += str(ptr.val)
            ptr = ptr.next
            count += 1
            if count > 10: break
        print(string)
        ptr = self.tail
        string = ''
        while ptr:
            string = str(ptr.val) + string
            ptr = ptr.prev
        print(string)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
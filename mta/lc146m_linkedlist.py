class Node:
    def __init__(self, key=None, value=None):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add_head(node)
            return node.value
        else: return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove(node)
            self.add_head(node)
        else:
            if len(self.cache)>=self.size:
                lru=self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
            
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.add_head(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

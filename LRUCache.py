class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        # node.next = node.prev = None

    def insert(self, node: Node):
        prev_node = self.tail.prev
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        # if the key exists in the cache
        if key in self.cache:
            # remove the key from its existing position in the list
            self.remove(self.cache[key])
            # insert it at the head of the linked list
            self.insert(self.cache[key])
            # retrun its value
            return self.cache[key].val
        # esle: return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key already exists
        if key in self.cache:
            # remove it from the list
            self.remove(self.cache[key])

        # make a new node with the new value
        curr = Node(key, value)
        # insert the node into the cache
        self.cache[key] = curr
        # insert it at the beginning of the list
        self.insert(self.cache[key])

        # check if the cap has been exceeded
        # if len(cache) > cap:
        if len(self.cache) > self.cap:
            # get the lru (next to head)
            lru = self.head.next
            # remove the lru
            self.remove(lru)
            # del the key from the cache
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

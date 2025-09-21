class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRU:
    def __init__(self, cap):
        self.cap = cap
        self.map = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = node.prev = None

    def insert(self, node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

    def get(self, key):
        # if the key exists:
        if key in self.map:
            # remove the node from the linked list
            self.remove(self.map[key])
            # insert it at the right (most recent)
            self.insert(self.map[key])
            # return the node
            return self.map[key].val
        else:
            return -1

    def put(self, key, val):
        # check if the key already exists:
        if key in self.map:
            # if it does -
            # 1. remove the k,v pair from the linked list
            self.remove(self.map[key])
        # 2. make the new Node and insert it into the linked list (to the right bcz it will be the most recently used)
        node = Node(key, val)
        self.map[key] = node
        self.insert(self.map[key])
        # check if the size of the hashmap is greater than cap:
        if len(self.map) > self.cap:
            # if it is -
            # remove the LRU value from the linked list
            lru = self.left.next
            self.remove(lru)
            # del the val from the hashmap
            del self.map[lru.key]

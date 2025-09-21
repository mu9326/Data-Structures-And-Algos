class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # print(self.root.children)
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True


# # Your Trie object will be instantiated and called as such:
# obj = Trie()
# print(obj.insert("apple"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
def print_trie(node, level=0):
    for char, child in node.children.items():
        print("  " * level + f"'{char}' (end={child.endOfWord})")
        print_trie(child, level + 1)


# Usage:
obj = Trie()
obj.insert("apple")
obj.insert("app")
print_trie(obj.root)

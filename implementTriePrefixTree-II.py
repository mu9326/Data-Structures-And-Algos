class TrieNode:
    def __init__(self):
        self.children = {}
        self.countEndsWith = 0
        self.countPrefix = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.countPrefix += 1

        cur.countEndsWith += 1

    def countWordsEqualTo(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        return cur.countEndsWith

    def countWordsStartingWith(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]

        return cur.countPrefix

    def erase(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return
            else:
                cur = cur.children[c]
                cur.countPrefix -= 1

        cur.countEndsWith -= 1

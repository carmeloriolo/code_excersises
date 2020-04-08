class TrieNode:

    def __init__(self, value):
        self.value = value
        self.children = [None] * 26
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.count = 0
        self.root = TrieNode('root')

    def add(self, word):
        word = word.lower()
        root = self.root
        for word_index in range(0, len(word)):
            key = word[word_index]
            index = ord(key) - 97
            if root.children[index] is not None:
                root = root.children[index]
                continue
            tn = TrieNode(key)
            root.children[index] = tn
            root = tn
        root.end_of_word = True

    def search(self, word) -> bool:
        word = word.lower()
        root = self.root
        found = True
        for key in word:
            index = ord(key) - 97
            if root.children[index] is not None:
                root = root.children[index]
                continue
            found = False
            break
        return found

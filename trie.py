from hashtable import HashTable
from dynamicarray import DynArray

class Trie:
    class _TrieNode_:
        def __init__(self):
            self.children = HashTable()
            self.word_end = False

    ## O(1)
    def __init__(self):
        self.root = self._TrieNode_()

    ## O(n)
    def insert(self, word:str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = self._TrieNode_()
            curr = curr.children[c]
        curr.word_end = True

    ## O(x)
    def delete(self, word:str) -> None:
        pass

    ## O(n)
    def search(self, word:str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.word_end

    ## O(n)
    def hasPrefix(self, prefix) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True

    ## O(x)
    def startsWith(self, prefix) -> bool:
        words = DynArray()
        pass

    ## O(x)
    def listWords(self) -> None:
        words = DynArray()
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert('Hello')
    trie.insert('Hell')

    print(trie.search('Hello'))
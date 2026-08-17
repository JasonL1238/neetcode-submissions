class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i in curr.children:
                curr = curr.children[i]
            else:
                node = TrieNode()
                curr.children[i] = node
                curr = node
        
        curr.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if not i in node.children:
                return False
            else:
                node = node.children[i]
        
        return node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if not i in node.children:
                return False
            else:
                node = node.children[i]
        return True
        
        
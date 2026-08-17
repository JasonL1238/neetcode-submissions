class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if not i in curr.children:
                node = TrieNode()
                curr.children[i] = node
                curr = node
            else:
                curr = curr.children[i]
        
        curr.isEnd = True
        print(word + " add")        

    def search(self, word: str) -> bool:

        i = 0
        def helper(node: TrieNode) -> bool:
            nonlocal i

            while i < len(word):
                if word[i] == ".":
                    a = False
                    print(word + " word")
                    print(str(i) + " i")
                    print(node.children)
                    for k in node.children.values():
                        temp = i
                        i += 1
                        a = a or helper(k)
                        i = temp
                    return a
                elif not word[i] in node.children:
                    return False
                else:
                    node = node.children[word[i]]
                
                i += 1
            
            return node.isEnd 
        
        return helper(self.root)

        

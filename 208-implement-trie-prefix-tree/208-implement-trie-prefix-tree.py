class TrieNode:
    
    def __init__(self, children = dict(), exists: bool = False) -> None:
        self.children = dict(children)
        self.exists = exists

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curNode = self.root
        
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            
            curNode = curNode.children[char]
        
        curNode.exists = True

    def search(self, word: str) -> bool:
        curNode = self.root
        
        for char in word:
            if char not in curNode.children:
                return False
            
            curNode = curNode.children[char]
        
        return curNode.exists
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        
        for char in prefix:
            if char not in curNode.children:
                return False
            
            curNode = curNode.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
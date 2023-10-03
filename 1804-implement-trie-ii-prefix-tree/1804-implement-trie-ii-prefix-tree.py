class TrieNode:
    def __init__(self):
        self.children = dict() 
        self.count = 0
        self.thisCount = 0
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            cur.count += 1
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        
        cur.count += 1
        cur.thisCount += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                return 0
            
            cur = cur.children[char]
        
        return cur.thisCount

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return 0
            
            cur = cur.children[char]
        
        return cur.count

    def erase(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            cur.count -= 1
            if char not in cur.children:
                return 
            
            cur = cur.children[char]
        
        cur.count -= 1
        cur.thisCount -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
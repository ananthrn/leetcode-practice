class TrieNode:
    def __init__(self, children = dict(), numWords = 0):
        self.children = dict()
        self.numWords = numWords
        
class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def insertWord(self, word: str):
        currentNode = self.rootNode
        currentNode.numWords += 1
        for char in word:
            
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            
            currentNode = currentNode.children[char]
            currentNode.numWords += 1
        
    def getNumWords(self, word: str) -> int:
        currentNode = self.rootNode 
        ans = 0
        for char in word:
            if char not in currentNode.children:
                return ans
            
            currentNode = currentNode.children[char]
            ans += currentNode.numWords
        
        return ans
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insertWord(word)
        
        ans = map(trie.getNumWords, words)
        
        return ans
        
class TrieNode:
    def __init__(self):
        self.numWords = 0
        self.children = dict()

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
        
    
    def getNumWordsWithPrefix(self, prefix: str) -> int:
        currentNode = self.rootNode
        
        for char in prefix:
            if char not in currentNode.children:
                return 0
            
            currentNode = currentNode.children[char]
        
        return currentNode.numWords
        
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        
        list(map(lambda word: trie.insertWord(word), words))
        
        numWords = trie.getNumWordsWithPrefix(pref)
        
        return numWords
        
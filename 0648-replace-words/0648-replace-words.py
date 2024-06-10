class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self, words: List[str]):
        self.rootNode = TrieNode()
        
        for word in words:
            self.insert(word)
        
    def insert(self, word: str):
        currentNode = self.rootNode
        
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            
        currentNode.isWord = True
    
    def search(self, word: str) -> str:
        currentNode = self.rootNode
        
        for ind, char in enumerate(word):
            if char not in currentNode.children:
                return word
                
            currentNode = currentNode.children[char]
            
            if currentNode.isWord:
                return word[:ind + 1]
        
        return word
    


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie(dictionary)
        
        newWords = [trie.search(word) for word in sentence.split()]
        
        return " ".join(newWords)
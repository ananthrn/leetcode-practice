class TrieNode:
    def __init__(self):
        self.wordExists = False
        self.children = dict()
        
    
class Trie:
    def __init__(self,):
        self.rootNode = TrieNode()
        
    
    def insertWord(self, word: str):
        currentNode = self.rootNode
        
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            # print("currentNode.children: ", currentNode.children)
            currentNode = currentNode.children[char]
            
        
        currentNode.wordExists = True
        
        # print("self.rootNode.children: ", self.rootNode.children)
    
    def findString(self, word: str) -> bool:
        currentNode = self.rootNode
        
        for char in word:
            
            if char not in currentNode.children:
                return False
            
            currentNode = currentNode.children.get(char, None)
            if currentNode.wordExists:
                return True
        
        # print("self.rootNode.children: ", self.rootNode.children)
        return currentNode.wordExists

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        for word in words:
            self.trie.insertWord(reversed(word))
        
        self.fullQuery = ""
        

    def query(self, letter: str) -> bool:
        self.fullQuery += letter
        
        return self.trie.findString(reversed(self.fullQuery))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    def __init__(self, word: str = None) -> None:
        self.word = word
        self.children = dict()
        
class Trie:
    def __init__(self) -> None:
        self.rootNode = TrieNode(word="")
    
    def insertWord(self, word: str) -> None:
        currentNode = self.rootNode
        
        for index, char in enumerate(word):
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            
            currentNode = currentNode.children[char]
        currentNode.word = word
        
    
    def getLongestWord(self) -> str:
        currentLongestWord = ""
        
        Q = collections.deque([self.rootNode])
        
        while Q:
            tp = Q.pop()
            
            if tp.word is not None:
                if len(tp.word) > len(currentLongestWord) or (len(tp.word) == len(currentLongestWord) and tp.word < currentLongestWord):
                    currentLongestWord = tp.word
                
                for nextNode in tp.children.values():
                    Q.appendleft(nextNode)
        
        return currentLongestWord
        
        return currentLongestWord
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for word in words:
            trie.insertWord(word)
            
        
        return trie.getLongestWord()
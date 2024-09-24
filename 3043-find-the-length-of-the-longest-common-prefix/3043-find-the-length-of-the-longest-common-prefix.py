class TrieNode:
    def __init__(self, prefix: str = None) -> None:
        self.prefix = prefix
        self.counts = [0, 0]
        self.children = dict()
        
class Trie:
    def __init__(self) -> None:
        self.rootNode = TrieNode(prefix="")
    
    def insertWord(self, word: str, arrayIndex: int) -> None:
        currentNode = self.rootNode
        currentNode.counts[arrayIndex] += 1
        for index, char in enumerate(word):
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            
            currentNode = currentNode.children[char]
            currentNode.prefix = word[:index + 1]
            currentNode.counts[arrayIndex] += 1
        
    
    def getLongestWord(self) -> str:
        currentLongestWord = ""
        
        Q = collections.deque([self.rootNode])
        
        while Q:
            tp = Q.pop()
            
            if min(tp.counts) >= 1:
                if len(tp.prefix) > len(currentLongestWord):
                    currentLongestWord = tp.prefix
                
                for nextNode in tp.children.values():
                    Q.appendleft(nextNode)
        
        return currentLongestWord

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        
        for word in arr1:
            trie.insertWord(str(word), 0)
        
        for word in arr2:
            trie.insertWord(str(word), 1)
            
        LCP = trie.getLongestWord()
        
        return len(LCP)
        
        
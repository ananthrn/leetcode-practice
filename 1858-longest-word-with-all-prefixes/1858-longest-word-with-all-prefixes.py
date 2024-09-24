
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
                # print("current longest", currentLongestWord)
                # print("tp.word: ", tp.word)
                # print("tuples: ", (len(tp.word), currentLongestWord))
                # print("tuple second: ", (len(currentLongestWord), tp.word))
                # print("greater? :", (len(tp.word), currentLongestWord) > (len(currentLongestWord), tp.word))
                # print()
                if (len(tp.word), currentLongestWord) > (len(currentLongestWord), tp.word):
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
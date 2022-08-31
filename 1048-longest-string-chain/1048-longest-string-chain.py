from collections import defaultdict
class Solution:
    def isSubSeq(self, word_1, word_2) -> bool:
        charPos = defaultdict(list)
        
        for ind, char in enumerate(word_2):
            charPos[char].append(ind)
            
        currentIndex = -1
        
        for char in word_1:
            if char not in charPos:
                return False
            
            posIndex = bisect_left(charPos[char], currentIndex)
            
            if posIndex >= len(charPos[char]):
                return False
            
            currentIndex = charPos[char][posIndex]
        
        return True
    
    def isPredecessor(self, word_1, word_2) -> bool:
        return len(word_2) == len(word_1) + 1 and self.isSubSeq(word_1, word_2)
    
    def longestStrChain(self, words: List[str]) -> int:
        # ans = 0
        words = sorted(words, key=lambda x: len(x))
        
        cache = {}
        
        @lru_cache
        def backtrack(index):
            if cache.get(index, None):
                return cache.get(index)
            
            # print("currentWord:", currentWord)
            # print("index: ", index)
            # print("depth: ",depth)
            ans = 0 #max(ans, depth)
                
            for ind in range(index + 1, len(words)):
                if self.isPredecessor( words[index], words[ind]):
                    nextAns = backtrack(ind)
                    ans = max(ans, nextAns)
            
            cache[index] = ans + 1
            return ans + 1
        
        ansAll = max([backtrack(ind) for ind in range(len(words))])
    
            
        return ansAll
            
        
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def getBitMask(word: str) -> int:
            mask = 0
            char_index = lambda ch: ord(ch) - ord('a')
            for ch in word:
                bitSet = 1 << char_index(ch)
                mask |= bitSet
            
            return mask
        
        n = len(words)
        
        bitMaskToLength = collections.defaultdict(int)
        
        for word in words:
            bitMaskToLength[getBitMask(word)] = max(bitMaskToLength[getBitMask(word)], len(word))
        
        ans = 0
        for x in bitMaskToLength:
            for y in bitMaskToLength:
                if x & y == 0:
                    ans = max(
                        ans,
                        bitMaskToLength[x] * bitMaskToLength[y]
                    )
        
        
        
        return ans
                
        
        
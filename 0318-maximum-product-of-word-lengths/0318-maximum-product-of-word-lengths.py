class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        
        masks = n * [0]
        lens = [len(word) for word in words]
        
        char_index = lambda ch: ord(ch) - ord('a')
        for ind, word in enumerate(words):
            for ch in word:
                bit_index = 1 << char_index(ch)
                masks[ind] |= bit_index
        
        
        ans = 0
        
        for ind1 in range(n):
            for ind2 in range(ind1 + 1, n):
                if masks[ind1] & masks[ind2] == 0:
                    ans = max(ans, lens[ind1] * lens[ind2])
        
        return ans
                
        
        
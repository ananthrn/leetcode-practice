class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) <= 1:
            return True
        
        cnt = collections.Counter("".join(words))
        
        n = len(words)
        
        val = list(cnt.values())[0]
        
        return all([cntVal % len(words) == 0 for cntVal in cnt.values()])
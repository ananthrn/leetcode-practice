class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) <= 1:
            return True
        
        cnt = collections.Counter("".join(words))
        
        
        return all([cntVal % len(words) == 0 for cntVal in cnt.values()])
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        cnt = collections.Counter("".join(words))
        
        
        return all([cntVal % len(words) == 0 for cntVal in cnt.values()])
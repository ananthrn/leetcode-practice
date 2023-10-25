class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bitMap = collections.defaultdict(int)
        
        for candidate in candidates:
            binRep = bin(candidate)[2:]
            
            for ind, val in enumerate(binRep[::-1]):
                if val == "1":
                    bitMap[ind] +=1
        
        return max(bitMap.values())
        
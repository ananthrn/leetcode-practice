class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        
        travelSums = list(travel)
        
        for ind in range(1, len(travelSums)):
            travelSums[ind] += travelSums[ind - 1]
        
        lastFound = collections.defaultdict(int)
        totalCount = collections.Counter()
        
        for index, gar in enumerate(garbage):
            thisCount = collections.Counter(gar)
            
            totalCount += thisCount
            
            for key in ("M", "P", "G"):
                if key in thisCount:
                    lastFound[key] = index
        
        ans = 0
        for key, val in totalCount.items():
            travelAnswer = 0 if lastFound[key] == 0 else travelSums[lastFound[key] - 1]
            ans += val + travelAnswer
        
        return ans
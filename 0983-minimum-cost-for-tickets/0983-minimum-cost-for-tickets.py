class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        costMap = {
            0: 1,
            1: 7,
            2: 30
        }
        
        @cache
        def helper(index):
            if index >= len(days):
                return 0
            
            mincost = 1_000_000_000
            for costIndex, cost in enumerate(costs):
                dayPass = costMap[costIndex]
                nextIndex = bisect.bisect_right(days, days[index] + dayPass - 1, index+1)
                mincost = min(mincost, cost + helper(nextIndex))
            
#             print("index:", index)
#             print("mincost: ", mincost)
#             print()
            return mincost
        
        
        return helper(0)
            
            
        
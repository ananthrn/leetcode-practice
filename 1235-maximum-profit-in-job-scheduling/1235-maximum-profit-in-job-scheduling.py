class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         @lru_cache
#         def backtrack(index: int, currentEndTime: int) -> int:
#             """
#             returns profit starting from index, for currentEndTime
#             """
            
#             if index >= len(profit):
#                 return 0
            
#             maxProfit = backtrack(index + 1, currentEndTime)
            
#             if startEndProfit[index][0] >= currentEndTime:
#                 maxProfit = max(maxProfit, startEndProfit[index][2] + backtrack(index + 1, max(currentEndTime, startEndProfit[index][1])))
            
#             return maxProfit
        
        
        @lru_cache
        def backtrack(index: int) -> int:
            """
            returns profit starting from index, for currentEndTime
            """

            if index >= len(profit):
                return 0

            # if you include this job
            profitExclude = backtrack(index + 1)

            # if you don't include this job
            nextIndex = bisect.bisect_left(startEndProfit, (startEndProfit[index][1], 0, 0))
            profitInclude =  startEndProfit[index][2] + backtrack(nextIndex)

            return max(profitExclude, profitInclude)
        
        startEndProfit = list(sorted(zip(startTime, endTime, profit)))
        
        answer = backtrack(0)
        
        return answer
        
            
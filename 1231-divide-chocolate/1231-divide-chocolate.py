class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def getSplits(minSum) -> int:
            currentSum = 0
            pieces = 0
            for sweet in sweetness:
                currentSum += sweet
                if currentSum >= minSum:
                    pieces += 1
                    currentSum = 0
            
            return pieces
        
        
        bestSum = 0
        start, end = 1, sum(sweetness)
        
        while start <= end:
            mid = (start + end)//2
            
            splits = getSplits(mid)
            
            if splits >= k + 1:
                
                bestSum = max(bestSum, mid)
                start = mid + 1
            else:
                end = mid - 1
        
        return bestSum
        
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def getBouqets(day: int) -> int:
            numBouqets = 0
            currentCount = 0
            
            for bloom in bloomDay:
                if day >= bloom:
                    currentCount += 1
                else:
                    currentCount = 0
                
                if currentCount == k:
                    numBouqets += 1
                    currentCount = 0
            
            return numBouqets
        
        
        if len(bloomDay) < m *k:
            return -1
        
        low, high = min(bloomDay), max(bloomDay)
        earliestDay = max(bloomDay)
        
        while low <= high:
            mid = (high + low)//2
            
            if getBouqets(mid) >= m:
                earliestDay = min(earliestDay, mid)
                high = mid -1
            else:
                low = mid + 1
        
        return earliestDay
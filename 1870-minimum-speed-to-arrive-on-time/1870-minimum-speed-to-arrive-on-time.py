class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def getReachingHour(dist: List[int], speed: int) -> int:
            n = len(dist)
            
            return sum(ceil(d/speed) if ind < n - 1 else d/speed for (ind, d) in enumerate(dist))
        
        
        
        bestSpeed = 10_000_001
        possible = False
        start, end = 1, 10_000_000
        
        while start <= end:
            mid = (start + end)//2
            reachingHour = getReachingHour(dist, mid)
            
            if reachingHour <= hour:
                possible = True
                bestSpeed = min(bestSpeed, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        
        return bestSpeed if possible else -1
            
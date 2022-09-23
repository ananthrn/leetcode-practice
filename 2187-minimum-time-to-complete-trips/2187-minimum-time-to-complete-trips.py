class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def getTotalTrips(timestamp):
            busTrips = [
                timestamp//t for t in time 
            ]
            return sum(busTrips)
        
        start, end = 0, totalTrips * min(time)
        bestTime = end
        
        while start <= end:
            mid = (start + end)//2
            busTrips = sum([mid//t for t in time])
            
            if busTrips >= totalTrips:
                bestTime = min(bestTime, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return bestTime
        
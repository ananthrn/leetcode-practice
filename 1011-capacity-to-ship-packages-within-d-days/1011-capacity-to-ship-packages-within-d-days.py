class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checkCapacity(capacity: int) -> int:
            numberOfDaysNeeded = 1
            currentCapacity = capacity
            for weight in weights:
                if currentCapacity >= weight:
                    currentCapacity -= weight
                else:
                    numberOfDaysNeeded += 1
                    currentCapacity = capacity - weight
            print("capacity: ", capacity)
            print("numberOfDaysNeeded: ", numberOfDaysNeeded)
            print()
            return numberOfDaysNeeded <= days
        
        start, end = max(weights), sum(weights)
        
        bestCapacity = end 
        while start <= end:
            mid = (start + end)//2
            
            checkCap = checkCapacity(mid)
            
            if checkCap:
                end = mid - 1
                bestCapacity = min(bestCapacity, mid)
            else:
                start = mid + 1
        
        return bestCapacity
        
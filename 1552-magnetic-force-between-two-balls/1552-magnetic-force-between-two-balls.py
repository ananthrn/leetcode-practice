class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        @cache
        def helper(currentIndex: int, lastBallPosition: int, ballsToPlace: int) -> int:
            if ballsToPlace == 0:
                return inf
            
            if currentIndex >= len(position):
                return -inf if ballsToPlace > 0 else inf
            
            # place ball here:
            currentVal = inf if lastBallPosition == -1 else (position[currentIndex] - lastBallPosition)
            
            nextMinPlace = helper(currentIndex + 1, position[currentIndex], ballsToPlace - 1)
            
            minPlace = min(currentVal, nextMinPlace)
            # don't place ball here
            nextMinDontPlace = helper(currentIndex + 1, lastBallPosition, ballsToPlace)
            
            # print("currentIndex: ", currentIndex)
            # print("lastBallPosition: ", lastBallPosition)
            # print("ballsToPlace: ", ballsToPlace)
            # print("minPlace: ", minPlace)
            # print("nextMinDontPlace", nextMinDontPlace)
            # print()
            return max(minPlace, nextMinDontPlace)
        
        def maxBallsPossible(minDistance: int) -> int:
            """
            returns the max balls you can place while respecting the minimum distance.
            """
            
            lastBallPlaced = position[0]
            numBalls = 1
            for newPos in position[1:]:
                if newPos - lastBallPlaced >= minDistance:
                    numBalls += 1
                    lastBallPlaced = newPos
            
            return numBalls
        
        position = sorted(position)
        
        bestDistance = 1
        low, high = 1, max(position) - min(position)
        
        while low <= high:
            mid = (low + high)//2
            
            if maxBallsPossible(mid) >= m:
                low = mid + 1
                bestDistance = max(bestDistance, mid)
            else:
                high = mid - 1
        
        return bestDistance
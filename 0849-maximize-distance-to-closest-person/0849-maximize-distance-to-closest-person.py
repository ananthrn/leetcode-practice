class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        positions = [ind for ind, seat in enumerate(seats) if seat == 1]
        
        n = len(seats)
        maxDiff = 0
        
        for ind, pos in enumerate(positions[:-1]):
            nextPos = positions[ind + 1]
            
            maxDiffHere = (nextPos - pos)//2
            
            maxDiff = max(maxDiff, maxDiffHere)
        
        maxDiff = max(maxDiff, positions[0] - 0, n - 1 - positions[-1])
        
        return maxDiff
            
            
        
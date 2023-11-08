class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t == 0 or t >= 2
        
        finalDist = max(abs(sx - fx), abs(sy - fy))
        print("finalDist: ", finalDist)
        print("t: ", t)
        
        return finalDist <= t
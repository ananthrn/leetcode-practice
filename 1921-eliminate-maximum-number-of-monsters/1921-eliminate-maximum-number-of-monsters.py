class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsters = sorted(zip(dist, speed), key=lambda x: (x[0]/x[1]))
        
        for minute, (d, s) in enumerate(monsters):
            if d - minute * s <= 0:
                return minute
            
        
        return len(monsters)
        
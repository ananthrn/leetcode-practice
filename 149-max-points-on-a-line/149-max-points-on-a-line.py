from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def sameSlope(p1: List[int], p2: List[int], p3: List[int]):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return (x1 - x2) * (y2 - y3) == (x2 - x3) * (y1 - y2)
        
        points = sorted(points)
        n = len(points)
        
        c = defaultdict(int)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]
                    if sameSlope(p1, p2, p3):
                        print("yes:!")
                        c[tuple(p1 + p2)] +=1
        
        print("c:, ", c)
        if len(c) == 0:
            return min(2, len(points))
        
        return max(c.values()) + 2
        
import numpy as np
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cnt = {tuple(point): 1 for point in points}
        area = np.inf
        for j, (x, y) in enumerate(points):
            for x2, y2 in points[j + 1:]:
                if x != x2 and y != y2:
                    if cnt.get((x, y2), 0) == 1 and cnt.get((x2, y),0) == 1:
                        area = min(area, abs(x - x2) * abs(y - y2))
        
        return 0 if area == np.inf else area
        
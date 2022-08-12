from collections import defaultdict
class DetectSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for diagPoint, diagPointCount in self.pointCount.items():
            if diagPoint[0] != point[0] and diagPoint[1] != point[1]:
                if abs(point[0] - diagPoint[0]) == abs(point[1] - diagPoint[1]):
                    count1 = self.pointCount.get((diagPoint[0], point[1]), 0)
                    count2 = self.pointCount.get((point[0], diagPoint[1]), 0)

                    ans += diagPointCount * count1 * count2
        
        return ans
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
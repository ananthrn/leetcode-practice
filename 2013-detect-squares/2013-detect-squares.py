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
        for diagPoint in self.points:
            if diagPoint[0] != point[0] and diagPoint[1] != point[1]:
                if abs(point[0] - diagPoint[0]) == abs(point[1] - diagPoint[1]):
                    count1 = self.pointCount[(diagPoint[0], point[1])]
                    count2 = self.pointCount[(point[0], diagPoint[1])]
                    # count3 = self.pointCount[tuple(diagPoint)]

                    ans += count1*count2
        
        return ans
                
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
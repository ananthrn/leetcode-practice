class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sortedPoints = sorted(points, key=lambda point: point[0])
        
        maxWidth = max([sortedPoints[i+1][0] - sortedPoints[i][0] for i in range(len(points) - 1) ])
        return maxWidth
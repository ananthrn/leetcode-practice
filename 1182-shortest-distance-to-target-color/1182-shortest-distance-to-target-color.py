class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        closestColor = [
            n * [math.inf]
            for _ in range(4)
        ]
        
        # closestColor = collections.defaultdict(list)
        
        for colorVal in range(1, 4):
            currentIndex = None
            for ind in range(len(colors)):
                if colors[ind] == colorVal:
                    currentIndex = ind
                    closestColor[colorVal][ind] = 0
                elif currentIndex is not None:
                    closestColor[colorVal][ind] = min(closestColor[colorVal][ind], abs(ind - currentIndex))
            
            currentIndex = None
            for ind in range(len(colors) -1, -1, -1):
                if colors[ind] == colorVal:
                    currentIndex = ind
                    closestColor[colorVal][ind] = 0
                elif currentIndex is not None:
                    closestColor[colorVal][ind] = min(closestColor[colorVal][ind], abs(ind - currentIndex))
            
        
        ans = [closestColor[color][index] for (index, color) in queries]
        
        ans = [val if val != math.inf else -1 for val in ans]
        return ans
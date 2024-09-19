class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        
        rowBlackCount = collections.Counter()
        colBlackCount = collections.Counter()
        
        for r in range(m):
            for c in range(n):
                if picture[r][c] == "B":
                    rowBlackCount[r] += 1
                    colBlackCount[c] += 1
        
        
        lonelyPixels = [
            (r, c) for r in range(m) for c in range(n) if picture[r][c] == "B" and rowBlackCount[r] == 1 and colBlackCount[c] == 1
        ]
        
        return len(lonelyPixels)
                
        
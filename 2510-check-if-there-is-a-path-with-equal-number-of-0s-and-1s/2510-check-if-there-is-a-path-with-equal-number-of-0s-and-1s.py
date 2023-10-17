class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        @cache
        def checkPath(r: int, c: int, onesDelta: int) -> bool:
            if not (0 <= r < m and 0 <= c < n):
                return False
            
            if (r, c) == (0, 0):
                thisDelta = -1 if grid[r][c] == 0 else 1
                # print("r, c: ", r, c)
                # print("thisAnser: ", onesDelta + thisDelta == 0)
                return onesDelta + thisDelta == 0
            
            thisDelta = -1 if grid[r][c] == 0 else 1
            
            return checkPath(r-1, c, thisDelta + onesDelta) or checkPath(r, c -1 , thisDelta + onesDelta)
        
        m, n = len(grid), len(grid[0])
        
        return checkPath(m - 1, n - 1, 0)
        
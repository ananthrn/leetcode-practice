class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        num_ones = len(list((r, c) for r in range(m) for c in range(n) if grid[r][c] == 1))
        best_x = sorted(list( r for r in range(m) for c in range(n) if grid[r][c] == 1))[num_ones//2]
        best_y = sorted(list(c for r in range(m) for c in range(n) if grid[r][c] == 1))[num_ones//2]
        
        print(best_x, best_y)
        return sum(abs(r - best_x) + abs(c - best_y) for r in range(m) for c in range(n) if grid[r][c] == 1) 
    
        
        
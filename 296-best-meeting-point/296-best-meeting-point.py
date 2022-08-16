class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        
        x_pos = sorted([r for r in range(m) for c in range(n) if grid[r][c] == 1])
        y_pos = sorted([c for r in range(m) for c in range(n) if grid[r][c] == 1])
        
        med_x = x_pos[(len(x_pos) - 1)//2]
        # med_x_plus_1 = x_pos[(len(x_pos) - 1)//2 + 1]
        
        med_y = y_pos[(len(y_pos) - 1)//2]
        # med_y_plus_1 = y_pos[(len(y_pos) - 1)//2 + 1]
        
        # min_x = min(sum([abs(x - med_x) for x in x_pos]), sum([abs(x - med_x_plus_1) for x in x_pos]))
        
        # min_y = min(sum([abs(y - med_y) for y in y_pos]), sum([abs(y - med_y_plus_1) for y in y_pos]))
        min_x = sum([abs(x - med_x) for x in x_pos])
        min_y = sum([abs(y - med_y) for y in y_pos])
        return min_x + min_y
        
        
        
        
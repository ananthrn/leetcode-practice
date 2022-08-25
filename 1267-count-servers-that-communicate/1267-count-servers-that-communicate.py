from collections import defaultdict
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        servers = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
        
        rowCount = defaultdict(int)
        colCount = defaultdict(int)
        
        for srv_r, srv_c in servers:
            rowCount[srv_r] += 1
            colCount[srv_c] += 1
            
        
        ans = len([1 for srv_r, srv_c in servers if (rowCount[srv_r] >= 2 or colCount[srv_c] >= 2)])
        # for srv_r, srv_c in servers:
        #     if rowCount[srv_r] or colCount[srv_c] > 2:
        #         ans += 1
                
        return ans
        
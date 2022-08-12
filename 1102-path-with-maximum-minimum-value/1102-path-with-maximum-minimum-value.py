from sortedcontainers import SortedList

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        
        m, n = len(grid), len(grid[0])
        dp = [ n * [None] for i in range(m)]
        
        cache = {}
        seen = {}
        # minVal = 0
        
        def dfs(r, c, minVal):
            if grid[r][c] < minVal:
                return False
            
            if (r, c) == (m-1, n-1):
                cache[(r, c)] = True
                return True
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            seen[(r, c)] = 1
            for nxt_r, nxt_c in (
                    (r, c + 1),
                    (r, c - 1),
                    (r + 1, c),
                    (r - 1, c)):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    if grid[nxt_r][nxt_c] >= minVal and (nxt_r, nxt_c) not in seen:
                        check = dfs(nxt_r, nxt_c, minVal)
                        if check:
                            cache[(r, c)] = True
                            return True
                
            
            cache[(r, c)] = False
            seen[(r, c)] = 2
            return False
            
            
            
            
        def binSearch(start, end):
            nonlocal cache, seen
            bestVal = start - 1
            while start <= end:
                mid = (start + end)//2
                cache = {}
                seen = {}
                check = dfs(0, 0, mid)
                
                if check:
                    bestVal = max(bestVal, mid)
                    start = mid + 1
                else:
                    end = mid - 1
            
            return bestVal
        
        bestMax = binSearch(0, int(1e9))
        return bestMax
#         def dijkstra():
#             Q = SortedList()
#             Q.add((grid[0][0], 0, 0))
#             seen = [ n * [False] for i in range(m)]
            
#             while len(Q) > 0:
#                 # print("Q: ", Q)
#                 val, r, c = Q.pop()
                
#                 if not seen[r][c]:
#                     seen[r][c] = True
#                     dp[r][c] = val
                
#                 if (r, c) == (m-1, n-1):
#                     return
                
#                 for nxt_r, nxt_c in (
#                     (r, c + 1),
#                     (r, c - 1),
#                     (r + 1, c),
#                     (r - 1, c)
#                 ):  
#                     if 0 <= nxt_r < m and 0 <= nxt_c < n:
#                         if not seen[nxt_r][nxt_c]:
#                             Q.add((min(val, grid[nxt_r][nxt_c]), nxt_r, nxt_c))
        
#         dijkstra()
        
#         return dp[m-1][n-1]
            

        
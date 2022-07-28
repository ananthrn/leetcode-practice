class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        def bfs(time: int) -> bool:
            if grid[0][0] > time:
                return False
            
            Q = deque([[0, 0]])
            seen = defaultdict(bool)
            # print("time: ", time)
            while len(Q) > 0:
                r, c = Q.popleft()
                
                if seen[(r, c)]:
                    continue
                    
                seen[(r, c)] = True
                
                # print("(r, c): ", r, c)
                # print()
                if (r, c) == (n-1, n-1):
                    return True
                
                for nxt_r, nxt_c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    try:
                        if(0 <= nxt_r < n and 0 <= nxt_c < n):
                            if(grid[nxt_r][nxt_c] <= time and seen[(nxt_r, nxt_c)] == False):
                                # seen[(nxt_r, nxt_c)] = True
                                Q.append((nxt_r, nxt_c))
                    except IndexError:
                        pass
            
            return False
        
        start, end, bestTime = 0, n * n, n * n
        print("n :", n)
        while(start <= end):
            mid = (start + end)//2
            
            check = bfs(mid)
            
            if check:
                bestTime = min(bestTime, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return bestTime
        
        
            
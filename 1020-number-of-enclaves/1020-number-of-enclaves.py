class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(src: Tuple[int]) -> bool:
            """
            returns True if it is an enclave and false otherwise
            """
            
            Q = collections.deque([src])
            print("src: ", src)
            print()
            enclave = True
            numElements = 0
            
            while  Q:
                tp = Q.pop()
                print("tp: ", tp)
                
                if tp[0] in (0, m - 1) or tp[1] in (0, n -1):
                    enclave  = False
                
                if not seen[tp]:
                    numElements += 1
                    seen[tp] = True
                    for nxt_r, nxt_c in (
                        (tp[0] + 1, tp[1]),
                        (tp[0] - 1, tp[1]),
                        (tp[0], tp[1] + 1),
                        (tp[0], tp[1] - 1),
                    ):
                        if 0 <= nxt_r < m and 0 <= nxt_c < n:
                            if grid[nxt_r][nxt_c] == 1 and seen[(nxt_r, nxt_c)] == False:
                                Q.appendleft((nxt_r, nxt_c))
            
            print()
            print("enclave: ", enclave)
            print()
            return enclave, numElements
        
        m, n = len(grid), len(grid[0])
        seen = collections.defaultdict(bool)
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not seen[(r, c)]:
                    check, numElements = bfs((r, c))
                    if check:
                        ans += numElements
        return ans        
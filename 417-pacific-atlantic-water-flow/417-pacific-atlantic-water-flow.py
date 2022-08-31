from collections import deque
class Solution:
    def bfs(self, heights: List[List[int]], startPos: List[List[int]], seen: List[List[int]], val: int):
        
        m, n = len(heights), len(heights[0])
        Q = deque(startPos)
        
        for r, c in startPos:
            seen[r][c] += 1
        
        while len(Q) > 0:
            tp_r, tp_c = Q.pop()
            # print("tp_r, tp_c: ")
            for nxt_r, nxt_c in (
                (tp_r, tp_c + 1),
                (tp_r, tp_c - 1),
                (tp_r + 1, tp_c),
                (tp_r - 1, tp_c)
            ):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    if seen[nxt_r][nxt_c] <= val and heights[nxt_r][nxt_c] >= heights[tp_r][tp_c]:
                        seen[nxt_r][nxt_c] += 1
                        Q.append((nxt_r, nxt_c))
        
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacific = (
            [
                (r, 0)
                for r in range(m)
            ] + 
            [
                (0, c)
                for c in range(1, n)
            ]
        )
        
        atlantic = (
            [
                (r, n-1)
                for r in range(m)
            ] + 
            [
                (m-1, c)
                for c in range(0, n -1)
            ]
        )
        
        seenPacific = [n * [0] for _ in range(m)]
        seenAtlantic = [n * [0] for _ in range(m)]
        
        self.bfs(heights, pacific, seenPacific, 0)
        # print("seen pacific: ", seenPacific)
        self.bfs(heights, atlantic, seenAtlantic, 0)
        
        # print("seen pacific and atlantic: ", seen)
        ans = [(r, c) for r in range(m) for c in range(n) if seenPacific[r][c] + seenAtlantic[r][c] == 2]
        
        return ans
        
    
        
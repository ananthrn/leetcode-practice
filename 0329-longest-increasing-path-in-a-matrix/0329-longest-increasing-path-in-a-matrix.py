class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(r, c) -> int:
            maxPath = 0
            
            for nxt_r, nxt_c in (
                (r, c + 1),
                (r, c - 1),
                (r + 1, c),
                (r - 1, c),
            ):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    if matrix[r][c] < matrix[nxt_r][nxt_c]:
                        maxPath = max(maxPath, helper(nxt_r, nxt_c))
            
            
            return maxPath + 1
        
        m, n = len(matrix), len(matrix[0])
        
        return max([
            helper(r, c) for r in range(m) for c in range(n)
        ])
        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def backtrack(row: int, col: int) -> int:
            # currentVal = 0
            
            ans = 0 
            
            for new_row, new_col in [
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col)
            ]:
                if 0 <= new_row < m and 0 <= new_col < n:
                    if matrix[new_row][new_col] > matrix[row][col]:
                        ans = max(ans, backtrack(new_row, new_col))
            
            return ans + 1
        
        
        return max([backtrack(row, col) for row in range(m) for col in range(n)])
        
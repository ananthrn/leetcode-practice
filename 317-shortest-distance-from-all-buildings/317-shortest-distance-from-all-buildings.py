import numpy as np
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        visited = [[0] * n for _ in range(m)]
        total = [[0] * n for _ in range(m)]
        def bfs(row: int, col: int, count: int)-> int:
            min_dist = np.inf
            
            queue = deque([(row, col, 0)])
            steps = 0
            # print("count: ", count)
            # print("row, col: ", row, col)
            while len(queue) > 0:
                tp_row, tp_col, steps = queue.pop()
                # print("tp_row, tp_col: ", tp_row, tp_col)
                # print("visited[tp_row][tp_col]: ", visited[tp_row][tp_col])
                # print()
                steps +=1 
                
                for dir_row, dir_col in dirs:
                    new_row = tp_row + dir_row
                    new_col = tp_col + dir_col
                    
                    if 0 <= new_row < m and 0 <= new_col < n: 
                        # print("new_row, new_col: ", new_row, new_col)
                        # print("visited[new_row][new_col]: ", visited[new_row][new_col])
                        # print()
                        if (visited[new_row][new_col] == -count) and grid[new_row][new_col] == 0:
                            total[new_row][new_col] += steps
                            visited[new_row][new_col] -= 1
                            min_dist = min(min_dist, total[new_row][new_col])
                            queue.appendleft((new_row, new_col, steps))
            
            return min_dist
        
        count = 0
        min_dist = np.inf
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    min_dist = bfs(row, col, count)
                    count += 1
                    # print("visited: ")
                    # print(visited)
                    # print("total")
                    # print(total)
                    # print()
                    # Impossible to reach all buildings from any point
                    if min_dist == np.inf:
                        return -1
        
        return min_dist
                    
            
        
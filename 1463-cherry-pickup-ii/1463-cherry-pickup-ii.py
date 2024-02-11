class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(row, robot_1, robot_2) -> int:
            if row == m or not (0 <= robot_1 <= n - 1) or not (0 <= robot_2 <= n - 1):
                return 0
            

            mx = 0
            for robot_1_next in range(robot_1 - 1, robot_1 + 2):
                for robot_2_next in range(robot_2 - 1, robot_2 + 2):
                    mx = max(mx, helper(row + 1, robot_1_next, robot_2_next))
            
            if robot_1 == robot_2:
                # print("row, robot_1, robot_2: ", row, robot_1, robot_2)
                # print("ans: ", mx + grid[row][robot_1])
                # print()
                return mx + grid[row][robot_1]
            else:
                # print("row, robot_1, robot_2: ", row, robot_1, robot_2)
                # print("ans: ", mx + grid[row][robot_1] + grid[row][robot_2])
                # print()
                return mx + grid[row][robot_1] + grid[row][robot_2]
        
        m, n = len(grid), len(grid[0])
        
        return helper(0, 0, n - 1)
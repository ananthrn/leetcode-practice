class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set([(0, 0)])
        dirMap = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        cur_x, cur_y = 0, 0
        for direction in path:
            del_x, del_y = dirMap[direction]
            cur_x += del_x
            cur_y += del_y
            
            if (cur_x, cur_y) in seen:
                return True
            
            seen.add((cur_x, cur_y))
        
        return False
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def checkVisited(r, c, completedMask) -> bool:
            index = r * n + c
            checkBit = (1 << (index)) & completedMask
            return checkBit != 0
        
        def markVisited(r, c, completedMask) -> int:
            index = r * n + c
            
            newMask = completedMask | (1 << index)
            # print("r, c: ", r, c)
            # print("index: ", index)
            # print("completedMask: ", completedMask)
            # print("newMask: ", newMask)
            return newMask
        
        def getOnes(mask) -> int:
            ones = 0
            while mask > 0:
                if mask %2  == 1:
                    ones += 1
                mask /= 2
            return ones
        # def markNotVisited(r, c, completedMask) -> int:
        #     newMask = 
        
        @cache
        def helper(r, c, completedMask)->int:
            binRep = bin(completedMask)
            cnt = collections.Counter(binRep[2:])
            numOnes = cnt['1']
            
            print("r, c:", r, c)
            print("completedMask: ", completedMask)
            print("binRep: ", binRep)
            print("numOnes", numOnes)
            print("numOpenPositions: ", numOpenPositions)
            print()
            if grid[r][c] == 2:
                if numOnes == numOpenPositions:
                    return 1
                else:
                    return 0
            
            ans = 0
            
            for (nxt_r, nxt_c) in (
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            ):
                if 0 <= nxt_r < m and 0 <= nxt_c < n:
                    
                    # print("checckVisited?: ", checkVisited(nxt_r, nxt_c, completedMask))
                    # print()
                    if not checkVisited(nxt_r, nxt_c, completedMask) and grid[nxt_r][nxt_c] != -1:
                        newMask = markVisited(nxt_r, nxt_c, completedMask)
                        print("nxt_r, nxt_c: ", nxt_r, nxt_c)
                        print("completedMask: ", completedMask)
                        print("newMask: ", newMask)
                        print()
                        ans += helper(nxt_r, nxt_c, newMask)
            
            return ans
        
        start_r, start_c = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1][0]
        
        numOpenPositions = len([1 for r in range(m) for c in range(n) if grid[r][c] != -1])
        
        mask = markVisited(start_r, start_c, 0)
        
        print("m, n: ", m, n)
        
        paths = helper(start_r, start_c, mask)
        
        return paths
                
        
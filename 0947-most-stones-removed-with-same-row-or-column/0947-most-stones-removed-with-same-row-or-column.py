class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def bfs(stone: Tuple[int]) -> int:
            Q = collections.deque([stone])
            
            stonesInComponent = 0
            while Q:
                topStone = Q.pop()
                
                if topStone not in visited:
                    stonesInComponent += 1
                    visited.add(topStone)
                    
                    for nextStone in rowStones[topStone[0]]:
                        if nextStone not in visited:
                            Q.append(nextStone)
                    
                    for nextStone in colStones[topStone[1]]:
                        if nextStone not in visited:
                            Q.append(nextStone)
                            
            return stonesInComponent
        
        visited = set()
        
        stones = [(r, c) for r, c in stones]
        
        
        rowStones = collections.defaultdict(set)
        colStones = collections.defaultdict(set)
        
        for r, c in stones:
            rowStones[r].add((r, c))
            colStones[c].add((r, c))
        
        totalStonesRemoved = 0
        
        for stone in stones:
            if stone not in visited:
                totalStonesRemoved += bfs(stone) - 1
        
        return totalStonesRemoved
        
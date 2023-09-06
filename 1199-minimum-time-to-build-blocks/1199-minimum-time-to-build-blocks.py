class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        
        cache = [[None] * (len(blocks) + 1) for _ in range(len(blocks) + 1)]
        
        blocks = sorted(blocks, reverse=True)
        # @lru_cache(maxsize=1000000)
        def backtrack(index: int, numWorkers: int) -> int:
            if index >= len(blocks):
                return 0
            
            if numWorkers <= 0:
                return inf
            
            workersNeeded = len(blocks) - index
            
            if numWorkers >= workersNeeded:
                return blocks[index]
            
            if cache[index][numWorkers] != None:
                return cache[index][numWorkers]
        
            cache[index][numWorkers] = min(split + backtrack(index, min(2 * numWorkers, workersNeeded)), max(blocks[index], backtrack(index + 1, numWorkers - 1)))
            
            return cache[index][numWorkers]            
        
        ans = backtrack(0, 1)
        
        return ans
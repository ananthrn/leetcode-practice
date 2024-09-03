class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalSum = sum(chalk)
        
        k = k % totalSum
        
        for index, pieces in enumerate(chalk):
            if pieces > k :
                return index
            k -= pieces
        
        return -1
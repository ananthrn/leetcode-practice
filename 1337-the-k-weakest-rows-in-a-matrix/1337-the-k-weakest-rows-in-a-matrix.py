class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        soldiers = list(map(lambda row: sum(row), mat))
        
        sortedIndices = sorted([ind for ind in range(len(mat))], key = lambda ind: (soldiers[ind], ind))
        
        return sortedIndices[:k]
        
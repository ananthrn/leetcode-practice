class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        
        seen = {}
        def backtrack(first, cur):
            if len(cur) == k:
                combs.append(cur[:])
            
            for j in range(first, n + 1):
                cur.append(j)
                backtrack(j + 1, cur)
                cur.pop()
        backtrack(1, [])
        return combs
            
                
            
            
            
        
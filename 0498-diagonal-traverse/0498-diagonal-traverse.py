class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # Key idea: diagonal nubmer is 
        m, n = len(mat), len(mat[0])
        diagNumToElements = collections.defaultdict(list)
        
        for r in range(m):
            for c in range(n):
                # Append element to the appropriate diagonal number
                diagNumToElements[r + c].append(mat[r][c])
        
        
        ans = []
        
        for diagNum, elems in sorted(diagNumToElements.items()):
            if diagNum%2 == 0:
                ans += elems[::-1]
            else:
                ans += elems
        
        return ans
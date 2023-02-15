class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answers = set()
        currentSet = set()
        def backtrack():
            currentSum = sum(currentSet)
            currentLen = len(currentSet)
            
            if currentLen == k and currentSum == n:
                answers.add(tuple(sorted(currentSet)))
            
            if currentLen >= k:
                return
            
            if currentSum >= n:
                return
            
            for nextVal in range(1, 10):
                if nextVal not in currentSet:
                    currentSet.add(nextVal)
                    backtrack()
                    currentSet.remove(nextVal)
        
        backtrack()
        
        return answers
            
        
        
        
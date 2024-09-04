class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        @cache
        def backtrack(currentIndex: int, targetHeads: int) -> float:
            if targetHeads < 0 or targetHeads > currentIndex + 1:
                return 0.0
            
            if currentIndex == 0:
                if targetHeads == 1:
                    return prob[currentIndex]
                elif targetHeads == 0:
                    return 1 - prob[currentIndex]
                else:
                    assert False, f"CurrentIndex: {currentIndex}, targetHeads: {targetHeads}"
            
            return prob[currentIndex] * backtrack(currentIndex - 1, targetHeads - 1) + (1 - prob[currentIndex]) * backtrack(currentIndex - 1, targetHeads)
        
        answer = backtrack(len(prob) - 1, target)
        
        return answer
        
        
        
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def backtrack(currentIndex: int, m: int) -> int:
            if currentIndex >= len(piles):
                return 0
            
            aliceAnswer = 0
            
            currentSum = 0
            for possibleIndex in range(currentIndex, min(currentIndex + 2 * m, len(piles))):
                currentSum += piles[possibleIndex]
                newM = max(m, possibleIndex - currentIndex + 1)
                bobAnswer = backtrack(possibleIndex + 1, newM)
                remainingAlice = (stonesSuffixSum[possibleIndex + 1] - bobAnswer) if possibleIndex + 1 < len(piles) else 0 
                aliceAnswer = max(aliceAnswer, remainingAlice + currentSum)
            
            return aliceAnswer
        
        stonesSuffixSum = list(piles)
        
        for j in range(len(piles) - 2, -1, -1):
            stonesSuffixSum[j] += stonesSuffixSum[j + 1]
        
        return backtrack(0, 1)
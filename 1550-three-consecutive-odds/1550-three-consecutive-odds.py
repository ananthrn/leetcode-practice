class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        
        for val in arr:
            if val%2 == 1:
                oddCount += 1
                if oddCount >= 3:
                    return True
            else:
                oddCount = 0
        
        return False
        
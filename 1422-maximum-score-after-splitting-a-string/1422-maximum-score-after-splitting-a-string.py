class Solution:
    def maxScore(self, s: str) -> int:
        return max(
            sum([1 for char in s[0:i] if char == '0']) 
            + sum([1 for char in s[i:] if char == '1'])
            for i in range(1, len(s))
        )
        
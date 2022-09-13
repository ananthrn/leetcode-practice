class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        start, end = 0, len(tokens) - 1
        
        score = 0
        ans = 0
        while start <= end:
            if power >= tokens[start]:
                score += 1
                power -= tokens[start]
                start += 1
                ans = max(ans, score)
            elif power < tokens[start] and score > 0:
                score -= 1
                power += tokens[end]
                end -= 1
            else:
                return ans
            
        
        
        
        return ans
        
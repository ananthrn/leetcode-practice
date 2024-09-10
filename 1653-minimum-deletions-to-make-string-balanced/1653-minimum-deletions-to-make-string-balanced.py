class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        n = len(s)
        
        count_b_left = len(s) * [0]
        count_a_right = len(s) * [0]
        
        count_b_left[0] = 1 if s[0] == 'b' else 0
        
        
        for index in range(1, n):
            count_b_left[index] = count_b_left[index - 1] + (1 if s[index] == 'b' else 0)
        
        
        count_a_right[-1] = 1 if s[-1] == 'a' else 0
        
        for index in range(2, n + 1):
            count_a_right[-index] = count_a_right[-index + 1] + (1 if s[-index] == 'a' else 0)
        
        
        minimumDeletions = n
        
        for index in range(n):
            minimumDeletions = min(minimumDeletions, -1 + count_a_right[index] + count_b_left[index])
        
        return minimumDeletions
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        currentStreak = []
        
        cnt = collections.Counter()
        
        for arr in arrays:
            cnt += collections.Counter(arr)
        
        
        currentStreak = [currentValue for currentValue in range(1, 101) if cnt[currentValue] == len(arrays)]
        
        return currentStreak
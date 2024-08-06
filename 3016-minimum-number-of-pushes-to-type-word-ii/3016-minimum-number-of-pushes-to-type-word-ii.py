class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = collections.Counter(word)
        
        totalCost = 0 
        
        currentPushes = 1
        
        keys = 8
        
        for freq in sorted(cnt.values(), reverse=True):
            totalCost += currentPushes * freq
            keys -= 1
            
            if keys == 0:
                keys = 8
                currentPushes += 1
        
        
        return totalCost
        
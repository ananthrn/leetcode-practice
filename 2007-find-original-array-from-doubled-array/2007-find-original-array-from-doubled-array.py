from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed = sorted(changed)
        cnt = Counter(changed)
        
        
        ans = []
        for elem in changed:
            if elem == 0:
                if cnt[elem] %2 !=0:
                    return []
                
                ans.extend(cnt[elem]//2 * [elem])
                cnt[elem] = 0
            elif elem > 0:
                currentCount = cnt[elem]
                if cnt[2*elem] < currentCount:
                    return []
                ans.extend(currentCount * [elem])
                cnt[elem] = 0
                cnt[2 * elem] -= currentCount
        
        return ans
        
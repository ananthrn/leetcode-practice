
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cntRansom = Counter(ransomNote)
        cntMagazine = Counter(magazine)
        
        for char, cnt in cntRansom.items():
            if cntMagazine[char] < cnt:
                return False
        
        return True
        
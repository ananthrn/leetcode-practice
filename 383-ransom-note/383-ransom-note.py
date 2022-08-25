class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cntRansom = dict()
        cntMagazine = dict()
        
        for char in ransomNote:
            cntRansom[char] = cntRansom.get(char, 0) + 1
        
        for char in magazine:
            cntMagazine[char] = cntMagazine.get(char, 0) + 1
        
        
        for char, cnt in cntRansom.items():
            if cntMagazine.get(char, 0) < cnt:
                return False
        
        return True
        
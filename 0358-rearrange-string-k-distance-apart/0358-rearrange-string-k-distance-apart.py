class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        cnt = Counter(s)
        if k <= 1:
            return s
        # if max(cnt.values()) > len(s)//k:
        #     return ""
        
        lastAppeared = dict()
        
        newString = ""
        
        for i in range(len(s)):
            bestChar = ''
            bestFreq = 0
            
            for char, count in cnt.items():
                if char not in lastAppeared or lastAppeared[char] <= i-k:
                    if count > bestFreq:
                        bestFreq = count
                        bestChar = char
            
            if bestChar != '':
                cnt[bestChar] -= 1
                lastAppeared[bestChar] = i
                newString += bestChar
            else:
                return ""
        
        return newString
                    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[0:len(s1)])
        
        if(cnt1 == cnt2):
            return True
        
        # print("cnt1: ", cnt1)
        for j in range(len(s1), len(s2)):
            cnt2[s2[j]] += 1
            cnt2[s2[j- len(s1)]] -=1
            
            # print("s2[i:j]: ", s2[j - len(s1) + 1: j + 1])
            # print("cnt2: ", cnt2)
            if cnt1 == cnt2:
                return True
        
        return False
        
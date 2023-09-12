class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        cntCnt = Counter(cnt.values())
        
        print(cntCnt.items())
        
        freeFrequencies = set([freq for freq in range(max(cntCnt.keys()))])
        
        for val in cntCnt.keys():
            if val in freeFrequencies:
                freeFrequencies.remove(val)
        
        maxFreq = max(freeFrequencies) 
        
        ans = 0
        
        print("cntCnt: ", cntCnt)
        print("freeFrequencies: ", freeFrequencies)
        for val in sorted(cntCnt.keys(), reverse=True):
            currentFreq = cntCnt[val]
            if currentFreq > 1:
                for nxt in range(0, currentFreq - 1):
                    maxFreq = max(min(maxFreq, val - 1), 0)
                    while maxFreq > 0 and maxFreq not in freeFrequencies:
                        maxFreq -=1
                    if maxFreq > 0:
                        freeFrequencies.remove(maxFreq)
                    ans += val - maxFreq
                
        return ans 
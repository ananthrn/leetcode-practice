class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        cntCnt = Counter(cnt.values())
        
        print(cntCnt.items())
        
        freeVals = set([freq for freq in range(max(cntCnt.keys()))])
        
        for val in cntCnt.keys():
            if val in freeVals:
                freeVals.remove(val)
        
        maxFreeVal = max(freeVals) 
        
        ans = 0
        
        print("cntCnt: ", cntCnt)
        print("freeVals: ", freeVals)
        for val in sorted(cntCnt.keys(), reverse=True):
            currentFreq = cntCnt[val]
            if currentFreq > 1:
                for nxt in range(0, currentFreq - 1):
                    maxFreeVal = max(min(maxFreeVal, val - 1), 0)
                    while maxFreeVal > 0 and maxFreeVal not in freeVals:
                        maxFreeVal -=1
                    if maxFreeVal > 0:
                        freeVals.remove(maxFreeVal)
                    ans += val - maxFreeVal
                
        return ans 
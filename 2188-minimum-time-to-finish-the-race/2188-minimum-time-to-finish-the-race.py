import numpy as np
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        
        dp = numLaps * [np.inf]
        
        dp[0] = min([f for f, r in tires])
        
        minConsec = 20 * [0]
        
        sumArray = list([f for f, r in tires])
        for consecLaps in range(1, 19):
            minConsec[consecLaps] = min(sumArray)
            for i in range(len(sumArray)):
                f, r = tires[i]
                sumArray[i] = (sumArray[i] * r) + f
                
            
        for lap in range(1, numLaps):
            # compute minimum for this lap
            for prev_lap in range(max(0, lap - 17), lap + 1):
                consecLaps = lap - prev_lap + 1
                minTire = minConsec[consecLaps] #np.min([f * (((r ** consecLaps) - 1)/(r - 1)) for f, r in tires])
                # minTireReal = min([f * (((r ** consecLaps) - 1)/(r - 1)) for f, r in tires])
                # assert int(minTire) == int(minTireReal), print(f"minTire: {minTire}, minTireReal: {minTireReal}" )
                minPrev = dp[prev_lap - 1] + changeTime if prev_lap > 0 else 0
                
                dp[lap] = min(dp[lap], int(minTire) + minPrev)
        
        # print("dp: ", dp)
        return dp[numLaps - 1]
        
        
        
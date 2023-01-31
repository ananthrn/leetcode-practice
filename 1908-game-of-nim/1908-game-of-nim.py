class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def helper(piles):
            pileList = list(piles)
            
            for ind in range(len(pileList)):
                
                if pileList[ind] > 0:
                    pileNum = pileList[ind]
                    for newPileNum in range(0, pileNum):
                        pileList[ind] = newPileNum
                        
                        if not helper(tuple(pileList)):
                            return True
                    
                    pileList[ind] = pileNum
                    
            
            return False
        
        return helper(tuple(piles))
        
        
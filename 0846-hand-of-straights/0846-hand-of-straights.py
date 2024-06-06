class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        cnt = collections.Counter(hand)
        
        handsRemaining = len(hand)
        
        
        
        while handsRemaining:
            currentMin = min(cnt.keys())
            for nextHand in range(currentMin, currentMin + groupSize):
                if cnt[nextHand] == 0:
                    return False
                
                cnt[nextHand] -= 1
                
                if cnt[nextHand] == 0:
                    del cnt[nextHand]
                
                handsRemaining -= 1
            
        
        return True
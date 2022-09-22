from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand = sorted(hand)
        c = Counter(hand)
        
        for val in hand:
            if c[val] > 0:
                cnt = c[val]
                
                for nxt_val in range(val, val + groupSize):
                    if c[nxt_val] < cnt:
                        return False
                    c[nxt_val] -= cnt
        
        return True
                    
        
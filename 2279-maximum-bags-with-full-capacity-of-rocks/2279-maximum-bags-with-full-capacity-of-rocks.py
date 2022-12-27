class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        difference = sorted([cap - rock for (cap, rock) in zip(capacity, rocks)])
        
        for ind, diff in enumerate(difference):
            if additionalRocks >= diff:
                additionalRocks -= diff
            else:
                return ind
        
        return len(difference)
        
from sortedcontainers import SortedList
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties)
        defences = SortedList([de for at, de in properties])
        
        j = 0
        
        ans = 0
        for ind, prop in enumerate(properties):
            while j < len(properties) and properties[j][0] == prop[0]:
                defences.discard(properties[j][1])
                j += 1
            
            if len(defences) > 0 and prop[1] < defences[-1]:
                ans += 1
        
        return ans
        
        
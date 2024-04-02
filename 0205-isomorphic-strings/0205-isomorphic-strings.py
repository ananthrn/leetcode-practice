class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        reverseMapping = dict()
        for chars, chart in zip(s, t):
            if chars in mapping:
                if mapping[chars] != chart:
                    return False
            
            if chart in reverseMapping:
                if reverseMapping[chart] != chars:
                    return False
                
            mapping[chars] = chart
            reverseMapping[chart] = chars
        
        return True
                
        
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return len(diff) == 2 and list(reversed(diff[0])) == diff[1]
    
    def dfs(self, src: str, compNum: int, components: Dict[str, int]):
        components[src] = compNum
                
        for nextStr, nextNum in components.items():
            if src != nextStr and nextNum == 0 and self.areAlmostEqual(src, nextStr):
                self.dfs(nextStr, compNum, components)
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        components = {string: 0 for string in strs}
        
        compNum = 0
        for string in strs:
            if components[string] == 0:
                compNum += 1
                self.dfs(string, compNum, components)
        
        return compNum
            
            
            
        
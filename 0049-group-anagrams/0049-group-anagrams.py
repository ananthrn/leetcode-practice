class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strToGroup = collections.defaultdict(list)
        
        for string in strs:
            strToGroup[str(sorted(string))].append(string)
        
        return strToGroup.values()
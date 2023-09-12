class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizeToIds = collections.defaultdict(list)
        
        for ind, groupSize in enumerate(groupSizes):
            groupSizeToIds[groupSize].append(ind)
            
        ans = []
        
        for groupSize, allIndices in groupSizeToIds.items():
            currentGroup = []
            for ind in allIndices:
                currentGroup.append(ind)
                if len(currentGroup) == groupSize:
                    ans.append(currentGroup)
                    currentGroup = []
        
        return ans
    
    
        
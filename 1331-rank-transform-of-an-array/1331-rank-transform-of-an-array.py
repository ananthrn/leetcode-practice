class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankMap = {
            key: index + 1 for index, key in enumerate(sorted(collections.Counter(arr).keys()))
        }
        
        return list(map(rankMap.get, arr))
        
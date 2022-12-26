class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        
        prefSums = list(nums)
        
        for ind in range(1, len(prefSums)):
            prefSums[ind] += prefSums[ind - 1]
        
        ans = []
        
        for query in queries:
            ind = bisect.bisect_right(prefSums, query)
            ans.append(ind)
        
        return ans
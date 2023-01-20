class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        def isBetter(list1, list2):
            return list1[1] - list1[0] < list2[1] - list2[0] or ((list1[1] - list1[0] == list2[1] - list2[0]) and list1[0] < list2[0])
        
        heap = [
            (lis[0], lisIndex, 0) for lisIndex, lis in enumerate(nums)
        ]
        
        heapq.heapify(heap)
        
        ans = -10e9, 10e9
        
        right = max(val[0] for val in heap)
        
        while len(heap) > 0:
            
            left, i, j = heapq.heappop(heap)
            
            if right - left < ans[1] - ans[0]:
                ans = left, right
            
            if j + 1 < len(nums[i]):
                right = max(right, nums[i][j+1])
                heapq.heappush(heap, (nums[i][j+1], i, j + 1))
            else:
                return ans
            
        
        return ans
        
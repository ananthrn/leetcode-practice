class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flipCount = 0
        
        flipped = collections.deque()
        
        for ind, val in enumerate(nums):
            if flipped and flipped[0] <= ind - k:
                flipped.popleft()
            # check if the bit is now 0, 
            if len(flipped) % 2 == val:
                if ind + k - 1 >= len(nums):
                    return -1
                
                flipped.append(ind)
                flipCount += 1
        
        return flipCount
            
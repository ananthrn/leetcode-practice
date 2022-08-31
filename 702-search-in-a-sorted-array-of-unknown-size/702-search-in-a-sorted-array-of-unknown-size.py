# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
import sys

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        MAXVAL = int(2**31) - 1
        
        sz = 1
        
        while reader.get(sz - 1) != MAXVAL:
            sz *= 2
        
        
        start  = 0
        end = sz
        
        while start <= end:
            mid = (start + end)//2
            
            val = reader.get(mid)
            
            if val > target:
                end = mid - 1
            elif val < target:
                start = mid + 1
            else:
                return mid
        
        return -1
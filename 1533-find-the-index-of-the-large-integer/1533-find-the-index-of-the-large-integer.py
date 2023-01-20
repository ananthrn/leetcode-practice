# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        def helper(l, r) -> int:
            if r == l:
                return l
            
            size = r - l + 1
            
            if size %2 == 0:
                mid = (r + l)//2
                check = reader.compareSub(l, mid, mid + 1, r)
                if check == 0:
                    return None
                elif check == 1:
                    return helper(l, mid)
                elif check == -1:
                    return helper(mid + 1, r)
            else:
                mid = (r + l)//2
                
                check = reader.compareSub(l, mid - 1, mid + 1, r)
                
                if check == 0:
                    return mid
                elif check == 1:
                    return helper(l, mid - 1)
                elif check == -1:
                    return helper(mid + 1, r)
                
                    
            
            
                
        
        
        length = reader.length()
        
        return helper(0, length - 1)
        
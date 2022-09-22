from collections import Counter
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenNums = Counter([num for num in nums if num %2 == 0])
        oddNums = Counter([num for num in nums if num %2 == 1])
        evenSum = sum([num for num in nums if num %2 == 0])
        
        ans = []
        for val, index in queries:
            oldVal = nums[index]
            newVal = nums[index] + val
            nums[index] += val
            
            if oldVal % 2 == 0:
                evenNums[oldVal] -= 1
                evenSum -= oldVal
            else:
                oddNums[oldVal] -=1
            
            if newVal %2 == 0:
                evenNums[newVal] += 1
                evenSum += newVal
            else:
                oddNums[newVal] += 1
            
            ans.append(evenSum)
        
        return ans
        
        
            
        
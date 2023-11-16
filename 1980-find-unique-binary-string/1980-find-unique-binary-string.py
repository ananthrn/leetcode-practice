class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numSet = set(nums)
        n = len(nums[0])
        
        for ind in range(2 ** n):
            binRep = bin(ind)[2:]
            binRep = (n - len(binRep)) * "0" + binRep
            
            if binRep not in numSet:
                return binRep
        
        return n *"0"
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        bn = bin(n)
        
        return sum(int(char) for char in bn[2:])
        
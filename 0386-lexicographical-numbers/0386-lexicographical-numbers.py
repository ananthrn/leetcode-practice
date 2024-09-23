class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        sortedStrings = sorted([str(num) for num in range(1, n + 1)])
        
        return [int(val) for val in sortedStrings]
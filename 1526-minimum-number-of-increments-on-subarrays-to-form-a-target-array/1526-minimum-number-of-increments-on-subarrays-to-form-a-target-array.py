class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return sum(
            max(val - prev, 0) for val, prev in zip(target, [0] + target)
        )
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return len(
            [
                1 for height, sortedHeight in zip(heights, sorted(heights)) if height != sortedHeight
            ]
        )
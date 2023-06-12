class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        smallestIndex = len(letters)
        
        while start <= end:
            mid = (end + start)//2
            if letters[mid] > target:
                smallestIndex = min(smallestIndex, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return letters[smallestIndex] if smallestIndex < len(letters) else letters[0]
        
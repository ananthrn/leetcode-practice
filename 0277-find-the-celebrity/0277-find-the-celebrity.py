# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def everyoneKnows(candidate):
            return all([
                knows(other, candidate) for other in range(n) if other != candidate
            ]
            ) and not any(
                [
                    knows(candidate, other) for other in range(n) if other != candidate
                ]
            )
        
        
        currentCandidate = 0
        
        for candidate in range(1, n):
            if knows(currentCandidate, candidate):
                currentCandidate = candidate
        
        
        return currentCandidate if everyoneKnows(currentCandidate) else -1
        
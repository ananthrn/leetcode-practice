class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lowerBound = (len(b) + len(a) - 1)//len(a) # same as ceil(len(a)/len(b))
        
        for reps in (lowerBound, lowerBound + 1):
            if b in reps * a:
                return reps
        
        return -1
        
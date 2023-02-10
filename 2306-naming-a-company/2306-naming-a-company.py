class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        letterToSuffix = collections.defaultdict(set)
        
        for idea in ideas:
            letterToSuffix[idea[0]].add(idea[1:])
        
        ans = 0
        
        for charA, setA in letterToSuffix.items():
            for charB, setB in letterToSuffix.items():
                if charA != charB:
                    mutual = len(setA.intersection(setB))
                    ans += (len(setA) - mutual) * (len(setB) - mutual)
        
        return ans
        
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def checkCounter(counter1, counter2):
            return all(
                [
                    counter2[key] >= val for key, val in counter1.items()
                ]
            )
        
        c = Counter()
        
        for word in words2:
            c |= Counter(word)
        
        print("c", c)
        return list(filter(lambda word: checkCounter(c, Counter(word)), words1 ))
    
        
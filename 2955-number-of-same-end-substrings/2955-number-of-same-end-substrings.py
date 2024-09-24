class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        def getAnswerFromCounter(counter: collections.Counter) -> int:
            return sum((val * (val + 1))//2 for val in counter.values())
        
        n = len(s)
        
        counters = n * [None]
        
        counters[0] = collections.Counter(s[0:1])
        
        for index, char in enumerate(s):
            if index == 0:
                counters[0] = collections.Counter(s[0:1])
            else:
                counters[index] = counters[index - 1] + collections.Counter(s[index: index + 1])
        
        answers = []
        for left, right in queries:
            leftCounter = counters[left - 1] if left > 0 else collections.Counter()
            rightCounter = counters[right]
            
            # print("query: ", left, right)
            # print("counter: ", rightCounter - leftCounter)
            
            answers.append(getAnswerFromCounter(rightCounter - leftCounter))
            
        
        return answers
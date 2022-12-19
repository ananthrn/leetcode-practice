from collections import Counter
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        counter = Counter()
        counter[fruits[0]] += 1
        
        n = len(fruits)
        
        answer = 1
        while end < n:
            if len(counter) <= 2:
                answer = max(answer, end - start + 1)
                end += 1
                if end < n:
                    counter[fruits[end]] += 1
            else:
                counter[fruits[start]] -=1
                if counter[fruits[start]] == 0:
                    del counter[fruits[start]]
                
                start += 1
        
        return answer
        
        
        
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        
        most_comm = counter.most_common()
        
        totalSize = len(arr)
        halfSize = totalSize //2
        
        removed = 0
        for val, cnt in most_comm:
            totalSize -= cnt
            removed +=1
            if totalSize <= halfSize:
                return removed
        
        return removed
            
        
        
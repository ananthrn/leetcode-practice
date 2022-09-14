class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList = sorted(firstList)
        secondList = sorted(secondList)
        
        def intersection(interval1, interval2):
            return [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
        
        
        i, j = 0, 0
        m, n = len(firstList), len(secondList)
        
        ans = []
        while i < m and j < n:
            interval1 = firstList[i]
            interval2 = secondList[j]
            
            intersect = intersection(interval1, interval2)
            
            if intersect[0] <= intersect[1]:
                ans.append(intersect)
            
            if interval1[1] >= interval2[1]:
                j += 1
            else:
                i += 1
        
        return ans
        
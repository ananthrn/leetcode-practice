class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        
        ans = []
        
        for left, right in intervals:
            print("toBeRemoved:", toBeRemoved)
            print("left, right:", left, right)
            if toBeRemoved[1] <= left or right <= toBeRemoved[0]:
                print("no overlap")
                ans.append([left, right])
            else:
                if left < toBeRemoved[0]:
                    print("left hang")
                    ans.append([left, toBeRemoved[0]])
                if right > toBeRemoved[1]:
                    print("right hang")
                    ans.append([toBeRemoved[1], right])
        
        return ans
            
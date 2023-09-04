class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        
        answers = list((total - numPens * cost1)//cost2 + 1 for numPens in range(0, total//cost1 + 1))
        
        # print("answers:", answers)
        return sum(answers)
            
        
        
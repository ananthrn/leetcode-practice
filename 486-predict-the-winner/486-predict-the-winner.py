class Solution:
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        scores = [0, 0]
        turn = 0
        start = 0
        end = len(nums) - 1
        @cache
        def dfs(start, end, turn, scores) -> int:
            if start == end:
                scoresNew = list(scores)
                scoresNew[turn] += nums[start]
                # print("here: ")
                return 0 if scoresNew[0] >= scoresNew[1] else 1
            
            startScores = list(scores)
            startScores[turn] += nums[start]
            checkStart = dfs(start + 1, end, 1 - turn, tuple(startScores))
            
            endScores = list(scores)
            endScores[turn] += nums[end]
            checkEnd = dfs(start, end -1, 1 - turn, tuple(endScores))
             
            
            if checkStart == turn or checkEnd == turn:
                return turn
            else:
                return 1 - turn
        
        winner = dfs(start, end, 0, tuple(scores))
        return winner == 0
#         while start <= end:
#             if nums[start] >= nums[end]:
#                 scores[turn] += nums[start]
#                 start += 1
#             else:
#                 scores[turn] += nums[end]
#                 end -= 1
                
#             turn = 1 - turn
        
#         return scores[0] >= scores[1]
        
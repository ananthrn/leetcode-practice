import sortedcontainers
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sortedDiffs = sortedcontainers.SortedList(
           [ [diff, prof] for diff, prof in zip(difficulty, profit)]
        )
        
        for ind in range(1, len(sortedDiffs)):
            sortedDiffs[ind][1] = max(sortedDiffs[ind][1], sortedDiffs[ind - 1][1])
        
        answer = 0
        print("sortedDiffs: ", sortedDiffs)
        for work in worker:
            index = sortedDiffs.bisect_left([work, inf])
            print("work:", work)
            print("index - 1:", index - 1)
            print("val: ", sortedDiffs[index - 1])
            print()
            if index != 0:
                answer += sortedDiffs[index - 1][1]
        
        return answer
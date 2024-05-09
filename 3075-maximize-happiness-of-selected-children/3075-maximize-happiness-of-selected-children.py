import sortedcontainers
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        negativeHappiness = list(map(lambda x: - x, happiness))
        heapq.heapify(negativeHappiness)
        
        # currentDelta = 0
        
        answer = 0
        for currentDelta in range(k):
            happiestChild = - heapq.heappop(negativeHappiness)
            # print("happiestChild: ", happiestChild)
            # print("")
            answer += max(0, happiestChild - currentDelta)
        
        return answer
        
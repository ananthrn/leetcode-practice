class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = collections.Counter()
        
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        
        
        # print(degrees)
        # print(sorted(degrees.values()))
        reverseSortedDegreeVals = sorted(degrees.values(), reverse=True)
        answer = sum(
            [
                index * value for  index, value in zip(range(n, 0, -1), reverseSortedDegreeVals)
            ]
        )
        
        return answer
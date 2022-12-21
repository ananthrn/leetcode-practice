class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def manhattanDistance(p1, p2) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        def totalDistance(workerToBikes: Dict[int, int]) -> int:
            distances = [
                manhattanDistance(workers[key], bikes[value]) for key, value in workerToBikes.items()
            ]
            return sum(distances)
        
        
        n = len(workers)
        m = len(bikes)
        
        workerToBikes = dict()
        # bikeToWorkers = dict()
        cache = dict()
        
        def helper(workerIndex, bikeMask: int) -> int:
            if workerIndex >= n:
                return 0
            
            if bikeMask in cache:
                return cache[bikeMask]
            
            ans = 100_000_007
            for bikeIndex in range(m):
                if (bikeMask & (1 << bikeIndex)) == 0:
                    ans = min(
                        ans, 
                        manhattanDistance(workers[workerIndex], bikes[bikeIndex]) + helper(workerIndex + 1, bikeMask | (1 << bikeIndex)))
            # print("workerIndex: ", workerIndex)
            # print("bikeMask: ", format(bikeMask, 'b'))
            # print("ans: ", ans)
            # print()
            cache[bikeMask] = ans
            return ans 

        return helper(0, 0)
        
        
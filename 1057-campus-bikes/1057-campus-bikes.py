class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def distance(worker, bike):
            return sum(
                abs(pos1 - pos2) for (pos1, pos2) in zip(worker, bike)
            )
        
        workerBikePairs = sorted([(distance(worker, bike), workerIndex, bikeIndex) for (workerIndex, worker) in enumerate(workers) for (bikeIndex, bike) in enumerate(bikes)])
                
        
        workerToBikes = len(workers) * [None]
        bikeToWorkers = 0 
        
        totalDist = 0
        
        workersAssigned = 0
        for dist, workerIndex, bikeIndex in workerBikePairs:
            if workersAssigned == len(workers):
                return workerToBikes
            
            if workerToBikes[workerIndex] is None and (bikeToWorkers & (1<< bikeIndex)) == 0:
                workerToBikes[workerIndex] = bikeIndex
                bikeToWorkers |= 1 << bikeIndex
                totalDist += 1
                workersAssigned += 1
            
        
        return [workerToBikes[ind] for ind in range(len(workers))]
            
        
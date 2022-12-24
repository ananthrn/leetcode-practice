class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def distance(worker, bike):
            return sum(
                abs(pos1 - pos2) for (pos1, pos2) in zip(worker, bike)
            )
        
        workerBikePairs = sorted([(distance(worker, bike), workerIndex, bikeIndex) for (workerIndex, worker) in enumerate(workers) for (bikeIndex, bike) in enumerate(bikes)])
                
        
        workerToBikes = dict()
        bikeToWorkers = dict()
        
        totalDist = 0
        for dist, workerIndex, bikeIndex in workerBikePairs:
            if len(workerToBikes) == len(workers):
                return [workerToBikes[ind] for ind in range(len(workers))]
            
            if workerIndex not in workerToBikes and bikeIndex not in bikeToWorkers:
                workerToBikes[workerIndex] = bikeIndex
                bikeToWorkers[bikeIndex] = workerIndex
                totalDist += 1
            
        
        return [workerToBikes[ind] for ind in range(len(workers))]
            
        
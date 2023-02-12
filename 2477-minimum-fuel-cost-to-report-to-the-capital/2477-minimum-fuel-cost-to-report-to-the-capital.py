class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfsHelper(src: int, par: int) -> Tuple[int]:
            totalCars = 0
            totalPeople = 1
            fuelNeeded = 0
            
            for child in graph[src]:
                if child != par:
                    people, cars, fuel = dfsHelper(child, src)
                    
                    totalPeople += people
                    totalCars += cars
                    fuelNeeded += fuel
            
                    
                    
            
            fuelNeeded += totalCars
            
            carsNeeded = (totalPeople + seats - 1)//seats
            
            return totalPeople, carsNeeded, fuelNeeded
        
        # def fuelCompute(src: int) -> int:
        #     pass
        
        people, cars, fuel = dfsHelper(0, -1)
        
        return fuel
        
        
        
        
        
        
        
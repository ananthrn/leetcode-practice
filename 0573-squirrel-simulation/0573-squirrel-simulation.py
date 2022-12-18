class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        nutTreeDists = list(map(lambda nut: abs(nut[0]-tree[0]) + abs(nut[1] - tree[1]), nuts))
        nutSquirrelDists = list(map(lambda nut: abs(nut[0]-squirrel[0]) + abs(nut[1] - squirrel[1]), nuts))
        
        # nutTreeDists 
        
        # compute where nutTreeDist - nutSquirrelDist is maximum
        
        bestIndex = -1
        maxDiff = -50000000
        
        
        for ind, (treeDist, squirrelDist) in enumerate(zip(nutTreeDists, nutSquirrelDists)):
            if treeDist - squirrelDist > maxDiff:
                maxDiff = treeDist - squirrelDist
                bestIndex = ind
                
        
        ans = 2 * sum(nutTreeDists) -nutTreeDists[bestIndex] + nutSquirrelDists[bestIndex] 
        return ans
        
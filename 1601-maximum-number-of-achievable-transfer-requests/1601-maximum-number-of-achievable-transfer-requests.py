class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        @lru_cache(None)
        def getInDegree(reqSat: Set[int]) -> collections.Counter:
            
            ins = [requests[index][1] for index in reqSat]
            
            return collections.Counter(ins)
        
        @lru_cache(None)
        def getOutDegree(reqSat: Set[int]) -> collections.Counter:
            outs = [requests[index][0] for index in reqSat]
            
            return collections.Counter(outs)
        
        @lru_cache(None)
        def checkValid(reqSat: Set[int]) -> bool:
            return getInDegree(reqSat) == getOutDegree(reqSat)
        
        @lru_cache(None)
        def helper(reqSat: Set[int], index: int) -> int:
            
            nonlocal maxRequests, inDegree, outDegree
            
            
            
            # print(f"reqSat: {reqSat}")
            # print(f"checkValid: {checkValid(reqSat)}")
            # print(f"inDegree: {getInDegree(reqSat)}")
            # print(f"outDegree: {getOutDegree(reqSat)}")
            if inDegree == outDegree:
                maxRequests = max(maxRequests, len(reqSat))
            
            if index >= len(requests):
                return
            
            helper(reqSat, index + 1)
            
            inDegree[requests[index][1]] += 1
            outDegree[requests[index][0]] += 1
            helper(reqSat.union({index}), index + 1)
            
            inDegree[requests[index][1]] -= 1
            outDegree[requests[index][0]] -= 1
        
        
        maxRequests = 0
        inDegree = collections.Counter()
        outDegree = collections.Counter()
        
        helper(frozenset(), 0)
        
        return maxRequests
            
            
        
            
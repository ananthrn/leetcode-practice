class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = dict()
        
        for regionlist in regions:
            for i in range(1, len(regionlist)):
                parent[regionlist[i]] = regionlist[0]
        
        p = region1
        q = region2
        
        while p != q:
            p = parent.get(p, region2)
            q = parent.get(q, region1)

        
        return p
        
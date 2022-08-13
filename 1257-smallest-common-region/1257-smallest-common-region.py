class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {region[i]: region[0] for region in regions for i in range(1, len(region))}
        
        p = region1
        q = region2
        
        while p != q:
            p = parent.get(p, region2)
            q = parent.get(q, region1)

        
        return p
        
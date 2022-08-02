class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        setSrc = set(source)
        setTar = set(target)
        
        if len(setTar.difference(setSrc)) > 0:
            return -1
        
        start = 0
        ans = 0
        
        while(start < len(target)):
            tar_ind = start
            
            for src_char in source:
                if tar_ind < len(target) and src_char == target[tar_ind]:
                    tar_ind +=1
            
            start  = tar_ind
            ans += 1
        
        return ans
            
            
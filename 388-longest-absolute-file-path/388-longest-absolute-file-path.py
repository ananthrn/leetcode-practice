class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depLength = dict()
        
        i = 0
        
        maxLen = 0
        
        lines = input.split('\n')
        
        for line in lines:
            
            depth = line.count('\t')
            stripped = line.lstrip('\t')
            
            fileLen = len(stripped)
            isFile = stripped.count('.') >= 1
            
            depLength[depth] = depLength.get(depth - 1, 0) + 1 + fileLen
            print("line: ", line)
            print("depth: ", depth)
            print("stripped: ", stripped)
            print("fileLen: ", fileLen)
            print("depLength[depth]:", depLength[depth])
            print()
            if isFile:
                maxLen = max(maxLen, depLength[depth] - 1)
        
        return maxLen
            
                
                    
                
                    
        
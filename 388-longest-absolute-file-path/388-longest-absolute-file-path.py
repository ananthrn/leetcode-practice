class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depLength = dict()
        
        i = 0
        
        maxLen = 0
        
        while i < len(input):
            depth = 0
            isFile = False
            fileLen = 0
            while i < len(input) and input[i] != '\n':
                if input[i] == '\t':
                    depth += 1
                else:
                    fileLen += 1
                    if input[i] == '.':
                        isFile = True
                i+=1
            
            i+=1
            
            depLength[depth] = depLength.get(depth - 1, 0) + 1 + fileLen
            
            if isFile == True:
                maxLen = max(maxLen, depLength[depth] - 1)
        
        return maxLen
                
                    
                
                    
        
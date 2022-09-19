from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for path in paths:
            strings = path.split(' ')
            
            dirName = strings[0]
            
            for fileNameContent in strings[1:]:
                fileName, content = fileNameContent.split('(')
                
                groups[content[:-1]].append(dirName + '/' + fileName)
        
        return [val for val in groups.values() if len(val) > 1]
        
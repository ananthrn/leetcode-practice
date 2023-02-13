class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = list(map(lambda s: int(s), version1.split(".")))
        split2 = list(map(lambda s: int(s), version2.split(".")))
        
        maxLen = max(len(split1), len(split2))
        
        split1 = split1 + (maxLen - len(split1)) * [0]
        split2 = split2 + (maxLen - len(split2)) * [0]
        
        if split1 < split2:
            return -1
        elif split1 == split2:
            return 0
        else:
            return 1
class Solution:
    def differByOne(self, dic: List[str]) -> bool:
        MOD = 10 ** 11 + 7
        
        m, n = len(dic), len(dic[0])
        hashes = m * [0]
        
        for i, string in enumerate(dic):
            for char in string:
                hashes[i] = (26 * (hashes[i]) + (ord(char) - ord('a'))) % MOD
        
#         seen = set()
#         for i, string in enumerate(dic):
#             BASE = 1
#             for char in reversed(string):
#                 new_hash = (hashes[i] - ((ord(char) - ord('a')) * BASE)%MOD + MOD) % MOD
#                 if new_hash in seen:
#                     return True
#                 seen.add(new_hash)
                
#                 BASE = (BASE * 26) % MOD
                
                
        base = 1
        for j in range(n - 1, -1, -1):        
            seen = set()
            for i in range(m):
                new_h = (hashes[i] - base * (ord(dic[i][j]) - ord('a'))) % MOD
                if new_h in seen:
                    return True
                seen.add(new_h)
            base = 26 * base % MOD
        
        return False
                
        
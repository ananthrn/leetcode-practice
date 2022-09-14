class Solution:
    def differByOne(self, dic: List[str]) -> bool:
        MOD = 10 ** 11 + 7
        
        m, n = len(dic), len(dic[0])
        hashes = m * [0]
        
        for i, string in enumerate(dic):
            for char in string:
                hashes[i] = ((27 * hashes[i])%MOD + (ord(char) - ord('a'))) % MOD
        
        seen = set()
        for i, string in enumerate(dic):
            BASE = 1
            for char_ind in range(n - 1, -1, -1):
                char = string[char_ind]
                new_hash = (hashes[i] - ((ord(char) - ord('a') + 26) * BASE)  + MOD) % MOD
                if new_hash in seen:
                    print("i, string: ", i, string)
                    print("hashes[i]: ", hashes[i])
                    print("char_ind: ", char_ind)
                    print("char: ", char)
                    print("new_hash: ", new_hash)
                    print("BASE: ", BASE)
                    return True
                seen.add(new_hash)
                
                BASE = (BASE * 27) % MOD
        
        return False
                
        
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1_000_000_007
        charSet = set("aeiou")
        
        charAllowed = {
            'a': {'e'},
            'e': {'a', 'i'},
            'i': {'a', 'e', 'o', 'u'},
            'o': {'i', 'u'},
            'u': {'a'}
        }
        
        dp = [dict() for _ in range(n)]
        
        for char in charSet:
            dp[n-1][char] = 1
        
        for ind in reversed(range(n - 1)):
            for char in charSet:
                dp[ind][char] = 0 
                for nextChar in charAllowed[char]:
                    dp[ind][char] = (dp[ind][char]  + dp[ind + 1][nextChar]) % MOD 
        
        totalSum = 0
        for char in charSet:
            totalSum = (totalSum + dp[0][char])%MOD
        return totalSum
        
        
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)
        
        new_val = list(map(lambda b: str(1 - int(b)), bin_n[2:]))
                
        return int("".join(new_val), 2)
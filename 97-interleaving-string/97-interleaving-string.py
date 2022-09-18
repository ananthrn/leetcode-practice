class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def helper(s1_ind: int, s2_ind: int, s3_ind: int) -> bool:
            if s3_ind == len(s3):
                return s1_ind == len(s1) and s2_ind == len(s2)
            
            check_s1 = (
                (s1_ind < len(s1)) 
                and s1[s1_ind] == s3[s3_ind]
                and helper(s1_ind + 1, s2_ind, s3_ind + 1)
            )
            
            check_s2 = (
                (s2_ind < len(s2)) 
                and s2[s2_ind] == s3[s3_ind]
                and helper(s1_ind, s2_ind + 1, s3_ind + 1)
            )
            
            return check_s1 or check_s2
        
        return helper(0, 0, 0)
            
        
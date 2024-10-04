class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        
        neededSkill = skill[0] + skill[-1]
        
        left, right = 0, len(skill) - 1
        
        chemistry = 0
        while left < right:
            if skill[left] + skill[right] != neededSkill:
                return -1
            
            chemistry += skill[left] * skill[right]
            left +=1
            right -= 1
        return chemistry
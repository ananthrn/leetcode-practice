from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        recipeToIngredient = {
            recipe: ingredients for recipe, ingredients in zip(recipes, ingredients)
        }
        
        cache = {
            supply: True for supply in supplies
        }
        seen = defaultdict(int)
        def dfs(recipe: str) ->bool:
            if recipe in cache:
                return cache[recipe]
            
            seen[recipe] = 1
            
            for ingredient in recipeToIngredient[recipe]:
                if seen[ingredient] == 1:
                    cache[recipe] = False
                    return False
                    
                if ingredient not in recipes and ingredient not in supplies:
                    cache[recipe] = False
                    return False
                
                checkPos = dfs(ingredient)
                if not checkPos:
                    cache[recipe] = False
                    return False
            
            seen[recipe] = 2
            cache[recipe] = True
            return True
        
        recipesPossible = [recipe for recipe in recipes if dfs(recipe)]
        
        return recipesPossible
            
        
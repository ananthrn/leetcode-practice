class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        seen = len(candidates) * [False]
        solutions = set()
        cache = set()
        
#         def backtrack(target):
#             if tuple([target] + seen) in cache:
#                 return
#             print("target: ", target)
#             print("seen: ", seen)
#             print()
#             if target == 0:
                
#                 ans = tuple(sorted([candidates[ind] for ind in range(len(seen)) if seen[ind]]))
#                 # print("ans: ", ans)
#                 solutions.add(ans)
#                 cache.add(tuple([target] + seen))
                
#             for ind, candidate in enumerate(candidates):
#                 if not seen[ind] and candidate <= target:
#                     seen[ind] = True
#                     backtrack(target - candidate)
#                     seen[ind] = False
#             cache.add(tuple([target] + seen))
        
#         backtrack(target)
        
        cnt = 51 * [0]
        origCnt = 51 * [0]
        for candidate in candidates:
            cnt[candidate] += 1
            origCnt[candidate] += 1
            
        def backtrack(target):
            
            if tuple([target] + cnt) in cache:
                return
            print("target: ", target)
            if target == 0:
                # print("ans: ", ans)
                ans = []
                
                for candidate in range(51):
                    if origCnt[candidate] - cnt[candidate] > 0:
                        ans += (origCnt[candidate] - cnt[candidate]) * [candidate]
                
                solutions.add(tuple(sorted(ans)))
                cache.add(tuple([target] + cnt))
            
            for ind, candidate in enumerate(candidates):
                if cnt[candidate] > 0 and target >= candidate:
                    cnt[candidate] -= 1
                    backtrack(target - candidate)
                    cnt[candidate] += 1
            cache.add(tuple([target] + cnt))
        
        backtrack(target)
        return list(solutions)
        
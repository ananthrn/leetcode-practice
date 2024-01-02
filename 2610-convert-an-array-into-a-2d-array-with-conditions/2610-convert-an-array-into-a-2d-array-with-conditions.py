class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = collections.Counter(nums)
        
        ans = []
        while len(cnt.items())>0:
            ans.append([])
            newCnt = collections.Counter()
            print("cnt: ", dict(cnt))
            for key, val in cnt.items():
                print("key, val: ", key, val)
                ans[-1].append(key)
                if cnt[key] > 1:
                    newCnt[key] = val - 1 
                
                # ans[-1].append(key)
            
            print("newCnt: ", dict(newCnt))
            print()
            cnt = newCnt
        return ans
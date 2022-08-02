#include <bits/stdc++.h>
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if(nums.size() == 0)
        {
            return {};
        }
        
        vector<int> nums2(nums.begin(), nums.end());
        
        sort(nums2.begin(), nums2.end());
        
        vector<int> ans;
        vector<int> dp(nums2.size(), 0);
        vector<int> prevDiv(nums2.size(), -1);
        
        int mx_ind = 0;
        int mx_vl = 1;
        dp[0] =  1;
        prevDiv[0] = 0;
        
        for(int i=1; i<nums2.size(); i++){
            dp[i] =1;
            prevDiv[i] = i;
            for(int j=0; j<i;j++){
                if(nums2[i] % nums2[j] ==0){
                    if(dp[j] + 1 > dp[i]){
                        dp[i] = dp[j] + 1;
                        prevDiv[i] = j;
                    }
                }
            }
            
            if(dp[i] > mx_vl)
            {
                mx_vl = dp[i];
                mx_ind = i;
            }
        }
        
        int cur_ind = mx_ind;
        
        while(cur_ind>=0  and prevDiv[cur_ind]!=cur_ind){
            ans.push_back(nums2[cur_ind]);
            cur_ind = prevDiv[cur_ind];
        }
        
        ans.push_back(nums2[cur_ind]);
        
        return ans;
        
        
    }
};
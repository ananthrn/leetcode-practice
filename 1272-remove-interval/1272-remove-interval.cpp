class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals, vector<int>& toBeRemoved) {
        vector<vector<int>> ans;
        
        for(const auto& interval: intervals){
            if(toBeRemoved[1] <= interval[0] or interval[1] <= toBeRemoved[0]){
                // no overlap
                ans.push_back(interval);
            } else {
                // check if left part of the interval can make it
                
                if(interval[0] < toBeRemoved[0]){
                    ans.push_back({interval[0], toBeRemoved[0]});
                }
                
                //check if there is a right part to be added
                
                if(interval[1] > toBeRemoved[1]){
                    ans.push_back({toBeRemoved[1], interval[1]});
                }
            }
        }
        
        return ans;
    }
};
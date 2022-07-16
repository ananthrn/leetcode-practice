class SortedIntervals{
    vector<vector<int>> intervals;
public:
    SortedIntervals(){
        intervals.clear();
    }
    
    int getTotalSize(vector<vector<int>>& ints){
        int sz = 0;
        for(const auto& interval: ints){
            sz += interval[1] - interval[0];
        }
        
        return sz;
    }
    
    int insert(const vector<int> &newInterval){
        if(intervals.empty()){
            intervals.push_back(newInterval);
            return newInterval[1] - newInterval[0];
        }
        
        vector<vector<int>> ans;
        

        
        int j = 0;
        
        int minVal = newInterval[0];
        int maxVal = newInterval[1];
        
        while(j < intervals.size()){
            if (intervals[j][1] < minVal){
                ans.push_back(intervals[j]);
            }
            else if(intervals[j][0] <= maxVal){
                minVal = min(intervals[j][0], minVal);
                maxVal = max(intervals[j][1], maxVal);
            } else {
                ans.push_back({minVal, maxVal});
                minVal = intervals[j][0];
                maxVal = intervals[j][1];
            } 
            j++;
        }
        
        ans.push_back({minVal, maxVal});
        
        int szdiff = getTotalSize(ans) - getTotalSize(intervals);
        
        intervals = ans;
        
        return szdiff;
        
    }
};
class Solution {
public:
    vector<int> amountPainted(vector<vector<int>>& paint) {
        vector<int> ans(paint.size(), 0);
        SortedIntervals SI;
        
        for(int i = 0; i < paint.size(); i++){
            ans[i] = SI.insert(paint[i]);
        }
        
        return ans;
    }
};
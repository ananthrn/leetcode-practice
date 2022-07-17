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
        vector<vector<int>> records;
        // set<int> positions;
        
        for(int i = 0; i < paint.size(); i++){
            records.push_back({paint[i][0], i, 1});
            records.push_back({paint[i][1], i, -1});
            // positions.insert(paint[i][0]);
            // positions.insert(paint[i][1]);
        }
        
        sort(records.begin(), records.end());
        set<int> indices;
        
        int last_pos = records[0][0];
        
        int i = 0;
//         for(const auto &pos: positions){
            
//             int smallestIndex = *(indices.begin());
            
//             // if(last_pos > 0)
//             if(not indices.empty())
//                 ans[smallestIndex] += pos - last_pos;
            
//             // cout<<"pos: "<<pos<<endl;
//             // cout<<"indices.empty(): "<<indices.empty()<<endl;
//             // cout<<"last_pos: "<<last_pos<<endl;
//             // cout<<"smallestIndex: "<<smallestIndex<<endl;
//             // cout<<"ans[smallestIndex]: "<<ans[smallestIndex]<<endl;
//             // cout<<endl;
            
//             while(i < records.size() and records[i][0] == pos){
//                 if(records[i][1] == 1){
//                     indices.insert(records[i][2]);
//                 } else {
//                     indices.erase(records[i][2]);
//                 }
                
//                 i+=1;
//             }
            
//             // cout<<endl;
            
//             last_pos = pos;
//         }
        
        for(int j = 0; j<records.size(); j++)
        {
            int pos = records[j][0];
            int ind = records[j][1];
            int start = records[j][2];
            
            if(not indices.empty()){
                int smallestInd = *(indices.begin());
                ans[smallestInd] += pos - last_pos;
            }
            
            last_pos = pos;
            
            if(start == 1){
                indices.insert(ind);
            }else{
                indices.erase(ind);
            }
        }
        return ans;
    }
};
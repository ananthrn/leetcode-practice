class Solution {
public:
    int backTrack(int src, vector<int>& time, const vector<int>& manager, const vector<int>& informTime){
        if(time[src] >= 0){
            return time[src];
        }
        
        int manId = manager[src];
        
        int mantime = backTrack(manId, time, manager, informTime);
        
        time[src] = mantime + informTime[manId];
        
        return time[src];
        
    }
                  
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<int> time(n, -1);
        
        time[headID] = 0;
        
        int mxTime = 0;
        
        for(int src = 0; src < n; src++){
            if(time[src] < 0 ){
                time[src] = backTrack(src, time, manager, informTime);
            }
            mxTime = max(mxTime, time[src]);
        }
        
        return mxTime;
        
    }
};
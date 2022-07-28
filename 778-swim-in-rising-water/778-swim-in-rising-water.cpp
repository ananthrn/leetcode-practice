class Solution {
public:
    bool canSwim(const vector<vector<int>>& grid, int t){
        int n = grid.size();
        
        if(grid[0][0] > t)
        {
            return false;
        }
        
        if(n == 0)
            return true;
        
        
        vector<vector<bool>> seen(n, vector<bool> (n, false));
        set<vector<int>> seenPairs;
        queue<vector<int>> q;
        vector<vector<int>> dirs = {
            {0, 1},
            {0, -1},
            {-1, 0},
            {1, 0}
        };
        
        q.push({0, 0});
        seenPairs.insert({0, 0});
        
        vector<int> target = {n-1, n-1};
        cout<<endl;
        
        while(not q.empty()){
            auto tp = q.front();
            q.pop();
            if(tp == target)
                return true;
            
            if(seen[tp[0]][tp[1]])
                continue;
            seen[tp[0]][tp[1]] = true;
            
            cout<<"tp: "<<" "<<tp[0]<<" "<<tp[1]<<endl;
            
            for(auto d: dirs){
                int r = tp[0] + d[0];
                int c = tp[1] + d[1];
                
                if(0 <= r and r <n and 0 <= c and c < n){
                    if(grid[r][c] <= t and not seen[r][c]){
                        if(r == n-1 and c == n-1){
                            return true;
                        }
                        // seen[r][c] = true;
                        q.push({r, c});
                    }
                }
            }
        }
        
        return false;
    }
    int swimInWater(vector<vector<int>>& grid) {
        auto binSearch = [this, grid](int start, int end){
            int best = end + 1;
            while (start <= end){
                int mid = (start + end)/2;
                auto check = this->canSwim(grid, mid);
                
                if(check){
                    best = min(best, mid);
                    end = mid - 1;
                } else{
                    start = mid + 1;
                }
            }
            
            return best;
        };
        
        int n = grid.size();
        
        return binSearch(0, n * n );
    }
};
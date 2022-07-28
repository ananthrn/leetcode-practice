class Solution {
private:
    vector<vector<int>> dirs = {
        {0, 1},
        {1, 0},
        {-1, 0},
        {0, -1}
    };
    
    map<vector<int>, int> dp;
    
public:
    Solution(){
        dp = map<vector<int>, int>();
    }
    
    int bfs(const vector<vector<int>>& grid, int k){
        
        int m = grid.size(), n = grid.front().size();
        
        // map<vector<int>, int> dist;
        vector<vector<vector<int>>> dist(m , vector<vector<int>>(n, vector<int>(k+1, m*n+100)));
        queue<vector<int>> Q;
        
        Q.push({0, 0, 0, 0});
        
        int finalDist = m * n + 100;
        
        while(not Q.empty())
        {
            
            auto top = Q.front();
            Q.pop();
            
            int d = top[0];
            int used = top[1];
            
            int r = top[2];
            int c = top[3];
            
            if(dist[r][c][used] < m*n)
            {
                continue;
            } else {
                dist[r][c][used] = d;
            }
            
            if(r == m-1 and c == n-1){
                 finalDist = min(finalDist, d);  
                return finalDist;
               }
            for(auto dir: dirs){
                int new_r = r + dir[0];
                int new_c = c + dir[1];
                
                if(0 <= new_r and new_r < m and 0 <= new_c and new_c < n){
                    if(used + grid[new_r][new_c] <= k){
                        Q.push({
                            d + 1,
                            used + grid[new_r][new_c],
                            new_r,
                            new_c
                        });
                    }
                }
            }
        }
        
        if(finalDist < m*n + 100){
            return finalDist;
        } else {
            return -1;
        }
        
    }
               
    int shortestPath(vector<vector<int>>& grid, int k) {
        
//         dp = {};
//         int m = grid.size(), n = grid.front().size();
        
//         cout<<"m n k :"<<m<<" "<<n<<" "<<k<<endl;
//         vector<vector<bool>> seen(m, vector<bool>(n, false));
//         vector<vector<int>> dist(m, vector<int>(n, m*n +1));
        
//         int val =  dfs({0, 0}, grid, dist, seen, 0, k);
        
//         if(val > m*n){
//             return -1;
//         } else {
//             return val;
//         }
        
        return bfs(grid, k);
    }
};
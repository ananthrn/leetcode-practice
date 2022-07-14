class Solution {
public:
    int backtrack(int node, int seqNum, const vector<int>& scores, const vector<vector<int>>& adj, unordered_map<int, bool>& seen){ 
        // cout<<"SeqNum, Node: "<<seqNum <<" "<<node<<endl;
        if(seqNum == 0){
            return 0;
        }
        
        if(seqNum == 1){
            // cout<<endl<<endl;
            return scores[node];
        }
        
        seen[node] = true;
        // int sum = scores[node];
        
        int mxSum = 0;
        for(auto v: adj[node]){
            if(not seen[v]){
                // seen[v] = true;
                int sum = backtrack(v, seqNum - 1, scores, adj, seen);
                // seen[v] = false;
                
                mxSum = max(mxSum, sum);
            }
        }
        
        seen[node] = false;
        if(mxSum == 0){
            return -1;
        } else{
            return scores[node] + mxSum;
        }
    }
    
    int maximumScore(vector<int>& scores, vector<vector<int>>& edges) {
        vector<vector<int>> adj(scores.size());
        vector<set<pair<int,int>>> adjTop3(scores.size());
        
        for(auto edge: edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
            
            adjTop3[edge[0]].insert({scores[edge[1]], edge[1]});
            adjTop3[edge[1]].insert({scores[edge[0]], edge[0]});
            
            if(adjTop3[edge[0]].size() > 3){
                adjTop3[edge[0]].erase(adjTop3[edge[0]].begin());
            }
            
            if(adjTop3[edge[1]].size() > 3){
                 adjTop3[edge[1]].erase(adjTop3[edge[1]].begin());
            }
        }
        
//         int mxSum = -1;
//         unordered_map<int, bool> seen;
        
//         for(int node = 0; node < scores.size();  node ++){
//             int sum = backtrack(node, 4, scores, adj, seen);
//             mxSum = max(mxSum, sum);
//         }
        
        int mxSum = -1;
        
        for(auto edge: edges){
            for(const auto [score_0, adj_0]: adjTop3[edge[0]]){
                for(const auto [score_1, adj_1]: adjTop3[edge[1]]){

                    if(adj_0 != adj_1 and adj_0 != edge[1] and adj_1 != edge[0]){
                        int currentScore = score_0 + score_1 + scores[edge[0]] + scores[edge[1]];
                        
                        mxSum = max(mxSum, currentScore);
                        
                    }
                    // cout<<"edge: "<<edge[0]<<" "<<edge[1]<<endl;
                    // cout<<"adj_0, score_0: "<<adj_0<<" "<<score_0<<endl;
                    // cout<<"adj_1, score_1: "<<adj_1<<" "<<score_1<<endl;
                    // cout<<"mxSum: "<<mxSum<<endl;
                    // cout<<endl;
                }
            } 
        }
        
        return mxSum;
    }
};
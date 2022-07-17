class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        vector<int> serverLoad(k, 0);
        set<int> servers;
        
        for(int serverIndex = 0; serverIndex < k; serverIndex ++){
            servers.insert(serverIndex);
        }
        
        map<int, vector<int>> serversFreeing; // map from time to when new servers will be available
        
        for(int i = 0; i < arrival.size(); i++){
            // free up the servers that get free at this time
            
            
            // while(*(serversFreeing.begin()) <= arrival[i]){
            //     auto it
            // }
            // if(serversFreeing.count(arrival[i]))
            // {   
            //     for(const auto& newServer: serversFreeing.at(arrival[i])){
            //         servers.insert(newServer);
            //     }
            //     // erase this element to free memory
            //     serversFreeing.erase(arrival[i]);
            // }
            
            // pick the next server that is available (if empty the task is not assigned)
            
            while(not serversFreeing.empty() and (*serversFreeing.begin()).first <= arrival[i]){
                auto time = (*serversFreeing.begin()).first;
                auto serversFreed = (*serversFreeing.begin()).second;
                for(const auto& newServer: serversFreed){
                    servers.insert(newServer);
                }
                serversFreeing.erase(serversFreeing.begin());
            }
            
            if(not servers.empty()){
                auto serverAssigned = servers.lower_bound((i %k));
                if(serverAssigned == servers.end()){
                    // if there are none higher just go with the first element
                    serverAssigned = servers.begin();
                }
                
                auto serverIndex = *(serverAssigned);
                
                serverLoad[serverIndex] += 1;
                
                // cout<<"task: "<<i<<endl;
                // cout<<"serverIndex: "<<serverIndex<<endl;
                // cout<<endl;
                // remove server from servers and set it to free at a later time
                servers.erase(serverIndex);
                serversFreeing[arrival[i] + load[i]].push_back(serverIndex);
            }
        }
        
        vector<int> ans;
        
        int mxLoad = 0;
        
        for(auto load: serverLoad){
            mxLoad = max(mxLoad, load);
        }
        
        for(int server = 0; server < serverLoad.size(); server++){
            if(serverLoad[server] == mxLoad){
                ans.push_back(server);
            }
        }
        return ans;
    }
};
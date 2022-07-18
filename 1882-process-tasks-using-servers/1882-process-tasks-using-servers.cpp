class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        queue<int> taskQ;
        set<pair<int, int>> servFree;
        map<int, vector<int>> timeServers;
        
        for(int serv = 0; serv < servers.size(); serv++){
            servFree.insert({servers[serv], serv});
        }
        
        int currentTime = 0;
        
        vector<int> ans(tasks.size(), -1);
        
        while(true){
            if(currentTime < tasks.size()){
                taskQ.push(currentTime);
            }
            
            if(taskQ.empty()){
                break;
            }
            
            // free the servers remaining at this time;
            
            if(timeServers.count(currentTime)){
                for(const auto serverIndex: timeServers.at(currentTime)){
                    servFree.insert({servers[serverIndex], serverIndex});
                }
                timeServers.erase(currentTime);
            }
            
            // if  free servers 
            
            if(not servFree.empty()){
            // assign free server to first task;
                while(not servFree.empty() and not taskQ.empty()){
                    int taskId = taskQ.front();
                    taskQ.pop();



                    const auto [serverWeight, serverId] = *(servFree.begin());
                    servFree.erase(servFree.begin());



                    ans[taskId] = serverId;

                    int taskTime = tasks[taskId];
                    timeServers[currentTime + taskTime].push_back(serverId);

                    // cout<<"currentTime: "<<currentTime<<endl;
                    // cout<<"taskId, serverId, serverWeight: "<<taskId<<" "<<serverId<<" "<<serverWeight<<endl;
                    // cout<<"server will be free at: "<<currentTime + taskTime<<endl;
                    // // cout<<"nextTime: "<<(currentTime < tasks.size() or timeServers.empty())?currentTime + 1: timeServers.begin()->first<<endl;
                    // cout<<endl;
                }
                
                // cout<<"server Release time: "<<
            }
            int nextTime = -1;
            if(currentTime < tasks.size()){
                nextTime = currentTime + 1;
            } else {
                if(not timeServers.empty()){
                   nextTime = timeServers.begin()->first;
                } else {
                    nextTime = currentTime + 1;
                }
            }
            // cout<<"nextTime: "<<nextTime<<endl;
            // cout<<endl;
            
            currentTime = nextTime;
        }
        
        return ans;
    }
};
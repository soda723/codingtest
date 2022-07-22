#include <cstring>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<string> lines) {    
    
    int answer = 0;
    
    vector<vector<long long>> infoList;
    
    for(int i =0;i<lines.size();i++){
        
        int h = stoi(lines[i].substr(11,2))*3600000;
        int m = stoi(lines[i].substr(14,2))*60000;
        int s = stod(lines[i].substr(17,6))*1000;
        int timeSpend = stod(lines[i].substr(24, lines[i].size()-1))*1000;
        
        int timeTotal = h+m+s;

        infoList.push_back({timeTotal-timeSpend+1, timeTotal});
    }
        
    for(int i =0;i<lines.size();i++){
        int end = infoList[i][1]+1000;
        int count = 0;
        for(int j = i; j<lines.size();j++){
            if(infoList[j][0]<end) count++;
        }
        if(answer <count) answer = count;
    }
    return answer;
}
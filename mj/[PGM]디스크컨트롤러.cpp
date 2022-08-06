#include <vector>
#include <queue>
#include <algorithm>
 
using namespace std;
 
struct shorter {    // 우선순위 큐의 우선순위 구조체
    bool operator()(vector<int> a, vector<int> b) {
        return a[1] > b[1];
    }
};
 
int solution(vector<vector<int>> jobs) {
    int answer = 0;
        
    //먼저 요청이 들어온 순으로 jobs 정렬 후, 작업의 우선순위를 나타낼 우선순위 큐 선언
    sort(jobs.begin(), jobs.end());
    priority_queue<vector<int>, vector<vector<int>>, shorter> prior_q;
    
    int i = 0, t = 0;
    
    // 우선순위 큐가 빌 때까지 반복
    while (i < jobs.size() || !prior_q.empty()) {
        
        // 아직 해야할 작업이 남아있고 현재의 작업보다 처리시간이 적다면
        if (jobs.size() > i){
            if(t >= jobs[i][0]) {
                //우선순위 큐에 추가
                prior_q.push(jobs[i]);
                i++;
                continue;
            }
        }
        
        // 작업 중 다른 작업이 들어왔을 경우 상정
        if (!prior_q.empty()) {
            //해당 작업의 소요시간만큼 시간 추가
            t += prior_q.top()[1];
            //작업시간에 대기 시간만큼 추가(현재시간 - 들어온 시간)
            answer += t - prior_q.top()[0];
            //작업이 끝났으므로 우선순위 큐에서 제거한다.
            prior_q.pop();
        }
        
        else //큐가 비어있다면 다음작업이 올때까지 대기
            t = jobs[i][0];
    }
    
    // 평균을 구한다.
    answer /= jobs.size();
    
    return answer; 
}
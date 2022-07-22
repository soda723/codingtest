#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 입국심사를 기다리는 사람 n명, 각 심사관이 한명 심사하는데 걸리는 시간 times
long long solution(int n, vector<int> times) {
    // 모든 심사대 비어있고
    // 1심사대 당 1명
    // 가장 앞에 서 있는 사람 비어 있는 심사대로 갈 수 있음
    long long answer = 0;    
    
    // times 배열을 오름차순 정렬
    sort(times.begin(), times.end());
 
    // 입국심사의 대기시간은 1~1000의 범위이다. => 이분탐색
    long long start = 1, end = (long long)times.back() * n, mid;
    
    while(start <= end){    /// start가 end보다 클때까지 반복
        
        mid = (start+end)/2;    // mid 구하고
        
        // mid 시간동안 심사할 수 있는 사람 수 p
        long long p = 0;
        
        //심사대 개수만큼 병렬처리할 수 있으니 (총 예상시간/한 심사대의 대기시간)의 총계를 구한다.
        for(int i =0; i<times.size();i++){
            p += mid/times[i];
        }//즉, mid 시간동안 심사할 수 있는 사람 수p가 만들어짐
        
        if(p >= n){ // p가 n보다 크거나 같으면 문제 요구사항에 부합!
            end = mid-1;  // 범위의 끝을 줄인다
            answer = mid;
        }
        else{ // p가 n보다 작으면, 
            start = mid+1;// 범위의 시작을 높인다.
        }
    }
    return answer;
}
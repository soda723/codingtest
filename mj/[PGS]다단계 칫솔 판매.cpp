#include <string>
#include <vector>
#include <unordered_map>

using namespace std;
unordered_map<string, string> refer_info;   // key: enroll ,value:referral
unordered_map<string, int> money_info;      // key: seller ,value:amount

// 수익분배 계산 함수. 재귀로 구현
void moneyget(string person,int money){    
    if(person.compare("-")==0) return;  // 추천인이 없으면 return
    int togive = money * 0.1;       // 추천인에게 줘야하는 수익의 10% 금액
    money_info[person] += (money - togive); // 추천인에게 줄 것 제외하고 현재 판매원의 몫
    if(togive<1) return;    // 추천인에게 안 줘도 되면 return 
    moneyget(refer_info[person], togive);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;

    // 두 uo_m 준비
    for(int i = 0 ; i<enroll.size();i++){
        refer_info.insert(pair<string, string>(enroll[i],referral[i]));
        money_info.insert(pair<string, int>(enroll[i],0));
    }
    
    // 판매실적을 낸 판매원들을 기준으로 수익분배 계산
    for(int i =0; i<seller.size();i++){
        int salesMoney = amount[i] * 100;        // 칫솔개수 *100원
        moneyget(seller[i] ,salesMoney); 
    }
    
    for(int i = 0; i< enroll.size();i++)
        answer.push_back(money_info[enroll[i]]);
    
    return answer;
}
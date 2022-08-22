#소요시간 : 1h 30m
from itertools import combinations_with_replacement

def solution(n, info):
    answer=[]
    nlen = len(info)
    #라이언이 쏠 수 있는 모든 경우의 수 
    canlist = list(combinations_with_replacement(range(nlen),n))
    max_d = -1
    info = info[::-1] # 계산 편의성을 위해 순서 뒤집음
    
    for can in canlist : 
        now = [0]*nlen
        for arrow in can:
            now[arrow] += 1

        apeach = 0
        lion = 0
        for i in range(nlen):
            if info[i] < now[i]:
                lion += i 
            elif info[i] != 0: # 둘다 0점일때 계산하면 안됌
                apeach += i

        if lion > apeach :
            tmp = lion - apeach
            if max_d < tmp :
                max_d = tmp
                answer = now
            elif max_d == tmp: # 점수차가 같으면 아래점수가 많은거
                for i in range(nlen):
                    if answer[i] < now[i]:
                        answer = now
                        break
                    elif answer[i] > now[i]: #이전답이 커도 멈춰야함
                        break

    if max_d == -1:
        return [-1]

    return answer[::-1]

#print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))

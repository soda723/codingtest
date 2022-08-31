# BOJ 1946 신입사원 silver1
# 소요시간 : 1h 34m
# 첫 번째값을 더하는 걸 빼먹어서 오래 걸렸다 ㅠㅠㅠ
# ==, = 실수 언제 까지 할겨

import sys
input = sys.stdin.readline

def solution(N, itv):
    answer = 1 # 첫번째 값 포함
    mm = itv[0] 
    for idx in range(1,N): # 첫번재 값은 할필요 없음
        s = itv[idx] 
        ## answer = N으로 시작했을때
        # if s == 1 : mm = s
        # elif s == N : answer -= 1 
        # elif s > mm : answer -= 1 
        # else : mm = s 
        if s < mm : 
            answer += 1
            mm = s

    return answer

T = int(input()) # 테스트 케이스의 수
for _ in range(T):
    N = int(input()) # 지원자의 수
    score=[]
    for _ in range(N):
        score.append(list(map(int, input().split())))
    score.sort()
    itv=[]
    for sc in score:
        itv.append(sc[1])

    print(solution(N, itv))
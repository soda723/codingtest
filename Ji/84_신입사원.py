# BOJ 1946 신입사원 silver1
# 소요시간 : 28m > 시간초과

def solution(N, score):
    answer = N
    fail = set()
    for idx in range(1,N+1):
        doc = score[idx][0]
        itv = score[idx][1]
        if doc == 1 or itv == 1: continue
        elif doc == N or itv == N : 
            fail.add(idx)
            continue
        
        for i in range(1,N+1):
            if i == idx:
                continue
            if score[i][0] < doc and score[i][1] < itv:
                fail.add(idx)

    return answer - len(fail)

T = int(input()) # 테스트 케이스의 수
for _ in range(T):
    N = int(input()) # 지원자의 수
    score = {}
    for idx in range(1,N+1):
        score[idx] = list(map(int, input().split()))
    print(solution(N, score))

# BOJ 11399 ATM
# 소요시간 : 15m

def solution(N, times):
    answer = 0
    times.sort()
    for i, t in enumerate(times):
        answer += (t * (N-i))
    return answer

N = int(input())
times = list(map(int, input().split()))
print(solution(N,times))

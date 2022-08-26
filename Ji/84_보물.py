# BOJ 1026 보물
# 소요시간 : 8m28s
# 역정렬 B.sort(reverse = True)

def solution(N, A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(N):
        answer += A[i]*B[N-i-1]

    return answer

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(N, A, B))
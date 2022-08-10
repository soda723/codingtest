#백준 2839 설탕배달 : 다이나믹프로그래밍
#소요시간 50m
def solution(N):
    answer = N//3 +1
    if N % 5 == 0 : answer = N//5
    elif N % 3 == 0 :answer = N//3
    i = N // 5 
    while(i >=0):
        #print(i)
        num = N - 5*i
        if (num % 3 != 0) : pass
        else : 
            tmp = i + num//3
            if tmp < answer : answer = tmp
        i -= 1


    if answer == N//3 +1 : return -1
    return answer

N = int(input())
print(solution(N))
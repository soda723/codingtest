#힌트 1h 54m
def solution(n, times):
    times.sort()
    maxtime = n*times[-1] # 최대시간 넉넉하게 n명*제일느린심사관
    lefttime = times[0] # 1명이 가장빠른 심사관에게 심사 받고 끝날때
    mid = 0
    while(lefttime <= maxtime):
        mid = (maxtime + lefttime) // 2
        people = 0
        #중간시간동안 각 심사관이 몇 명을 검사할 수 있는지 확인
        for t in times:
            people += mid//t
        if people >= n : 
            #시간이 넘처요 시간을 줄이자
            #완전 일치하지 않아도 부족하지 않으면 최솟값이 될 수 있음
            answer = mid
            maxtime = mid-1
        else:
            #시간이 모자라요 시간을 늘리자
            lefttime = mid +1
            
    return answer
# 소요시간 1h 49m
# 힌트 0 
# 이전에 완료한 시간이 필요하다 jobs =/= ablejob
import heapq
def solution(jobs):
    divide = len(jobs)
    wating = 0  # 대기시간 합 answer = wating/divide
    # jobs.sort(key = lambda x: (x[0] , x[1])) ## 힙 쓸거니까 필요가 없음

    now = 0
    ablejob = []
    cnt = 0
    start = -1
    while cnt < divide :
        # 현재 가능한 job리스트 만들기
        for job in jobs:
            if job[0] <= now  and job[0] > start:
                heapq.heappush(ablejob, [job[1],job[0]]) # 우선순위가 소요시간이 되도록

        #현재 가능한게 있을때
        if len(ablejob) > 0:
            best = heapq.heappop(ablejob)
            # 0,1 자리 바꿨으니까 헷갈리면 안됌
            wating += (best[0] + now - best[1]) # 소요시간 + 지금시간 - 들어온시간
            start = now # 이전에 완료한 시간
            now += best[0] # 지금시간 + 소요시간 = 다음 시작시간
            cnt += 1
        else :
            #없을때 시간 늘리기
            now += 1

    return int(wating / divide)

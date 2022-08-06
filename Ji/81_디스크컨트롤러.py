# 소요시간 : 1h1m~
# 마지막 TC빼고 다 틀림큐ㅠ 
def solution(jobs):
    divide = len(jobs)
    answer = 0
    jobs.sort(key = lambda x: (x[0] , x[1]))
    # 첫번째 값 미리 넣기
    startidx = jobs[0]
    nextt = jobs[0][1]
    answer += jobs[0][1] - jobs[0][0]
    jobs.pop(0)

    time = 0 # 우선 순위 결정할 변수
    maxidx = 0 # 우선순위 높은 idx 저장할 변수
    while(jobs):
        for i in range(len(jobs)):
            if jobs[i][0] <= nextt:
                if time != 0:
                    if time > jobs[i][1]:
                        time = jobs[i][1]
                        maxidx = i
                else:
                    time = jobs[i][1]
                    maxidx = i

        answer += (jobs[maxidx][1] + nextt - jobs[maxidx][0])
        nextt = answer
        jobs.pop(maxidx)
        time = 0
        maxidx = 0
        
    return int(answer/divide)
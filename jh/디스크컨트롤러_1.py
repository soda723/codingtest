def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    current, answer = 0, 0
    queue = [jobs[i] for i in range(len(jobs))]
    
    while len(queue) != 0:
        if queue[0][0] > current: # 지금 정렬이 되어 있음 -> [0][0]의 원소가 current보다 크면 무조건 첫번째가 답
            answer += queue[0][1]
            current = queue[0][0] + queue[0][1]
            del queue[0]
        else: # 위의 경우가 아니라면 실행시간이 가장 짧은 것이 답
            min = queue[0][1]
            m_index = 0
            cost = current - queue[0][0] + queue[0][1]
            for i in range(1, len(queue)):
                if queue[i][0] > current: # 최소값을 찾는 과정에서 요청 시간이 current보다 크면 무조건 안 됨
                    break
                if queue[i][1] < min:
                    min = queue[i][1]
                    m_index = i
                    cost = current - queue[i][0] + queue[i][1]
            answer += cost
            current += queue[m_index][1]
            del queue[m_index]
            
    return answer // len(jobs)
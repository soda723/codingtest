import heapq

def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    n = len(jobs)
    current, answer = 0, 0
    heap = []
    
    while len(heap) != 0 or len(jobs) != 0:
        if len(heap) == 0: # jobs는 있는데 heap이 비어 있다면 jobs 배열 중 가장 빨리 요청되는 것을 heap에 추가해야 함 -> 정렬된 상태기 때문에 무조건 첫 번째 원소가 답
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]])
            del jobs[0]
            
        while len(jobs) != 0 and jobs[0][0] <= current: # current보다 일찍 요청된 일들을 heap에 추가
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]]) # heap에 있는 값 중 실행 시간이 가장 짧은 것을 빼와야 하기 때문에 배열 순서 뒤집어서 heap에 추가
            del jobs[0]
        
        request = heapq.heappop(heap)
        current = max(current + request[0], request[1] + request[0]) # 이전 current를 기준으로 job이 언제 요청되었는지에 따라 실행된 후의 current가 달라지기 때문에 max 함수 사용
        answer += current - request[1]

    return answer // n
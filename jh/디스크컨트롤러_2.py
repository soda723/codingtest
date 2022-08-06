import heapq

def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    n = len(jobs)
    current, answer = 0, 0
    heap = []
    
    while len(heap) != 0 or len(jobs) != 0:
        if len(heap) == 0:
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]])
            del jobs[0]
            
        while len(jobs) != 0 and jobs[0][0] <= current:
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]])
            del jobs[0]
        
        request = heapq.heappop(heap)
        current = max(current + request[0], request[1] + request[0])
        answer += current - request[1]

    return answer // n
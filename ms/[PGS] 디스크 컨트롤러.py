import heapq

def solution(jobs):
    jobs.sort()
    minHeap = []
    start = -1   
    now = answer = finish = 0   # now는 현재 시간, answer은 걸린 시간, finish는 처리한 작업의 개수

    # 모든 작업을 다 처리할 때까지 반복
    while finish < len(jobs):
        for i in range(len(jobs)):
            if start < jobs[i][0] <= now:   # start를 설정해주지 않으면 리스트의 첫부분부터 다시 힙에 넣게 됨
                heapq.heappush(minHeap, [jobs[i][1], jobs[i][0]])   # 이차원 리스트를 힙에 넣는 코드는 찾아봄

        # 힙이 비어있지 않으면 처리 시간이 짧은 작업부터 처리함
        if len(minHeap) > 0:
            work = heapq.heappop(minHeap)
            answer += work[0] + (now - work[1])
            start = now   # 처음에 start=work[1]로 풀었는데 틀림.. 이유 잘 모르겠음
            now += work[0]
            finish += 1
        else:   # 힙이 비어있으면 현재 시간을 증가시켜줌
            now += 1

    return answer // finish

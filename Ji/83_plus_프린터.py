# 소요시간 17m
# 다양한 풀이 읽어보기 any

from collections import deque

def solution(priorities, location):
    answer = 0
    data = [[i,p] for i, p in enumerate(priorities)]
    q = deque(data)
    order = []
    while q : 
        now = q.popleft()
        if now[1] == max(priorities):
            order.append(now[0])
            priorities.remove(max(priorities)) # 앞에서 부터 하나만 삭제
        else:
            q.append(now) # 다시 뒤에 넣기
        
    return order.index(location) + 1
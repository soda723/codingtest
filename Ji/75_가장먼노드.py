  #1h 24m / 힌트0
from collections import deque
def solution(n, edge):
  
    # # 방향이 2개
    # vertex = edge
    # for es in edge:
    #     vertex.append([es[1],es[0]])

    edge.sort() #[[1, 2], [1, 3], [2, 4], [3, 2], [3, 6], [4, 3], [5, 2]]
    #1로 부터 아무것도 연결되지 않았을 때
    if edge[0][0] != 1:
        return n-1

    n_vertex = [[] for _ in range (n+1)]
    for s, e in edge:
        n_vertex[s].append(e)
        n_vertex[e].append(s)

    visit = [0]*(n+1) #방문정보 담을 곳, 인덱스 통일하기 위해 n + 1
    visit[1] = 1 #1에서 시작하는거 방문표시 안했더니 TC1틀림 ㅎㅎ
    q = deque()
    q.append(1) #시작노드1 넣어두기
    while q:
        now = q.popleft()
        for v in n_vertex[now]: # 현재 노드와 연결되어 있는 노드 리스트
            if visit[v] == 0: # 방문여부 확인
                visit[v] = visit[now] + 1 # 지금까지 방문한 곳 거리 +1
                q.append(v) #방문했으니까 q 에 넣는다.
    maxlength = max(visit)
    answer = visit.count(maxlength)

    return answer
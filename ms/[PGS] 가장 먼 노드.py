def solution(n, edge):
    adj = {}   # 시간 줄이기 위해 딕셔너리 이용
    for i in range(1, n+1):
        adj[i] = []

    # 각 노드별로 연결된 노드들을 리스트로 저장함
    for v in edge:
        adj[v[0]].append(v[1])
        adj[v[1]].append(v[0])

    discovered = [False for _ in range(n+1)]   # 노드별 탐색 여부

    # BFS 이용함!!
    q = []
    q.append(1)
    discovered[1] = True
    distance = [0 for _ in range(n+1)]

    while len(q) != 0:
        here = q.pop(0)
        for i in adj[here]:  # here에 연결된 노드들만 반복문 돌림(시간 줄어듦)
            if not discovered[i]:
                q.append(i)
                discovered[i] = True
                distance[i] = distance[here] + 1   # 그래프 거리 구하기

    # 예제의 경우 distance = [0, 0, 1, 1, 2, 2, 2]
    answer = distance.count(max(distance))

    return answer

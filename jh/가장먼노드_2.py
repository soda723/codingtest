def solution(n, edge):
    answer = {i: 0 for i in range(1, n)} # {depth: depth로 연결된 노드 개수}의 딕셔너리
    dict = {i: set() for i in range(1, n+1)}
    
    for e in edge: # 서로 연결된 노드들 양방향으로 추가
        dict[e[0]].add(e[1])
        dict[e[1]].add(e[0])

    # set으로 한 이유: set은 유니크한 값을 가지기 때문에 중복을 처리하는 데 용이하다고 생각함
    queue = set(dict[1]) # 1번 노드로부터 연결 가능한 노드를 가지는 집합
    closed = {1} # 이미 방문한 노드를 가지는 집합
    depth = 1
    
    while len(queue) != 0:
        for v in queue:
            answer[depth] += 1 # key == depth인 딕셔너리의 value를 1 증가
            closed.add(v) # 방문한 노드를 closed에 추가

        # 현재 queue에 있는 노드들 방문이 다 끝나면    
        depth += 1 # depth를 증가시키고
        li = list(queue)
        
        while len(li) != 0: # queue에 있는 노드에서 연결된 노드들을 queue에 추가시킴
            v = li.pop()
            queue.update(dict[v])
        
        queue = queue - closed # 추가된 노드에서 이미 방문한 노드를 걸러냄
        
    for i in range(n-1, 0, -1):
        if answer[i] != 0:
            return answer[i]
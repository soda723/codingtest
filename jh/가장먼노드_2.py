def solution(n, edge):
    answer = {i: 0 for i in range(1, n)}
    dict = {i: set() for i in range(1, n+1)}
    
    for e in edge:
        dict[e[0]].add(e[1])
        dict[e[1]].add(e[0])
        
    queue = set(dict[1])
    closed = {1}
    depth = 1
    
    while len(queue) != 0:        
        for v in queue:
            answer[depth] += 1
            closed.add(v)
            
        depth += 1
        li = list(queue)
        
        while len(li) != 0:
            v = li.pop()
            queue.update(dict[v])
        
        queue = queue - closed
        
    for i in range(n-1, 0, -1):
        if answer[i] != 0:
            return answer[i]
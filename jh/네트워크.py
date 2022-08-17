def solution(n, computers):
    answer = 0
    visited = [False] * n
    queue = []
    
    for i in range(n):
        for j in range(n):
            if not visited[j] and computers[i][j] == 1:
                queue.append(j)
        visited[i] = True
        
        while len(queue) != 0:
            q = queue.pop()
            visited[q] = True
            for j in range(n):
                if not visited[j] and computers[q][j] == 1:
                    queue.append(j)
            if len(queue) == 0:
                answer += 1

    return answer
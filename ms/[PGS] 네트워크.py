# 3단계 수준은 아닌듯..
def dfs(v, n, computers):
    visited[v] = True

    for i in range(n):
        if (not visited[i]) and computers[v][i] == 1:
            dfs(i, n, computers)
            
    
def solution(n, computers):
    global visited
    visited = [False for _ in range(n)]   # 각 노드의 방문 여부

    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += 1   # 컴포넌트 세기(정답)
            dfs(i, n, computers)
            
    return answer

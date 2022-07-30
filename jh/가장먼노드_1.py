# 테스트 7, 8, 9 시간 초과

def solution(n, edge):
    answer = {i: 0 for i in range(1, n)}
    dict = {i: set() for i in range(1, n+1)}
    
    for e in edge:
        dict[e[0]].add(e[1])
        dict[e[1]].add(e[0])
        
    for i in range(2, n+1):
        queue = set()
        queue.update(dict[i])
        closed = set()
        depth = 1
        flag = False
        
        while len(queue) != 0:
            if 1 in queue: # O(1)
                flag = True
                break
            else:
                depth += 1
                closed.update(queue)
                li = list(queue) # O(len(queue))
                queue.clear() # O(1)
                
                while len(li) != 0: # for문 안에서 set 사이즈 변경 불가능
                    v = li.pop()
                    queue.update(dict[v])
                    
                queue = queue - closed # 이미 방문한 노드를 제외하기 위해서
            
        if flag == True:
            answer[depth] += 1

    for i in range(n-1, 0, -1):
        if answer[i] != 0:
            return answer[i]
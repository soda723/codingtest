def solution(n, k, cmd):
    answer = ['O'] * n
    now = k # 굳이 선언 안 해도 되지만 가독성 높이려고 선언
    linked = {i: [i-1, i+1] for i in range(n)} # i: [prev, next]
    linked[0][0], linked[n-1][1] = '-', '-'
    queue = []
    
    for c in cmd:
        if c[0] == 'C':
            queue.append(now)
            prev = linked[now][0]
            next = linked[now][1]
            
            if prev != '-':
                linked[prev][1] = next
            if next != '-':
                linked[next][0] = prev
            
            if linked[now][1] == '-':
                answer[now] = 'X'
                now = linked[now][0]
            else:
                answer[now] = 'X'
                now = linked[now][1]
        
        elif c[0] == 'U':
            count = int(c[2:])
            while count != 0:
                now = linked[now][0]
                count -= 1
        
        elif c[0] == 'D':
            count = int(c[2:])
            while count != 0:
                now = linked[now][1]
                count -= 1
                
        elif c[0] == 'Z':
            q = queue.pop()
            answer[q] = 'O'
            prev = linked[q][0]
            next = linked[q][1]
            
            if prev != '-':
                linked[prev][1] = q
            if next != '-':
                linked[next][0] = q
            
    return ''.join(answer)
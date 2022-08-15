def solution(n, k, cmd):
    now = k
    leng = n
    linked = {i: 'O' for i in range(n)}
    queue = []
    
    for c in cmd:
        if c[0] == 'C':
            queue.append(now)
            linked[now] = 'X'
            leng -= 1
            if leng < now:
                now -= 1
                while now > 0 and linked[now] == 'X':
                    now -= 1
            else:
                now += 1
                while now < n and linked[now] == 'X':
                    now += 1
        
        elif c[0] == 'U':
            count = int(c[2:])
            while now > 0 and count != 0:
                if linked[now-1] != 'X':
                    count -= 1
                now -= 1
        
        elif c[0] == 'D':
            count = int(c[2:])
            while now < n and count != 0:
                if linked[now+1] != 'X':
                    count -= 1
                now += 1
                
        elif c[0] == 'Z':
            q = queue.pop()
            linked[q] = 'O'
            leng += 1
    
    return ''.join(list(linked.values()))
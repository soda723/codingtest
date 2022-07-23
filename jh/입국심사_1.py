def solution(n, times):
    answer = 0
    
    current = [[t, 0] for t in times]
    current[0][1] = current[0][0]
    n -= 1
    
    while n > 0:
        current.sort(key=lambda x: (x[1], x[0]))
        
        while current[0][1] == 0:
            for i in range(1, len(current)):
                if current[i][0] + current[i][1] < current[0][0]:
                    current[0][1] = current[i][0] + current[i][1]
                    break
                    
            if current[0][1] == 0:
                current[0][1] = current[0][0]
                
            current.sort(key=lambda x: (x[1], x[0]))
            n -= 1

        t = current[0][1]
        for i in range(len(current)):
            current[i][1] -= t
        answer += t
        
    current.sort(key=lambda x: x[1])
    answer += current[-1][1]
    
    return answer
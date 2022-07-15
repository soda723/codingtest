def solution(N, number):
    if N == number:
        return 1
    
    li = []
    for _ in range(9):
        li.append([])    
    li[1] = [N]
    
    for i in range(2, 9):
        s = set()
        s.add(int(str(N) * i))
        for j in range(1, int(i/2)+1):
            for a in li[j]:
                for b in li[i-j]:
                    s.add(a + b)
                    s.add(a - b)
                    s.add(b - a)
                    s.add(a * b)
                    if b != 0:
                        s.add(a / b)
                    if a != 0:
                        s.add(b / a)
        if number in s:
            return i
        s = list(s)
        li[i] = s
        
    return -1
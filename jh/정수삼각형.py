def solution(triangle):
    f = []
    f.append(triangle[0])
    
    for i in range(1, len(triangle)):
        sum = []
        for j in range(len(triangle[i])):
            if j == 0:
                sum.append(f[i-1][0] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                sum.append(f[i-1][j-1] + triangle[i][j])
            else:
                n = max(f[i-1][j-1], f[i-1][j])
                sum.append(n + triangle[i][j])
        f.append(sum)
    
    return max(f[-1])
import sys
sys.setrecursionlimit(10000)   # 런타임 에러 방지

t = int(input())

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    for j in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    result = 0
    for x in range(n):
        for y in range(m):
            if dfs(x, y):
                result += 1

    print(result)
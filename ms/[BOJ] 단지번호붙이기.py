n = int(input())
house = []
for i in range(n):
    house.append(list(map(int, input().strip())))   # *
    

def dfs(x, y):
    global num
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if house[x][y] == 1:
        num += 1
        house[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
number = []
num = 0
for x in range(n):
    for y in range(n):
        if dfs(x, y):
            result += 1
            number.append(num)
            num = 0

print(result)
number.sort()
for i in number:
    print(i)
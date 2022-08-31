n, m = map(int, input().split())
li = list(map(int, input().split()))
max = 0
for i in range(len(li)):
    for j in range(len(li)):
        if i == j: continue
        for k in range(len(li)):
            if i == k or j == k: continue
            sum = li[i] + li[j] + li[k]
            if sum > max and sum <= m:
                max = sum
print(max)
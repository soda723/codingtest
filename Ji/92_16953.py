# BOJ A->B 16953번 silver2
# 소요시간 : 33m
A, B = map(int, input().split())
answer = -1
q = [[B, 1]]
while(q):
    cur = q.pop()
    if cur[0] == A : 
        answer = cur[1]
        break
    if cur[0]%2==0 and cur[0] // 2  >= A : 
        q.append([cur[0] // 2, cur[1] +1])
    if cur[0]%10 == 1 and (cur[0]-1)//10 >= A : 
        q.append([(cur[0]-1)//10, cur[1] +1])

print(answer)
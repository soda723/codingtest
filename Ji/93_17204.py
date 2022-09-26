# BOJ 죽음의 게임 17204번 silver3
# 소요시간 : 17m 54s

N, bs = map(int, input().split())
visited = [0]*N
noanswer = 0
death = {n:0 for n in range(N)}
for i in range(N):
    death[i] = int(input())
#print(death)

visited[0] = 1
end = death[0]
answer = 1

while end != bs:
    if visited[end] == 1: 
        noanswer = 1
        break
    else : 
        visited[end] = 1
        answer += 1
        end = death[end]

if noanswer : print(-1)
else : print(answer)  

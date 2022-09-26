 # BOJ 바이러스 2606번 silver3
 # 소요시간 : 27m 42s

n = int(input())
ring = int(input())
nodes = [0]*(n+1)
ok = [0]*(n+1)

#그래프 만들기(?)
for _ in range(ring):
    f, b = map(int, input().split())
    if nodes[f] == 0: nodes[f] = [b]
    else : nodes[f].append(b)

    if nodes[b] == 0: nodes[b] = [f]
    else : nodes[b].append(f)
#print(nodes)      
#계산하기
ok[1] = 1
answer = 0
q = nodes[1]
while q:
    now = q.pop()
    if ok[now] : pass
    else:
        ok[now] = 1
        answer += 1
        if nodes[now] != 0:
            for v in nodes[now]:
                if ok[v] == 0:
                    q.append(v)

print(answer)
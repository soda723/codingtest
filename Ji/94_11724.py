# 백준 연결요소의 개수 11724번 silver2
# 소요시간 : 58m
# 문제 잘못이해, 시간초과, NameError 등... 으로 오래걸림
# BFS로 풀어보기 (sys.setrecursionlimit()사용안하기)
# 시간초과 시 input먼저 바꿔보기

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
global visited
global nodes

def solution(i):
    for k in nodes[i]:
        if visited[k] == 0 : 
            visited[k] = 1
            solution(k)

N, M = map(int, input().split())
visited = [0]*(N+1)
answer = 0
nodes = [[] for _ in range(N+1)]

if M == 0: print(N)
else:
    for _ in range(M):
        u, v = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    #print(nodes)
    
    for i in range(1,N+1):
        if visited[i] == 0:
            visited[i] = 1
            #print('i:',i)
            if nodes[i] != [] : solution(i)
            answer += 1

    print(answer)
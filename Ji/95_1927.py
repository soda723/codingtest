# 백준 최소 힙 silver2
# 소요시간 : 10m
import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
# 연산1: 자연수 입력 > 배열에 넣음
# 연산2: 0 입력 > 배열에서 가장 작은 값을 출력, 제거
for _ in range(N):
    a = int(input())
    if a == 0 :
        if heap :
            print(heapq.heappop(heap))
        else : print(0)
            
    else : 
        heapq.heappush(heap, a)


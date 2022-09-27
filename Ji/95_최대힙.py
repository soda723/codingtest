# 백준 최대힙 silver2
# 소요시간 : 5m 30s
# 최소힙과 동일, 원소가 튜플 등이면 첫번째 원소로 정렬
import heapq
import sys
input = sys.stdin.readline

def solution():
    heap = []
    N = int(input())
    for _ in range(N):
        a = int(input())
        if a>0 : #자연수 넣기
            heapq.heappush(heap, (-a, a))
        else:
            if not len(heap): print(0)
            else: print(heapq.heappop(heap)[1])


if __name__ == '__main__':
    solution()
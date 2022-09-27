# 백준 절댓값 힙 silver1
# 소요시간 : 5m
# (참고)절댓값 함수로 abs() 가 있다. 
import heapq
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    heap = []
    for _ in range(N):
        a = int(input())
        if a == 0 : #꺼내기
            if len(heap) == 0 : print(0)
            else : print(heapq.heappop(heap)[1])
        elif a < 0 : #음수
            heapq.heappush(heap, (-a,a))
        else : #양수
            heapq.heappush(heap, (a,a))


if __name__ == '__main__' : 
    solve()
# 백준 2805번 나무자르기 # 이분탐색
# 소요시간 : 43m
# 런타임 에러
import sys
input = sys.stdin.readline

def solution(N, M, trees):
    left = max(trees) - M 
    right = max(trees)
    answer = 0

    while(left <= right):
        #print(left, right)
        tmp = 0
        answer = (right + left)//2 # 16

        for tree in trees:
            if tree > answer :
                tmp += tree- answer # 38
        
        if tmp == M : break
        elif M < tmp: 
            left = answer+1
        else : 
            right= answer-1

    return answer

N, M = map(int, input().split())
trees = list(map(int, input.split()))
print(solution(N,M,trees))


#print(solution(4, 7, [20,15, 10,17]))
#print(solution(5, 19, [4, 42, 40, 26, 46]))

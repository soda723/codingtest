# BOJ 25418 정수 a를 k로 만들기 silver3
# 소요시간 : 40m
# 다이나믹인거 알고 풀었음.. / 나중에 bps로도 도전
import sys
a, k = map(int, sys.stdin.readline().split())
cnt = 0
tmp = [0]*(k+1)
for i in range(a+1, k+1):
    if i // 2 >= a and i % 2 == 0 :
        tmp[i] = min(tmp[i-1], tmp[i//2]) +1  
    else:
        tmp[i] = tmp[i-1] +1

print(tmp[k])